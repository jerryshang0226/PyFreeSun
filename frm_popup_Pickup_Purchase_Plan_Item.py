# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_popup_Pickup_Purchase_Plan_Item.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_popup_Pickup_Purchase_Plan_Item(object):
    def setupUi(self, popup_Pickup_Purchase_Plan_Item):
        popup_Pickup_Purchase_Plan_Item.setObjectName("popup_Pickup_Purchase_Plan_Item")
        popup_Pickup_Purchase_Plan_Item.resize(926, 760)
        self.centralwidget = QtWidgets.QWidget(popup_Pickup_Purchase_Plan_Item)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 891, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pbtn_Pick = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Pick.setGeometry(QtCore.QRect(710, 670, 88, 23))
        self.pbtn_Pick.setObjectName("pbtn_Pick")
        self.pbtn_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Quit.setGeometry(QtCore.QRect(810, 670, 88, 23))
        self.pbtn_Quit.setObjectName("pbtn_Quit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 211, 16))
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(280, 10, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 350, 891, 271))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pbtn_Add = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Add.setGeometry(QtCore.QRect(730, 300, 88, 23))
        self.pbtn_Add.setObjectName("pbtn_Add")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 630, 451, 71))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 640, 72, 15))
        self.label_2.setObjectName("label_2")
        popup_Pickup_Purchase_Plan_Item.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(popup_Pickup_Purchase_Plan_Item)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 23))
        self.menubar.setObjectName("menubar")
        popup_Pickup_Purchase_Plan_Item.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(popup_Pickup_Purchase_Plan_Item)
        self.statusbar.setObjectName("statusbar")
        popup_Pickup_Purchase_Plan_Item.setStatusBar(self.statusbar)

        self.retranslateUi(popup_Pickup_Purchase_Plan_Item)
        QtCore.QMetaObject.connectSlotsByName(popup_Pickup_Purchase_Plan_Item)

    def retranslateUi(self, popup_Pickup_Purchase_Plan_Item):
        _translate = QtCore.QCoreApplication.translate
        popup_Pickup_Purchase_Plan_Item.setWindowTitle(_translate("popup_Pickup_Purchase_Plan_Item", "建立采购申请单"))
        self.pbtn_Pick.setText(_translate("popup_Pickup_Purchase_Plan_Item", "申请"))
        self.pbtn_Quit.setText(_translate("popup_Pickup_Purchase_Plan_Item", "退出"))
        self.label.setText(_translate("popup_Pickup_Purchase_Plan_Item", "申请在此时间内采购选中目标"))
        self.pbtn_Add.setText(_translate("popup_Pickup_Purchase_Plan_Item", "添加"))
        self.label_2.setText(_translate("popup_Pickup_Purchase_Plan_Item", "申请事由："))
