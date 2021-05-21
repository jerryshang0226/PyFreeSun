import sys
import globalvar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from frm_popup_Project import *
from dbtool import *
from main import *

# 窗口初始化
class main(QMainWindow, Ui_popup_Project):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.query_product()

    def query_product(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setHorizontalHeaderLabels(
            ['项目id', '项目编号', '项目名称', '甲方', '乙方', '业务负责人', '项目经理', '合同款', '保证金', '采购预算费用', '采购发生比例',
             '工程预算费用', '工程发生比例', '业务费用', '毛利润', '毛利率'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 绑定数据
        result = dbQueryFull("""SELECT t1.id,  t1.ProjectNo as "No", t1. Name, t2. Name as "PartyAname",
                 t3. Name as "PartyBname", CONCAT(bln.Fst_Name, bln.Lst_Name) as "BL",
                 CONCAT(pmn.Fst_Name, pmn.Lst_Name) as "PM", tc.Amount,
                 '' as "baozheng", '' as "caigouyusuan", '' as "caigoufasheng",
                 '' as "gongchengyusuan", '' as "gongchengfasheng",
                 '' as "yewufeiyong", '' as "maolirun", '' as "maolilv"
            FROM S_PROJECT t1
            LEFT JOIN S_ACCOUNT t2
              on t1.PartyA_id = t2.id
            LEFT JOIN S_ACCOUNT t3
              on t1.PartyB_id = t3.id
            LEFT JOIN S_PROJECT_EMP pm
              on t1.id = pm.Project_id
             and pm.Type = 'PM'
             and pm. Status = 'Y'
            LEFT JOIN S_CONTACT pmn
              on pm.Emp_id = pmn.id
            LEFT JOIN S_PROJECT_EMP bl
              on t1.id = bl.Project_id
             and bl.Type = 'BL'
             and bl. Status = 'Y'
            LEFT JOIN S_CONTACT bln
              on bl.Emp_id = bln.id
            LEFT JOIN S_CONTRACT tc
              on t1.id = tc.Project_id and tc.Type = '实施合同'""")
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
    popup_win.show()

def popup_pick(main_window,popup_win):
    globalvar.pick_project_id = ''
    row_index = popup_win.tableWidget.currentIndex().row()
    # 如果有选中记录
    if row_index >= 0:
        globalvar.pick_project_id = popup_win.tableWidget.item(row_index, 0).text()
        popup_win.close()
        main_window.setEnabled(True)
    else:
        QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)

def popup_quit(main_window,popup_win):
    globalvar.pick_account_id = ''
    popup_win.close()
    main_window.setEnabled(True)