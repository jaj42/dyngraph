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
        NewPlot.resize(578, 763)
        NewPlot.setSizeGripEnabled(False)
        self.verticalLayout_4 = QtGui.QVBoxLayout(NewPlot)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(NewPlot)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.txtFile = QtGui.QLineEdit(self.groupBox)
        self.txtFile.setObjectName(_fromUtf8("txtFile"))
        self.horizontalLayout_2.addWidget(self.txtFile)
        self.btnBrowse = QtGui.QPushButton(self.groupBox)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.horizontalLayout_2.addWidget(self.btnBrowse)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(NewPlot)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtGui.QFrame.Plain)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtSep = QtGui.QComboBox(NewPlot)
        self.txtSep.setEditable(True)
        self.txtSep.setObjectName(_fromUtf8("txtSep"))
        self.txtSep.addItem(_fromUtf8(""))
        self.txtSep.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtSep)
        self.label = QtGui.QLabel(NewPlot)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.txtDecimal = QtGui.QComboBox(NewPlot)
        self.txtDecimal.setEditable(True)
        self.txtDecimal.setObjectName(_fromUtf8("txtDecimal"))
        self.txtDecimal.addItem(_fromUtf8(""))
        self.txtDecimal.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtDecimal)
        self.label_7 = QtGui.QLabel(NewPlot)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtDateTime = QtGui.QComboBox(NewPlot)
        self.txtDateTime.setEditable(True)
        self.txtDateTime.setObjectName(_fromUtf8("txtDateTime"))
        self.txtDateTime.addItem(_fromUtf8(""))
        self.txtDateTime.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtDateTime)
        self.chkUnixTime = QtGui.QCheckBox(NewPlot)
        self.chkUnixTime.setObjectName(_fromUtf8("chkUnixTime"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.chkUnixTime)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.btnLoad = QtGui.QPushButton(NewPlot)
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.verticalLayout_4.addWidget(self.btnLoad)
        self.groupBox_2 = QtGui.QGroupBox(NewPlot)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lstVAll = QtGui.QTableView(self.groupBox_2)
        self.lstVAll.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lstVAll.setObjectName(_fromUtf8("lstVAll"))
        self.verticalLayout.addWidget(self.lstVAll)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnToX = QtGui.QPushButton(self.groupBox_2)
        self.btnToX.setObjectName(_fromUtf8("btnToX"))
        self.horizontalLayout.addWidget(self.btnToX)
        self.btnToY = QtGui.QPushButton(self.groupBox_2)
        self.btnToY.setObjectName(_fromUtf8("btnToY"))
        self.horizontalLayout.addWidget(self.btnToY)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_3 = QtGui.QGroupBox(NewPlot)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lstVY = QtGui.QListView(self.groupBox_3)
        self.lstVY.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lstVY.setObjectName(_fromUtf8("lstVY"))
        self.verticalLayout_5.addWidget(self.lstVY)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(NewPlot)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lstVX = QtGui.QListView(self.groupBox_4)
        self.lstVX.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lstVX.setObjectName(_fromUtf8("lstVX"))
        self.verticalLayout_6.addWidget(self.lstVX)
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(NewPlot)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.btnRemoveX = QtGui.QPushButton(NewPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemoveX.sizePolicy().hasHeightForWidth())
        self.btnRemoveX.setSizePolicy(sizePolicy)
        self.btnRemoveX.setObjectName(_fromUtf8("btnRemoveX"))
        self.horizontalLayout_5.addWidget(self.btnRemoveX)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.btnRemoveY = QtGui.QPushButton(NewPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemoveY.sizePolicy().hasHeightForWidth())
        self.btnRemoveY.setSizePolicy(sizePolicy)
        self.btnRemoveY.setObjectName(_fromUtf8("btnRemoveY"))
        self.gridLayout.addWidget(self.btnRemoveY, 1, 1, 1, 1, QtCore.Qt.AlignRight)
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
        self.groupBox_2.raise_()
        self.btnLoad.raise_()

        self.retranslateUi(NewPlot)
        QtCore.QMetaObject.connectSlotsByName(NewPlot)

    def retranslateUi(self, NewPlot):
        NewPlot.setWindowTitle(_translate("NewPlot", "New Plot", None))
        self.groupBox.setTitle(_translate("NewPlot", "Open File", None))
        self.btnBrowse.setText(_translate("NewPlot", "Browse", None))
        self.label_2.setText(_translate("NewPlot", "Field Seperator", None))
        self.txtSep.setItemText(0, _translate("NewPlot", ";", None))
        self.txtSep.setItemText(1, _translate("NewPlot", ",", None))
        self.label.setText(_translate("NewPlot", "Decimal seperator", None))
        self.txtDecimal.setItemText(0, _translate("NewPlot", ",", None))
        self.txtDecimal.setItemText(1, _translate("NewPlot", ".", None))
        self.label_7.setText(_translate("NewPlot", "Date/Time Format", None))
        self.txtDateTime.setItemText(0, _translate("NewPlot", "%Y-%m-%d %H:%M:%S,%f", None))
        self.txtDateTime.setItemText(1, _translate("NewPlot", "%Y-%m-%d %H:%M:%S.%f", None))
        self.chkUnixTime.setText(_translate("NewPlot", "Unix Timestamp", None))
        self.btnLoad.setText(_translate("NewPlot", "Load", None))
        self.groupBox_2.setTitle(_translate("NewPlot", "Loaded Fields", None))
        self.btnToX.setText(_translate("NewPlot", "Move to X", None))
        self.btnToY.setText(_translate("NewPlot", "Move to Y", None))
        self.groupBox_3.setTitle(_translate("NewPlot", "Data on Y axis", None))
        self.groupBox_4.setTitle(_translate("NewPlot", "Data on X axis", None))
        self.label_4.setText(_translate("NewPlot", "(Check to interpret as Date/Time)", None))
        self.btnRemoveX.setText(_translate("NewPlot", "Remove", None))
        self.btnRemoveY.setText(_translate("NewPlot", "Remove", None))
        self.btnOk.setText(_translate("NewPlot", "OK", None))
        self.btnCancel.setText(_translate("NewPlot", "Cancel", None))

