import os, sys
from datetime import datetime
from enum import Enum

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

import numpy as np
import pandas as pd
import pyqtgraph as pg

import algorithms
import exporter

class PlotFrame(QtGui.QWidget):
    layout = property(QtGui.QWidget.layout, QtGui.QWidget.setLayout)
    colors = [Qt.red, Qt.green, Qt.blue,
              Qt.cyan, Qt.magenta, Qt.yellow,
              Qt.darkRed, Qt.darkGreen, Qt.darkBlue,
              Qt.darkCyan, Qt.darkMagenta, Qt.darkYellow]

    def __init__(self, plotdata, parent=None):
        super().__init__(parent=parent)

        self.parent = parent
        self.plotdata = plotdata

        self.layout = QtGui.QHBoxLayout(self)

        if self.plotdata.xisdate:
            axisItems = {'bottom': TimeAxisItem(orientation='bottom')}
        else:
            axisItems = None

        #self.plotw = pg.PlotWidget(parent=self, axisItems=axisItems, background='w')
        self.plotw = pg.PlotWidget(parent=self, axisItems=axisItems)
        self.plotw.setAntialiasing(True)
        self.plotw.addLegend()
        self.layout.addWidget(self.plotw)

        self.vb = self.plotw.getViewBox()
        self.vb.setMouseMode(self.vb.RectMode)
        self.exporter = exporter.Exporter(self)

        self.addAllCurves()

    @property
    def curves(self):
        return {item.name() : item for item in self.plotw.listDataItems() if isinstance(item, CurveItem)}

    @property
    def feetitems(self):
        return {item.name() : item for item in self.plotw.listDataItems() if isinstance(item, FeetItem)}

    def addAllCurves(self):
        allSeries = (self.plotdata.data[c] for c in self.plotdata.yfields)
        for series in allSeries:
            self.addCurve(series)

    def addCurve(self, series):
        n = len(self.curves)
        if n >= len(self.colors):
            color = Qt.white
        else:
            color = self.colors[n]

        try:
            curve = CurveItem(series = series,
                                 pen    = QtGui.QColor(color))
        except ValueError as e:
            self.parent.haserror.emit(e)
        else:
            self.plotw.addItem(curve)

    def addFeet(self, curve, foottype):
        if foottype is FootType.pressure:
            feet = PressureFeetItem(curve)
            feet.sigClicked.connect(self.sigPointClicked)
            self.plotw.addItem(feet)
        elif foottype is FootType.velocity:
            start = VelocityFeetItem(curve, isend=False)
            start.sigClicked.connect(self.sigPointClicked)
            self.plotw.addItem(start)
            stop = VelocityFeetItem(curve, isend=True)
            stop.sigClicked.connect(self.sigPointClicked)
            self.plotw.addItem(stop)
        else:
            return

    def sigPointClicked(self, curve, points):
        point = points[0] # keep the first point
        if not curve.isPointSelected(point):
            curve.selectPoint(point)
        else:
            curve.unselectPoint(point)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            for curve in self.feetitems.values():
                curve.removeSelection()


class CurveItem(pg.PlotDataItem):
    def __init__(self, series, pen=QtGui.QColor(Qt.white), parent=None):
        self.series = series
        #self.pen = pg.mkPen(pen, width=2)
        self.pen = pen
        super().__init__(x    = self.series.index.astype(np.int64),
                         y    = self.series.values.astype(np.float64),
                         name = self.series.name,
                         pen  = self.pen,
                         *args, **kwargs)


class FeetItem(pg.ScatterPlotItem):
    def __init__(self, feet, curve, namesuffix='feet', *args, **kwargs):
        self.selected = []
        pen = curve.opts['pen']
        self._name = "{}-{}".format(curve.name(), namesuffix)
        super().__init__(x    = feet.index.astype(np.int64),
                         y    = feet.values.astype(np.float64),
                         pen  = pen,
                         *args, **kwargs)

    def name(self):
        return self._name

    @property
    def feet(self):
        points = self.points()
        time   = [point.pos().x() for point in points]
        values = [point.pos().y() for point in points]
        return pd.Series(data  = values,
                         index = pd.to_datetime(time, unit='ns'),
                         name  = self.name())

    def isPointSelected(self, point):
        return point in self.selected

    def selectPoint(self, point):
        if not self.isPointSelected(point):
            self.selected.append(point)
        point.setBrush('r')

    def unselectPoint(self, point):
        if self.isPointSelected(point):
            self.selected.remove(point)
        point.resetBrush()

    def removePoints(self, points):
        datapoints = self.points().tolist()
        for point in points:
            try:
                datapoints.remove(point)
            except ValueError as e:
                print("Point not found: {}".format(e), sys.stderr)
                continue
        self.setData(pos = [(p.pos().x(), p.pos().y()) for p in datapoints])
        self.selected = []

    def removeSelection(self):
        return self.removePoints(self.selected)


class PressureFeetItem(FeetItem):
    def __init__(self, curve):
        feet = algorithms.findPressureFeet(curve.series)
        super().__init__(feet, curve)


class VelocityFeetItem(FeetItem):
    def __init__(self, curve, isend=False):
        starts, stops = algorithms.findFlowCycles(curve.series)
        if isend:
            super().__init__(stops, curve, namesuffix='velstop', symbol='s')
        else:
            super().__init__(starts, curve, namesuffix='velstart', symbol='t')


class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        ret = []
        for value in values:
            value = value / 1e6 # convert from ns to ms
            date = QtCore.QDateTime.fromMSecsSinceEpoch(value)
            date = date.toTimeSpec(Qt.UTC)
            datestr = date.toString("hh:mm:ss.zzz")
            ret.append(datestr)
        return ret

class PlotDescription():
    def __init__(self, filepath  = "",
                       seperator = ",",
                       decimal   = ".",
                       xfield  = None,
                       yfields = [],
                       xisdate = False,
                       isunixtime = False,
                       loadall = False,
                       datetime_format = "%Y-%m-%d %H:%M:%S,%f"):
        self.filepath = filepath
        self.seperator = seperator
        self.decimal = decimal
        self.xfield  = xfield
        self.yfields = yfields
        self.loadall = loadall
        self.datetime_format = datetime_format
        self.xisdate = xisdate
        self.isunixtime = isunixtime
        self.data = None

    @property
    def fields(self):
        xfields = [] if self.xfield is None else [self.xfield]
        return xfields + self.yfields

    @property
    def datefield(self):
        if not self.xisdate: return False
        return self.xfield if self.xfield is not None else False

    @property
    def xvalues(self):
        if not self.xisdate and self.xfield is not None:
            values = self.data[self.xfield].values
            return values.astype(np.float64)
        else:
            return None

    @property
    def name(self):
        name, _ = os.path.splitext(os.path.basename(self.filepath))
        return name

class FootType(Enum):
    none     = 'None'
    pressure = 'Pressure'
    velocity = 'Velocity'
