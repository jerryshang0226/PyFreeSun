# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_popup_Project.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_popup_Project(object):
    def setupUi(self, popup_Project):
        popup_Project.setObjectName("popup_Project")
        popup_Project.resize(949, 425)
        self.centralwidget = QtWidgets.QWidget(popup_Project)
        self.centralwidget.setObjectName("centralwidget")
        self.pbtn_Query = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Query.setGeometry(QtCore.QRect(360, 0, 88, 23))
        self.pbtn_Query.setObjectName("pbtn_Query")
        self.pbtn_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Cancel.setGeometry(QtCore.QRect(540, 0, 88, 23))
        self.pbtn_Cancel.setObjectName("pbtn_Cancel")
        self.pbtn_Save = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Save.setGeometry(QtCore.QRect(270, 0, 88, 23))
        self.pbtn_Save.setObjectName("pbtn_Save")
        self.pbtn_Update = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Update.setGeometry(QtCore.QRect(720, 0, 88, 23))
        self.pbtn_Update.setObjectName("pbtn_Update")
        self.pbtn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Delete.setGeometry(QtCore.QRect(810, 0, 88, 23))
        self.pbtn_Delete.setObjectName("pbtn_Delete")
        self.pbtn_Modify = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Modify.setGeometry(QtCore.QRect(630, 0, 88, 23))
        self.pbtn_Modify.setObjectName("pbtn_Modify")
        self.pbtn_Run = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Run.setGeometry(QtCore.QRect(450, 0, 88, 23))
        self.pbtn_Run.setObjectName("pbtn_Run")
        self.pbtn_New = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_New.setGeometry(QtCore.QRect(180, 0, 88, 23))
        self.pbtn_New.setObjectName("pbtn_New")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 891, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pbtn_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Quit.setGeometry(QtCore.QRect(810, 320, 88, 23))
        self.pbtn_Quit.setObjectName("pbtn_Quit")
        self.pbtn_Pick = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_Pick.setGeometry(QtCore.QRect(710, 320, 88, 23))
        self.pbtn_Pick.setObjectName("pbtn_Pick")
        popup_Project.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(popup_Project)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 23))
        self.menubar.setObjectName("menubar")
        popup_Project.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(popup_Project)
        self.statusbar.setObjectName("statusbar")
        popup_Project.setStatusBar(self.statusbar)

        self.retranslateUi(popup_Project)
        QtCore.QMetaObject.connectSlotsByName(popup_Project)

    def retranslateUi(self, popup_Project):
        _translate = QtCore.QCoreApplication.translate
        popup_Project.setWindowTitle(_translate("popup_Project", "MainWindow"))
        self.pbtn_Query.setText(_translate("popup_Project", "查询"))
        self.pbtn_Cancel.setText(_translate("popup_Project", "取消"))
        self.pbtn_Save.setText(_translate("popup_Project", "保存"))
        self.pbtn_Update.setText(_translate("popup_Project", "更新"))
        self.pbtn_Delete.setText(_translate("popup_Project", "删除"))
        self.pbtn_Modify.setText(_translate("popup_Project", "修改"))
        self.pbtn_Run.setText(_translate("popup_Project", "执行"))
        self.pbtn_New.setText(_translate("popup_Project", "新建"))
        self.label_2.setText(_translate("popup_Project", "项目清单↓"))
        self.pbtn_Quit.setText(_translate("popup_Project", "退出"))
        self.pbtn_Pick.setText(_translate("popup_Project", "选择"))