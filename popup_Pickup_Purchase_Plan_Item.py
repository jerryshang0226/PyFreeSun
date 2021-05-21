import sys
import globalvar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from frm_popup_Pickup_Purchase_Plan_Item import *
from dbtool import *
from main import *

# 窗口初始化
class main(QMainWindow, Ui_popup_Pickup_Purchase_Plan_Item):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(17)
        self.tableWidget_2.setHorizontalHeaderLabels(['采购项id', '采购模块', '产品名称', '产品型号','技术标准', '供应商名称', '供应商行业', '供应商规模', '商品品牌', '商品型号', '商品上市日期'
                                                        , '商品单价', '供货周期','数量', '计量单位', '询价日期', '备注'])
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.pbtn_Add.clicked.connect(self.click_pbtn_add)
    def click_pbtn_add(self):
        row_index = self.tableWidget.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            row = self.tableWidget_2.rowCount() + 1
            self.tableWidget_2.setRowCount(row)
            vol = self.tableWidget.columnCount()
            for i in range(vol):
                data = QtWidgets.QTableWidgetItem(self.tableWidget.item(row_index, i).text())
                self.tableWidget_2.setItem(row-1, i, data)
            self.tableWidget_2.resizeColumnsToContents()
            self.tableWidget_2.resizeRowsToContents()
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
    popup_win.tableWidget.setRowCount(0)
    popup_win.tableWidget.setColumnCount(17)
    popup_win.tableWidget.setHorizontalHeaderLabels(['采购项id', '采购模块', '产品名称', '产品型号','技术标准', '供应商名称', '供应商行业', '供应商规模', '商品品牌', '商品型号', '商品上市日期'
                                                        , '商品单价', '供货周期','数量', '计量单位', '询价日期', '备注'])
    popup_win.tableWidget.horizontalHeader().setStretchLastSection(True)
    # 绑定数据
    result = dbQueryFull("""SELECT
	itm.id as "itm_id",
	ord.`Name` as "Ord_Name",
	prd.`Name` as "Prod_Name",
	prd.Model as "Prod_Model",
	prd.Standard as "Prod_Standard",
	sp.`Name` as "Sp_Name",
	sp.Industry as "Sp_Industry",
	sp.Scale as "Gd_Scale",
	gd.Brand as "Gd_Brand",
	gd.Model as "Gd_Model",
	gd.Market_DT as "Gd_Market_DT",
	itm.Unit_Price as "Gd_Unit_Price",
	gi.Cycle as "Gd_Cycle",
	itm.Prod_Num as "Itm_Prod_Num",
	itm.Unit_Name as "Itm_Unit_Name",
	gi.Inquiry_dt as "Gd_Inquiry_dt",
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
	AND ord.Project_id = """ + project_id + " order by ord.id, itm.id")
    row = len(result)
    vol = popup_win.tableWidget.columnCount()
    popup_win.tableWidget.setRowCount(row)
    for fi in range(row):
        for fj in range(vol):
            data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
            popup_win.tableWidget.setItem(fi, fj, data)
    popup_win.tableWidget.verticalHeader().setVisible(False)
    popup_win.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    popup_win.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    popup_win.tableWidget.setAlternatingRowColors(True)
    popup_win.tableWidget.resizeColumnsToContents()
    popup_win.tableWidget.resizeRowsToContents()

def popup_show(main_window,popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    query_plan(main_window, popup_win)
    popup_win.show()

def popup_pick(main_window,popup_win):
    from datetime import datetime
    row_index = main_window.tbw_Project.currentIndex().row()
    project_id = main_window.tbw_Project.item(row_index, 0).text()
    adds_count = popup_win.tableWidget_2.rowCount()
    plan_dt = popup_win.dateEdit.text()
    Comments = popup_win.textEdit.toPlainText()
    # 如果有选中记录
    if row_index >= 0 and adds_count > 0 :
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = dbExec(
            "INSERT INTO S_ORDER (Owner_id,Create_Time,Type,Project_id,Name,Status,Plan_dt,Comments) values(%s,%s,%s,%s,%s,%s,%s,%s)",
            ('1', dt, '采购申请单', project_id, dt, 'Pending', plan_dt,Comments))
        if result > 0 :
            result = dbQuery("SELECT id from S_ORDER where Create_Time = %s and Type = '采购申请单' and Project_id = %s", (dt , project_id))
            order_id = str(result[0][0])
            for i in range(adds_count):
                add_id = popup_win.tableWidget_2.item(i, 0).text()
                result = dbExec(
                    "INSERT INTO S_ORDER_ITEM (Ord_id,Prod_id,Goods_id,Inquiry_id,Prod_Num,Unit_Price,Unit_Name,Comments) " +
                    "select %s, Prod_id,Goods_id,Inquiry_id,Prod_Num,Unit_Price,Unit_Name,Comments from S_ORDER_ITEM where id = %s",
                    (order_id, add_id))
        popup_win.close()
        main_window.setEnabled(True)
    else:
        QMessageBox.warning(None, '警告', '请选中供应品报价后，再执行相关操作！', QMessageBox.Ok)

def popup_quit(main_window,popup_win):
    popup_win.close()
    main_window.setEnabled(True)