import sys
import globalvar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from frm_popup_Pickup_Goods import *
from dbtool import *
from main import *

# 窗口初始化
class main(QMainWindow, Ui_popup_Pickup_Goods):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.query_goods()
        self.tableWidget.itemSelectionChanged.connect(self.click_tableWidget)

    def click_tableWidget(self):
        row_index = self.tableWidget.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tableWidget.item(row_index, 0).text()
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.setColumnCount(12)
            self.tableWidget_2.setHorizontalHeaderLabels( ['询价id','供应商名称', '行业', '规模', '省份', '品牌', '数量', '价格', '单价', '供货周期', '询价日期', '备注'])
            self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
            # 绑定数据
            result = dbQueryFull(
                "select t2.id,t3.`Name`,t3.Industry,t3.Scale,t3.Place,t1.Brand,t2.nums,round(t2.Price/1000,4),round((t2.Price/t2.nums)/1000,4),t2.Cycle,t2.Inquiry_dt, t2.comments " +
                "from S_GOODS t1 LEFT JOIN S_GOODS_INQUIRY t2 on t1.id = t2.Goods_id LEFT JOIN S_ACCOUNT t3 on t1.Supppiler_id = t3.id " +
                "where t1.id = " + select_id)
            row = len(result)
            vol = self.tableWidget_2.columnCount()
            self.tableWidget_2.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tableWidget_2.setItem(fi, fj, data)
            self.tableWidget_2.verticalHeader().setVisible(False)
            self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.tableWidget_2.setAlternatingRowColors(True)
            self.tableWidget_2.resizeColumnsToContents()
            self.tableWidget_2.resizeRowsToContents()

    def query_goods(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['供应品id', '供应商名称', '行业', '规模', '品牌', '型号', '上市日期'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 绑定数据
        result = dbQueryFull("select t1.id,t2.`Name`,t2.Industry,t2.Scale,t1.Brand,t1.Model,t1.Market_DT " +
                             "from S_GOODS t1 LEFT JOIN S_ACCOUNT t2 on t1.Supppiler_id = t2.id")
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
        globalvar.pick_Inquiry_id = ""
        row_index = self.tableWidget_2.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            globalvar.pick_Inquiry_id = self.tableWidget_2.item(row_index, 0).text()
            self.close()
        else:
            QMessageBox.warning(None, '警告', '请选中供应品报价后，再执行相关操作！', QMessageBox.Ok)

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
    popup_win.query_goods()
    popup_win.show()

def popup_pick(main_window,popup_win):
    globalvar.pick_Inquiry_id = ""
    row_index = popup_win.tableWidget_2.currentIndex().row()
    # 如果有选中记录
    if row_index >= 0:
        globalvar.pick_Inquiry_id = popup_win.tableWidget_2.item(row_index, 0).text()
        popup_win.close()
        main_window.setEnabled(True)
    else:
        QMessageBox.warning(None, '警告', '请选中供应品报价后，再执行相关操作！', QMessageBox.Ok)

def popup_quit(main_window,popup_win):
    popup_win.close()
    main_window.setEnabled(True)