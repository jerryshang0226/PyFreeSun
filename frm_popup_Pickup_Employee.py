# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_popup_Pickup_Employee.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_popup_Pickup_Employee(object):
    def setupUi(self, popup_Pickup_Employee):
        popup_Pickup_Employee.setObjectName("popup_Pickup_Employee")
        popup_Pickup_Employee.resize(965, 420)
        self.centralwidget = QtWidgets.QWidget(popup_Pickup_Employee)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 941, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pbtn_Pick = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Pick.setGeometry(QtCore.QRect(720, 330, 93, 28))
        self.pbtn_Pick.setObjectName("pbtn_Pick")
        self.pbtn_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Cancel.setGeometry(QtCore.QRect(850, 330, 93, 28))
        self.pbtn_Cancel.setObjectName("pbtn_Cancel")
        popup_Pickup_Employee.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(popup_Pickup_Employee)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 23))
        self.menubar.setObjectName("menubar")
        popup_Pickup_Employee.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(popup_Pickup_Employee)
        self.statusbar.setObjectName("statusbar")
        popup_Pickup_Employee.setStatusBar(self.statusbar)

        self.retranslateUi(popup_Pickup_Employee)
        QtCore.QMetaObject.connectSlotsByName(popup_Pickup_Employee)

    def retranslateUi(self, popup_Pickup_Employee):
        _translate = QtCore.QCoreApplication.translate
        popup_Pickup_Employee.setWindowTitle(_translate("popup_Pickup_Employee", "雇员"))
        self.pbtn_Pick.setText(_translate("popup_Pickup_Employee", "保存"))
        self.pbtn_Cancel.setText(_translate("popup_Pickup_Employee", "取消"))