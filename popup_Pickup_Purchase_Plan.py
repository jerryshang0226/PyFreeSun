import sys
import globalvar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from frm_popup_Pickup_Purchase_Plan import *
from dbtool import *
from main import *

# 窗口初始化
class main(QMainWindow, Ui_popup_Pickup_Purchase_Plan):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.tbw_Project_PurchaseList_Plan.itemSelectionChanged.connect(self.click_tbw_Project_PurchaseList_Plan)

    def click_tbw_Project_PurchaseList_Plan(self):
        row_index = self.tbw_Project_PurchaseList_Plan.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Project_PurchaseList_Plan.item(row_index, 0).text()
            self.tbw_Project_PurchaseList_Plan_Item.setRowCount(0)
            self.tbw_Project_PurchaseList_Plan_Item.setColumnCount(16)
            self.tbw_Project_PurchaseList_Plan_Item.setHorizontalHeaderLabels( ['采购项id', '产品名称', '规格型号', '技术标准','供应商名称', '行业', '规模', '品牌', '型号', '上市日期', '价格', '供货周期', '数量', '单位', '询价日期', '备注'])
            self.tbw_Project_PurchaseList_Plan_Item.horizontalHeader().setStretchLastSection(True)
            # 绑定数据
            result = dbQueryFull("""SELECT
	itm.id,
	prd.`Name`,
	prd.Model,
	prd.Standard,
	sp.`Name`,
	sp.Industry,
	sp.Scale,
	gd.Brand,
	gd.Model,
	gd.Market_DT,
	itm.Unit_Price/1000,
	gi.Cycle,
	itm.Prod_Num,
	itm.Unit_Name,
	gi.Inquiry_dt,
	itm.Comments 
FROM
	S_ORDER ord
	INNER JOIN S_ORDER_ITEM itm ON ord.id = itm.Ord_id
	LEFT JOIN S_PRODUCT prd ON itm.Prod_id = prd.id
	LEFT JOIN S_GOODS gd ON itm.Goods_id = gd.id
	LEFT JOIN S_ACCOUNT sp ON gd.Supppiler_id = sp.id
	LEFT JOIN S_GOODS_INQUIRY gi ON itm.Inquiry_id = gi.id 
WHERE
	ord.type = '采购计划单' 
	AND ord.id = """ + select_id)
            row = len(result)
            vol = self.tbw_Project_PurchaseList_Plan_Item.columnCount()
            self.tbw_Project_PurchaseList_Plan_Item.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Project_PurchaseList_Plan_Item.setItem(fi, fj, data)
            self.tbw_Project_PurchaseList_Plan_Item.verticalHeader().setVisible(False)
            self.tbw_Project_PurchaseList_Plan_Item.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.tbw_Project_PurchaseList_Plan_Item.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.tbw_Project_PurchaseList_Plan_Item.setAlternatingRowColors(True)
            self.tbw_Project_PurchaseList_Plan_Item.resizeColumnsToContents()
            self.tbw_Project_PurchaseList_Plan_Item.resizeRowsToContents()
            self.tbw_Project_PurchaseList_Plan_Item.setEnabled(False)
    def click_pbtn_pick(self):
        globalvar.pick_Inquiry_id = ""
        row_index = self.tbw_Project_PurchaseList_Plan_Item.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            globalvar.pick_Inquiry_id = self.tbw_Project_PurchaseList_Plan_Item.item(row_index, 0).text()
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

def query_plan(main_window, popup_win):
    row_index = main_window.tbw_Project.currentIndex().row()
    project_id = main_window.tbw_Project.item(row_index, 0).text()
    popup_win.tbw_Project_PurchaseList_Plan.setRowCount(0)
    popup_win.tbw_Project_PurchaseList_Plan.setColumnCount(5)
    popup_win.tbw_Project_PurchaseList_Plan.setHorizontalHeaderLabels(['采购单id', '采购模块', '状态', '提交人', '审核人'])
    popup_win.tbw_Project_PurchaseList_Plan.horizontalHeader().setStretchLastSection(True)
    # 绑定数据
    result = dbQueryFull("""select ord.id, ord. Name, ord. Status, CONCAT(con.Fst_Name, con.Lst_Name),
   CONCAT(apr.Fst_Name, apr.Lst_Name)
from S_ORDER ord
LEFT JOIN S_CONTACT con
on ord.owner_id = con.id
LEFT JOIN S_CONTACT apr
on ord.Approved_id = apr.id
WHERE ord.type = '采购计划单' and ord.Project_id = """ + project_id)
    row = len(result)
    vol = popup_win.tbw_Project_PurchaseList_Plan.columnCount()
    popup_win.tbw_Project_PurchaseList_Plan.setRowCount(row)
    for fi in range(row):
        for fj in range(vol):
            data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
            popup_win.tbw_Project_PurchaseList_Plan.setItem(fi, fj, data)
    popup_win.tbw_Project_PurchaseList_Plan.verticalHeader().setVisible(False)
    popup_win.tbw_Project_PurchaseList_Plan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    popup_win.tbw_Project_PurchaseList_Plan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    popup_win.tbw_Project_PurchaseList_Plan.setAlternatingRowColors(True)
    popup_win.tbw_Project_PurchaseList_Plan.resizeColumnsToContents()
    popup_win.tbw_Project_PurchaseList_Plan.resizeRowsToContents()

def popup_show(main_window,popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    query_plan(main_window, popup_win)
    popup_win.show()

def popup_pick(main_window,popup_win):
    globalvar.pick_Inquiry_id = ""
    row_index = popup_win.tbw_Project_PurchaseList_Plan_Item.currentIndex().row()
    # 如果有选中记录
    if row_index >= 0:
        globalvar.pick_Inquiry_id = popup_win.tbw_Project_PurchaseList_Plan_Item.item(row_index, 0).text()
        popup_win.close()
        main_window.setEnabled(True)
    else:
        QMessageBox.warning(None, '警告', '请选中供应品报价后，再执行相关操作！', QMessageBox.Ok)

def popup_quit(main_window,popup_win):
    popup_win.close()
    main_window.setEnabled(True)