# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_popup_Pickup_Purchase_Plan.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_popup_Pickup_Purchase_Plan(object):
    def setupUi(self, popup_Pickup_Purchase_Plan):
        popup_Pickup_Purchase_Plan.setObjectName("popup_Pickup_Purchase_Plan")
        popup_Pickup_Purchase_Plan.resize(921, 478)
        self.centralwidget = QtWidgets.QWidget(popup_Pickup_Purchase_Plan)
        self.centralwidget.setObjectName("centralwidget")
        self.tbw_Project_PurchaseList_Plan = QtWidgets.QTableWidget(self.centralwidget)
        self.tbw_Project_PurchaseList_Plan.setGeometry(QtCore.QRect(10, 50, 901, 141))
        self.tbw_Project_PurchaseList_Plan.setObjectName("tbw_Project_PurchaseList_Plan")
        self.tbw_Project_PurchaseList_Plan.setColumnCount(0)
        self.tbw_Project_PurchaseList_Plan.setRowCount(0)
        self.label_122 = QtWidgets.QLabel(self.centralwidget)
        self.label_122.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_122.setObjectName("label_122")
        self.label_73 = QtWidgets.QLabel(self.centralwidget)
        self.label_73.setGeometry(QtCore.QRect(20, 210, 121, 16))
        self.label_73.setObjectName("label_73")
        self.tbw_Project_PurchaseList_Plan_Item = QtWidgets.QTableWidget(self.centralwidget)
        self.tbw_Project_PurchaseList_Plan_Item.setGeometry(QtCore.QRect(10, 240, 901, 141))
        self.tbw_Project_PurchaseList_Plan_Item.setObjectName("tbw_Project_PurchaseList_Plan_Item")
        self.tbw_Project_PurchaseList_Plan_Item.setColumnCount(0)
        self.tbw_Project_PurchaseList_Plan_Item.setRowCount(0)
        self.pbtn_Pick = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Pick.setGeometry(QtCore.QRect(710, 410, 88, 23))
        self.pbtn_Pick.setObjectName("pbtn_Pick")
        self.pbtn_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Quit.setGeometry(QtCore.QRect(810, 410, 88, 23))
        self.pbtn_Quit.setObjectName("pbtn_Quit")
        popup_Pickup_Purchase_Plan.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(popup_Pickup_Purchase_Plan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 23))
        self.menubar.setObjectName("menubar")
        popup_Pickup_Purchase_Plan.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(popup_Pickup_Purchase_Plan)
        self.statusbar.setObjectName("statusbar")
        popup_Pickup_Purchase_Plan.setStatusBar(self.statusbar)

        self.retranslateUi(popup_Pickup_Purchase_Plan)
        QtCore.QMetaObject.connectSlotsByName(popup_Pickup_Purchase_Plan)

    def retranslateUi(self, popup_Pickup_Purchase_Plan):
        _translate = QtCore.QCoreApplication.translate
        popup_Pickup_Purchase_Plan.setWindowTitle(_translate("popup_Pickup_Purchase_Plan", "计划任务"))
        self.label_122.setText(_translate("popup_Pickup_Purchase_Plan", "计划清单"))
        self.label_73.setText(_translate("popup_Pickup_Purchase_Plan", "计划清单内容"))
        self.pbtn_Pick.setText(_translate("popup_Pickup_Purchase_Plan", "选择"))
        self.pbtn_Quit.setText(_translate("popup_Pickup_Purchase_Plan", "退出"))
