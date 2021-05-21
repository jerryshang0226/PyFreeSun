import popup_Suppiler
from PyQt5.QtWidgets import *
from main import *
from dbtool import *
from frm_popup_M_Pay_Invc import *

class main(QMainWindow, Ui_popup_M_Pay_Invc):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)

    def query_payment(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['订单id', '订单名称', '采购合同编号', '供应商', '采购合同总额', '订单金额', '回票总额'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 绑定数据
        result = dbQueryFull(
            "SELECT t1.id,t1.Pay_Date,t1.Reason,t1.Amount,t1.dep_id,t1.Emp_id,t1.Pay_Type,t1.Note_Code FROM `S_PAYMENT` t1 " +
            "where t1.Uncollected > 0 ")
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
def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.query_payment()
    popup_win.show()

def popup_save(main_window, popup_win):
    row_index_invc = main_window.tbw_Purchase_Payment.currentIndex().row()
    Invc_id = main_window.tbw_Purchase_Payment.item(row_index_invc, 0).text()
    row_index_pay = popup_win.tableWidget.currentIndex().row()
    Pay_id = popup_win.tableWidget.item(row_index_pay, 0).text()
    if Invc_id == "" or Pay_id == "":
        QMessageBox.warning(None, '警告', '请选中产品数据后，再执行相关操作！', QMessageBox.Ok)
    if Invc_id != "" and Pay_id != "":
        result = dbExec("INSERT INTO S_M_PYMNT_INVC (Pay_id,Invc_id) values(%s,%s)",
                    (Pay_id,Invc_id))
        if result > 0:
            result1 = dbQuery("select Uncollected from S_PAYMENT where id = %s ", Pay_id)
            result2 = dbQuery("select Exchange from S_INVOICE where id = %s ", Invc_id)
            pay_num = str(result1[0][0])
            invc_num = str(result2[0][0])
            if int(pay_num) >= int(invc_num):
                dbExec("update S_INVOICE set Exchange = 0 where id = %s", (Invc_id))
                dbExec("update S_PAYMENT set Uncollected = Uncollected - %s where id = %s", (invc_num, Pay_id))
            else:
                dbExec("update S_INVOICE set Exchange = Exchange - %s where id = %s", (pay_num, Invc_id))
                dbExec("update S_PAYMENT set Uncollected = 0 where id = %s", (Pay_id))
    popup_win.close()
    main_window.setEnabled(True)
    main_window.dTabChange(0)

def popup_quit(main_window,popup_win):
    globalvar.pick_suppiler_id = ''
    popup_win.close()
    main_window.setEnabled(True)