# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designer\newplot.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewPlot(object):
    def setupUi(self, NewPlot):
        NewPlot.setObjectName(_fromUtf8("NewPlot"))
        NewPlot.resize(401, 763)
        NewPlot.setSizeGripEnabled(False)
        self.verticalLayout_4 = QtGui.QVBoxLayout(NewPlot)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(NewPlot)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtFile = QtGui.QLineEdit(self.groupBox)
        self.txtFile.setObjectName(_fromUtf8("txtFile"))
        self.horizontalLayout.addWidget(self.txtFile)
        self.btnBrowse = QtGui.QPushButton(self.groupBox)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(NewPlot)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txtSep = QtGui.QComboBox(NewPlot)
        self.txtSep.setEditable(True)
        self.txtSep.setObjectName(_fromUtf8("txtSep"))
        self.txtSep.addItem(_fromUtf8(""))
        self.txtSep.addItem(_fromUtf8(""))
        self.txtSep.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtSep)
        self.label1 = QtGui.QLabel(NewPlot)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label1)
        self.txtDecimal = QtGui.QComboBox(NewPlot)
        self.txtDecimal.setEditable(True)
        self.txtDecimal.setObjectName(_fromUtf8("txtDecimal"))
        self.txtDecimal.addItem(_fromUtf8(""))
        self.txtDecimal.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtDecimal)
        self.label_7 = QtGui.QLabel(NewPlot)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtDateTime = QtGui.QComboBox(NewPlot)
        self.txtDateTime.setEditable(True)
        self.txtDateTime.setObjectName(_fromUtf8("txtDateTime"))
        self.txtDateTime.addItem(_fromUtf8(""))
        self.txtDateTime.addItem(_fromUtf8(""))
        self.txtDateTime.addItem(_fromUtf8(""))
        self.txtDateTime.addItem(_fromUtf8(""))
        self.txtDateTime.addItem(_fromUtf8(""))
        self.txtDateTime.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtDateTime)
        self.chkLoadNotAll = QtGui.QCheckBox(NewPlot)
        self.chkLoadNotAll.setChecked(True)
        self.chkLoadNotAll.setObjectName(_fromUtf8("chkLoadNotAll"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.chkLoadNotAll)
        self.label_3 = QtGui.QLabel(NewPlot)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spnLinedrop = QtGui.QSpinBox(NewPlot)
        self.spnLinedrop.setObjectName(_fromUtf8("spnLinedrop"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spnLinedrop)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.btnLoad = QtGui.QPushButton(NewPlot)
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.verticalLayout_4.addWidget(self.btnLoad)
        self.groupBox1 = QtGui.QGroupBox(NewPlot)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lstVAll = QtGui.QTableView(self.groupBox1)
        self.lstVAll.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lstVAll.setObjectName(_fromUtf8("lstVAll"))
        self.verticalLayout.addWidget(self.lstVAll)
        self.horizontalLayout1 = QtGui.QHBoxLayout()
        self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
        self.btnToX = QtGui.QPushButton(self.groupBox1)
        self.btnToX.setObjectName(_fromUtf8("btnToX"))
        self.horizontalLayout1.addWidget(self.btnToX)
        self.btnToY = QtGui.QPushButton(self.groupBox1)
        self.btnToY.setObjectName(_fromUtf8("btnToY"))
        self.horizontalLayout1.addWidget(self.btnToY)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.verticalLayout_4.addWidget(self.groupBox1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(NewPlot)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.lstVY = QtGui.QListView(self.groupBox_5)
        self.lstVY.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lstVY.setObjectName(_fromUtf8("lstVY"))
        self.verticalLayout_7.addWidget(self.lstVY)
        self.gridLayout.addWidget(self.groupBox_5, 1, 1, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(NewPlot)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.lstVX = QtGui.QComboBox(self.groupBox_6)
        self.lstVX.setMaxCount(4)
        self.lstVX.setObjectName(_fromUtf8("lstVX"))
        self.verticalLayout_8.addWidget(self.lstVX)
        self.label_5 = QtGui.QLabel(self.groupBox_6)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_8.addWidget(self.label_5)
        self.gridLayout.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.btnRemoveY = QtGui.QPushButton(NewPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemoveY.sizePolicy().hasHeightForWidth())
        self.btnRemoveY.setSizePolicy(sizePolicy)
        self.btnRemoveY.setObjectName(_fromUtf8("btnRemoveY"))
        self.gridLayout.addWidget(self.btnRemoveY, 1, 2, 1, 1)
        self.btnRemoveX = QtGui.QPushButton(NewPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemoveX.sizePolicy().hasHeightForWidth())
        self.btnRemoveX.setSizePolicy(sizePolicy)
        self.btnRemoveX.setObjectName(_fromUtf8("btnRemoveX"))
        self.gridLayout.addWidget(self.btnRemoveX, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnOk = QtGui.QPushButton(NewPlot)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.horizontalLayout_3.addWidget(self.btnOk)
        self.btnCancel = QtGui.QPushButton(NewPlot)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.groupBox.raise_()
        self.groupBox.raise_()
        self.btnLoad.raise_()

        self.retranslateUi(NewPlot)
        QtCore.QMetaObject.connectSlotsByName(NewPlot)

    def retranslateUi(self, NewPlot):
        NewPlot.setWindowTitle(_translate("NewPlot", "New Plot", None))
        self.groupBox.setTitle(_translate("NewPlot", "Open File", None))
        self.btnBrowse.setText(_translate("NewPlot", "Browse", None))
        self.label.setText(_translate("NewPlot", "Field Seperator", None))
        self.txtSep.setItemText(0, _translate("NewPlot", ";", None))
        self.txtSep.setItemText(1, _translate("NewPlot", ",", None))
        self.txtSep.setItemText(2, _translate("NewPlot", "<tab>", None))
        self.label1.setText(_translate("NewPlot", "Decimal Seperator", None))
        self.txtDecimal.setItemText(0, _translate("NewPlot", ",", None))
        self.txtDecimal.setItemText(1, _translate("NewPlot", ".", None))
        self.label_7.setText(_translate("NewPlot", "Date/Time Format", None))
        self.txtDateTime.setItemText(0, _translate("NewPlot", "%Y-%m-%d %H:%M:%S,%f", None))
        self.txtDateTime.setItemText(1, _translate("NewPlot", "%Y-%m-%d %H:%M:%S.%f", None))
        self.txtDateTime.setItemText(2, _translate("NewPlot", "%H:%M", None))
        self.txtDateTime.setItemText(3, _translate("NewPlot", "<seconds>", None))
        self.txtDateTime.setItemText(4, _translate("NewPlot", "<milliseconds>", None))
        self.txtDateTime.setItemText(5, _translate("NewPlot", "<nanoseconds>", None))
        self.chkLoadNotAll.setText(_translate("NewPlot", "Load only selected Series", None))
        self.label_3.setText(_translate("NewPlot", "Drop n first lines", None))
        self.btnLoad.setText(_translate("NewPlot", "Load Fields", None))
        self.groupBox1.setTitle(_translate("NewPlot", "Loaded Fields", None))
        self.btnToX.setText(_translate("NewPlot", "Move to X", None))
        self.btnToY.setText(_translate("NewPlot", "Move to Y", None))
        self.groupBox_5.setTitle(_translate("NewPlot", "Series on Y axis", None))
        self.groupBox_6.setTitle(_translate("NewPlot", "Series on X axis", None))
        self.label_5.setText(_translate("NewPlot", "(Check to interpret as Date/Time)", None))
        self.btnRemoveY.setText(_translate("NewPlot", "Remove", None))
        self.btnRemoveX.setText(_translate("NewPlot", "Remove", None))
        self.btnOk.setText(_translate("NewPlot", "OK", None))
        self.btnCancel.setText(_translate("NewPlot", "Cancel", None))

