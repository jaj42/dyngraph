# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'periodexport.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PeriodExport(object):
    def setupUi(self, PeriodExport):
        PeriodExport.setObjectName("PeriodExport")
        PeriodExport.resize(255, 237)
        self.verticalLayout = QtWidgets.QVBoxLayout(PeriodExport)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(PeriodExport)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.btnBrowse = QtWidgets.QPushButton(self.groupBox)
        self.btnBrowse.setObjectName("btnBrowse")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btnBrowse)
        self.txtFile = QtWidgets.QLineEdit(self.groupBox)
        self.txtFile.setObjectName("txtFile")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.txtFile)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(PeriodExport)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblPeriodStart = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lblPeriodStart.sizePolicy().hasHeightForWidth()
        )
        self.lblPeriodStart.setSizePolicy(sizePolicy)
        self.lblPeriodStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPeriodStart.setObjectName("lblPeriodStart")
        self.horizontalLayout_2.addWidget(self.lblPeriodStart)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lblPeriodStop = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lblPeriodStop.sizePolicy().hasHeightForWidth()
        )
        self.lblPeriodStop.setSizePolicy(sizePolicy)
        self.lblPeriodStop.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPeriodStop.setObjectName("lblPeriodStop")
        self.horizontalLayout_2.addWidget(self.lblPeriodStop)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(PeriodExport)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtPatient = QtWidgets.QLineEdit(PeriodExport)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPatient.sizePolicy().hasHeightForWidth())
        self.txtPatient.setSizePolicy(sizePolicy)
        self.txtPatient.setObjectName("txtPatient")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtPatient)
        self.label_7 = QtWidgets.QLabel(PeriodExport)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txtPeriod = QtWidgets.QComboBox(PeriodExport)
        self.txtPeriod.setEditable(True)
        self.txtPeriod.setObjectName("txtPeriod")
        self.txtPeriod.addItem("")
        self.txtPeriod.addItem("")
        self.txtPeriod.addItem("")
        self.txtPeriod.addItem("")
        self.txtPeriod.addItem("")
        self.txtPeriod.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPeriod)
        self.label_2 = QtWidgets.QLabel(PeriodExport)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtComment = QtWidgets.QLineEdit(PeriodExport)
        self.txtComment.setObjectName("txtComment")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtComment)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnOk = QtWidgets.QPushButton(PeriodExport)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout_3.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(PeriodExport)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(PeriodExport)
        QtCore.QMetaObject.connectSlotsByName(PeriodExport)

    def retranslateUi(self, PeriodExport):
        _translate = QtCore.QCoreApplication.translate
        PeriodExport.setWindowTitle(
            _translate("PeriodExport", "Export period information")
        )
        self.groupBox.setTitle(_translate("PeriodExport", "Destination file"))
        self.btnBrowse.setText(_translate("PeriodExport", "Browse"))
        self.groupBox_2.setTitle(_translate("PeriodExport", "Period"))
        self.lblPeriodStart.setText(_translate("PeriodExport", "Beginning"))
        self.label_3.setText(_translate("PeriodExport", "-"))
        self.lblPeriodStop.setText(_translate("PeriodExport", "End"))
        self.label.setText(_translate("PeriodExport", "Patient"))
        self.label_7.setText(_translate("PeriodExport", "Period Identification"))
        self.txtPeriod.setItemText(0, _translate("PeriodExport", "carotid"))
        self.txtPeriod.setItemText(1, _translate("PeriodExport", "ascending"))
        self.txtPeriod.setItemText(2, _translate("PeriodExport", "descending"))
        self.txtPeriod.setItemText(3, _translate("PeriodExport", "renal"))
        self.txtPeriod.setItemText(4, _translate("PeriodExport", "iliac"))
        self.txtPeriod.setItemText(5, _translate("PeriodExport", "bolus"))
        self.label_2.setText(_translate("PeriodExport", "Comment"))
        self.btnOk.setText(_translate("PeriodExport", "Ok"))
        self.btnCancel.setText(_translate("PeriodExport", "Cancel"))
