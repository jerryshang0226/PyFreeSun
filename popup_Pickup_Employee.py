import sys
import globalvar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from frm_popup_Pickup_Employee import *
from dbtool import *
from main import *

# 窗口初始化
class main(QMainWindow, Ui_popup_Pickup_Employee):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)


    def click_pbtn_new(self):
        pass

    def click_pbtn_query(self):
        self.pbtn_New.setVisible(False)
        self.pbtn_Query.setVisible(False)
        self.pbtn_Modify.setVisible(False)
        self.pbtn_Delete.setVisible(False)
        self.pbtn_Run.setVisible(True)
        self.pbtn_Cancel.setVisible(True)

def query_employee(main_window, popup_win):
    popup_win.tableWidget.setRowCount(0)
    popup_win.tableWidget.setColumnCount(5)
    popup_win.tableWidget.setHorizontalHeaderLabels(['联系人Id', '姓名', '部门', '职位', '手机'])
    popup_win.tableWidget.horizontalHeader().setStretchLastSection(True)
    # 绑定数据
    result = dbQueryFull("""select t1.id, CONCAT(t1.Fst_Name,t1.Lst_Name) "full_name",  '' as "department", '' as "position",  Phone 
                                      from S_CONTACT t1 LEFT JOIN S_ACCOUNT t2 on t1.Account_id = t2.id where t1.Active_Flg = 'Y' and t2.id = 1 """)
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
    query_employee(main_window, popup_win)
    popup_win.show()

def popup_pick(main_window,popup_win):
    globalvar.pick_employee_id = ""
    row_index = popup_win.tableWidget.currentIndex().row()
    # 如果有选中记录
    if row_index >= 0:
        globalvar.pick_employee_id = popup_win.tableWidget.item(row_index, 0).text()
        popup_win.close()
        main_window.setEnabled(True)
    else:
        QMessageBox.warning(None, '警告', '请选中雇员记录后，再执行相关操作！', QMessageBox.Ok)

def popup_quit(main_window,popup_win):
    popup_win.close()
    main_window.setEnabled(True)