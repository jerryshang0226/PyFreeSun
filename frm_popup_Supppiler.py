# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_popup_Supppiler.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_popup_Suppiler(object):
    def setupUi(self, popup_Suppiler):
        popup_Suppiler.setObjectName("popup_Suppiler")
        popup_Suppiler.resize(945, 416)
        self.centralwidget = QtWidgets.QWidget(popup_Suppiler)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 891, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pbtn_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Cancel.setGeometry(QtCore.QRect(540, 10, 88, 23))
        self.pbtn_Cancel.setObjectName("pbtn_Cancel")
        self.pbtn_New = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_New.setGeometry(QtCore.QRect(180, 10, 88, 23))
        self.pbtn_New.setObjectName("pbtn_New")
        self.pbtn_Run = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Run.setGeometry(QtCore.QRect(450, 10, 88, 23))
        self.pbtn_Run.setObjectName("pbtn_Run")
        self.pbtn_Modify = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Modify.setGeometry(QtCore.QRect(630, 10, 88, 23))
        self.pbtn_Modify.setObjectName("pbtn_Modify")
        self.pbtn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Delete.setGeometry(QtCore.QRect(810, 10, 88, 23))
        self.pbtn_Delete.setObjectName("pbtn_Delete")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pbtn_Query = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Query.setGeometry(QtCore.QRect(360, 10, 88, 23))
        self.pbtn_Query.setObjectName("pbtn_Query")
        self.pbtn_Pick = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Pick.setGeometry(QtCore.QRect(710, 330, 88, 23))
        self.pbtn_Pick.setObjectName("pbtn_Pick")
        self.pbtn_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Quit.setGeometry(QtCore.QRect(810, 330, 88, 23))
        self.pbtn_Quit.setObjectName("pbtn_Quit")
        self.pbtn_Save = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Save.setGeometry(QtCore.QRect(270, 10, 88, 23))
        self.pbtn_Save.setObjectName("pbtn_Save")
        self.pbtn_Update = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Update.setGeometry(QtCore.QRect(720, 10, 88, 23))
        self.pbtn_Update.setObjectName("pbtn_Update")
        popup_Suppiler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(popup_Suppiler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 23))
        self.menubar.setObjectName("menubar")
        popup_Suppiler.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(popup_Suppiler)
        self.statusbar.setObjectName("statusbar")
        popup_Suppiler.setStatusBar(self.statusbar)

        self.retranslateUi(popup_Suppiler)
        QtCore.QMetaObject.connectSlotsByName(popup_Suppiler)

    def retranslateUi(self, popup_Suppiler):
        _translate = QtCore.QCoreApplication.translate
        popup_Suppiler.setWindowTitle(_translate("popup_Suppiler", "供应商"))
        self.pbtn_Cancel.setText(_translate("popup_Suppiler", "取消"))
        self.pbtn_New.setText(_translate("popup_Suppiler", "新建"))
        self.pbtn_Run.setText(_translate("popup_Suppiler", "执行"))
        self.pbtn_Modify.setText(_translate("popup_Suppiler", "修改"))
        self.pbtn_Delete.setText(_translate("popup_Suppiler", "删除"))
        self.label_2.setText(_translate("popup_Suppiler", "客户清单↓"))
        self.pbtn_Query.setText(_translate("popup_Suppiler", "查询"))
        self.pbtn_Pick.setText(_translate("popup_Suppiler", "选择"))
        self.pbtn_Quit.setText(_translate("popup_Suppiler", "退出"))
        self.pbtn_Save.setText(_translate("popup_Suppiler", "保存"))
        self.pbtn_Update.setText(_translate("popup_Suppiler", "更新"))