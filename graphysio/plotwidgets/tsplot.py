from functools import partial

import numpy as np
import pandas as pd
import pyqtgraph as pg

from pyqtgraph.Qt import QtGui, QtCore

from graphysio import algorithms, exporter, utils, dialogs
from graphysio.types import CycleId

from graphysio.plotwidgets.plotwidget import PlotWidget, CurveItem

class CurveItemWithFeet(CurveItem):
    visible = QtCore.pyqtSignal()
    invisible = QtCore.pyqtSignal()

    @staticmethod
    def sigPointClicked(feetitem, points):
        point = points[0] # only one point per click
        if not feetitem.isPointSelected(point):
            feetitem.selectPoint(point)
        else:
            feetitem.unselectPoint(point)

    def __init__(self, series, parent, pen=None):
        super().__init__(series, parent, pen)
        feetname = '{}-feet'.format(series.name)
        self.feetitem = PointsItem(self, name=feetname, pen=pen)
        parent.addItem(self.feetitem)
        self.feetitem.sigClicked.connect(self.sigPointClicked)
        self.visible.connect(self.__becameVisible)
        self.invisible.connect(self.__becameInvisible)

    def __becameVisible(self):
        if not self.feetitem in self.parent.listDataItems():
            self.parent.addItem(self.feetitem)
        self.render()
        self.feetitem.render()

    def __becameInvisible(self):
        self.parent.removeItem(self.feetitem)

    def addFeet(self, cycleid):
        if cycleid is CycleId.none:
            return
        elif cycleid is CycleId.velocity:
            starts, stops = algorithms.findFlowCycles(self)
            self.feetitem.indices['start'] = starts
            self.feetitem.indices['stop'] = stops
        elif cycleid is CycleId.foot:
            foot = algorithms.findPressureFeet(self)
            self.feetitem.indices['start'] = foot
        elif cycleid is CycleId.pressure:
            if not 'start' in self.feetitem.indices:
                self.addFeet(CycleId.foot)
            dia, sbp, dic = algorithms.findPressureFull(self)
            self.feetitem.indices['diastole'] = dia
            self.feetitem.indices['systole']  = sbp
            self.feetitem.indices['dicrotic'] = dic
        else:
            raise ValueError(cycleid)
        self.feetitem.render()

    def getCycleIndices(self, vrange=None):
        s = self.series
        clip = partial(utils.clip, vrange=vrange)
        hasstarts = ('start' in self.feetitem.indices) and self.feetitem.indices['start'].size > 0
        hasstops = ('stop' in self.feetitem.indices) and self.feetitem.indices['stop'].size > 0
        if vrange:
            xmin, xmax = vrange
        else:
            xmin = s.index[0]
            xmax = s.index[-1]
        if not hasstarts:
            # We have no feet, treat the whole signal as one cycle
            locs = (s.index.get_loc(i, method='nearest') for i in [xmin, xmax])
            indices = (s.index[l] for l in locs)
            begins, ends = [np.array([i]) for i in indices]
        elif not hasstops:
            # We have no stops, starts serve as stops for previous cycle
            begins = clip(self.feetitem.indices['start'].values)
            endloc = s.index.get_loc(xmax, method='nearest')
            end = s.index[endloc]
            ends = np.append(begins[1:], end)
        else:
            # We have starts and stops, use them
            begins = self.feetitem.indices['start'].values
            ends = self.feetitem.indices['stop'].values
            begins, ends = map(clip, [begins, ends])

        # Handle the case where we start in the middle of a cycle
        while ends[0] <= begins[0]:
            ends = ends[1:]

        begins, ends = utils.truncatevecs([begins, ends])
        durations = ends - begins
        return (begins, durations)

    def getFeetPoints(self, feetname):
        feetidx = self.feetitem.indices[feetname]
        feetnona = feetidx[pd.notnull(feetidx)]
        return self.series.loc[feetnona]


