import sys
import globalvar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from frm_popup_Account import *
from dbtool import *
from main import *

# 窗口初始化
class main(QMainWindow, Ui_popup_Account):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.query_account()

    def query_account(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['客户Id', '客户名称', '客户行业', '客户规模', '客户省份', '机构代码', '税号', '等级'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 绑定数据
        result = dbQueryFull(
            "select id,Name,Industry,Scale,Place,Business_license_No,Tax_No,Level from S_ACCOUNT where id != 0 and Active_Flg = 'Y'")
        row = len(result)
        vol = self.tableWidget.columnCount()
        self.tableWidget.setRowCount(row)
        for fi in range(row):
            for fj in range(vol):
                data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                self.tableWidget.setItem(fi, fj, data)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def click_pbtn_pick(self):
        row_index = self.tableWidget.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            globalvar.pick_account_id = self.tableWidget.item(row_index, 0).text()
            self.close()
        else:
            QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)

    def click_pbtn_new(self):
        pass

    def click_pbtn_query(self):
        self.pbtn_New.setVisible(False)
        self.pbtn_Query.setVisible(False)
        self.pbtn_Modify.setVisible(False)
        self.pbtn_Delete.setVisible(False)
        self.pbtn_Run.setVisible(True)
        self.pbtn_Cancel.setVisible(True)

def popup_show(main_window,popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.query_account()
    popup_win.show()

def popup_pick(main_window,popup_win):
    globalvar.pick_account_id = ''
    row_index = popup_win.tableWidget.currentIndex().row()
    # 如果有选中记录
    if row_index >= 0:
        globalvar.pick_account_id = popup_win.tableWidget.item(row_index, 0).text()
        popup_win.close()
        main_window.setEnabled(True)
    else:
        QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)

def popup_quit(main_window,popup_win):
    globalvar.pick_account_id = ''
    popup_win.close()
    main_window.setEnabled(True)