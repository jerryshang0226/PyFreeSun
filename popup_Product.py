import sys
import globalvar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from frm_popup_Product import *
from dbtool import *
from main import *

# 窗口初始化
class main(QMainWindow, Ui_popup_Product):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.query_product()

    def query_product(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['产品id', '产品编号','产品大类', '产品小类', '产品名称', '规格型号', '国产/进口','技术标准','计量单位'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 绑定数据
        result = dbQueryFull("SELECT p.`id`,p.`No`,p.TypeA, p.TypeB , p.`Name`, p.Model, p.Origin,p.Standard,p.Unit_Name FROM S_PRODUCT p")
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
        globalvar.pick_product_id = ''
        # 如果有选中记录
        if row_index >= 0:
            globalvar.pick_product_id = self.tableWidget.item(row_index, 0).text()
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
    popup_win.query_product()
    popup_win.show()

def popup_pick(main_window,popup_win):
    globalvar.pick_product_id = ''
    row_index = popup_win.tableWidget.currentIndex().row()
    # 如果有选中记录
    if row_index >= 0:
        globalvar.pick_product_id = popup_win.tableWidget.item(row_index, 0).text()
        popup_win.close()
        main_window.setEnabled(True)
    else:
        QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)

def popup_quit(main_window,popup_win):
    globalvar.pick_account_id = ''
    popup_win.close()
    main_window.setEnabled(True)