class TSWidget(PlotWidget):
    def __init__(self, plotdata, parent=None):
        super().__init__(parent=parent, CurveClass=CurveItemWithFeet)
        self.exporter = exporter.TsExporter(self, plotdata.name)
        self.appendData(plotdata)

    def filterCurve(self, oldcurve, filtername, asnew=False):
        newseries, newsamplerate = algorithms.filter(oldcurve, filtername, dialogs.askUserValue)
        if asnew:
            newcurve = self.addSeriesAsCurve(series=newseries)
            newcurve.samplerate = newsamplerate
        else:
            oldname = oldcurve.series.name
            newseries.name = oldname
            oldcurve.series = newseries
            oldcurve.samplerate = newsamplerate
            oldcurve.render()

    def filterFeet(self, curve, filtername, asnew=False):
        oldstarts = curve.feet['start']
        oldstops = curve.feet['stop']
        starts, stops = algorithms.filterFeet(oldstarts, oldstops, filtername, dialogs.askUserValue)
        curve.feet['start'] = starts
        curve.feet['stop'] = stops
        curve.feetitem.render()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            for curve in self.curves.values():
                curve.feetitem.removeSelection()

    def showCurveList(self):
        dlgCurveSelection = dialogs.DlgCurveSelection(parent=self, visible=self.curves.values(), hidden=self.hiddenitems)
        if not dlgCurveSelection.exec_():
            return
        visible, invisible = dlgCurveSelection.result
        newvisible = [item for item in visible if item not in self.curves.values()]
        newinvisible = [item for item in invisible if item not in self.hiddenitems]
        for item in newvisible:
            self.addCurve(item)
            if item in self.hiddenitems:
                self.hiddenitems.remove(item)

        for item in newinvisible:
            self.removeCurve(item)
            if item not in self.hiddenitems:
                self.hiddenitems.append(item)

    @property
    def exportMenu(self):
        menu = super().exportMenu.copy()
        newm = {'&Series to CSV'           : self.exporter.seriestocsv
               ,'&Time info to CSV'        : self.exporter.periodstocsv
               ,'&Cycle info to CSV'       : self.exporter.cyclepointstocsv
               ,'&Cycles to CSV directory' : self.exporter.cyclestocsv
               }
        menu.update(newm)
        return menu


class PointsItem(pg.ScatterPlotItem):
    sym = {'start' : 'star', 'stop' : 's', 'diastole' : 't1', 'systole' : 't', 'dicrotic' : 'd'}
    #Symbols = OrderedDict([(name, QtGui.QPainterPath()) for name in ['o', 's', 't', 't1', 't2', 't3','d', '+', 'x', 'p', 'h', 'star']])

    def __init__(self, parent, name, indices={}, pen=None):
        super().__init__(pen=pen)
        self.parent = parent
        self.indices = indices
        self.selected = []
        self.resym = {value : key for key, value in self.sym.items()}
        self.__name = name
        self.render()

    def addPoints_(self, key, locations):
        if not key in self.indices:
            self.indices[key] = pd.Index([])
        newlocs = []
        for loc in locations:
            locfixed = self.parent.series.index.get_loc(loc, method='nearest')
            locfixed = self.parent.series.index[locfixed]
            newlocs.append(locfixed)
        oldidx = self.indices[key]
        newidx = oldidx.append(pd.Index(newlocs))
        self.indices[key] = newidx.unique().sort_values()
        self.render()

    def removePoints_(self, key, locations):
        if not key in self.indices:
            return
        oldidx = self.indices[key]
        dellocs = []
        for loc in locations:
            locidx = oldidx.get_loc(loc, method='nearest')
            dellocs.append(locidx)
        newidx = oldidx.delete(dellocs)
        self.indices[key] = newidx
        self.render()

    def removePoints(self, points):
        for point in points:
            try:
                sym = self.resym[point.symbol()]
                idx = self.indices[sym]
            except KeyError:
                # Should not happen
                continue
            nidx = idx.get_loc(point.pos().x(), method='nearest')
            self.indices[sym] = idx.delete(nidx)
        self.render()

    def render(self):
        data = []
        for key, idx in self.indices.items():
            idxnona = idx.dropna()
            points = self.parent.series[idxnona]
            tmp = pd.DataFrame({'points' : points, 'sym' : self.sym[key]}, index=idxnona)
            data.append(tmp)
        if len(data) < 1:
            return
        feet = pd.concat(data)
        self.setData(x = feet.index.values,
                     y = feet['points'].values,
                     symbol = feet['sym'].values)

    def isPointSelected(self, point):
        return point in self.selected

    def selectPoint(self, point):
        if not self.isPointSelected(point):
            self.selected.append(point)
        point.setPen('r')
        point.setBrush('r')

    def unselectPoint(self, point):
        if self.isPointSelected(point):
            self.selected.remove(point)
        point.resetPen()
        point.resetBrush()

    def removeSelection(self):
        self.removePoints(self.selected)
        self.selected = []
        self.render()

    def name(self):
        # Method needed for compat with CurveItem
        return self.__name