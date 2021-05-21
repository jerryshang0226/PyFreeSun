import globalvar
import popup_Pickup_Employee
from PyQt5.QtWidgets import *
from main import *
from dbtool import *
from frm_popup_Payment import *

class main(QMainWindow, Ui_popup_Payment):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.popup_employee = popup_Pickup_Employee.main()
        self.pbtn_Employee_Pick.clicked.connect(self.click_popup_Employee_Popup)
        self.popup_employee.pbtn_Pick.clicked.connect(self.click_popup_Employee_Pick)
        self.popup_employee.pbtn_Cancel.clicked.connect(self.click_popup_Employee_Quit)

    def click_popup_Employee_Popup(self):
        globalvar.pick_employee_id = ""
        popup_Pickup_Employee.popup_show(self, self.popup_employee)
    def click_popup_Employee_Pick(self):
        globalvar.pick_employee_id = ""
        popup_Pickup_Employee.popup_pick(self, self.popup_employee)
        if globalvar.pick_employee_id != "" :
            result = dbQuery("select CONCAT(t1.Fst_Name,t1.Lst_Name) from S_CONTACT t1 where id = %s", globalvar.pick_employee_id)
            self.le_employee.setText(str(result[0][0]))
    def click_popup_Employee_Quit(self):
        popup_Pickup_Employee.popup_quit(self, self.popup_employee)

def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.le_amount.setText("")
    popup_win.le_department.setText("")
    popup_win.le_employee.setText("")
    popup_win.le_type.setText("")
    popup_win.le_note_no.setText("")
    popup_win.le_reason.setText("")
    popup_win.show()

def popup_save(main_window, popup_win):
    row_index = main_window.tbw_Project_Cost_Purchase.currentIndex().row()
    select_id = main_window.tbw_Project_Cost_Purchase.item(row_index, 0).text()
    Payment_DT = popup_win.dateEdit.text()
    Amount = popup_win.le_amount.text().strip()
    Employee_id = globalvar.pick_employee_id
    Type = popup_win.le_type.text().strip()
    Note_no = popup_win.le_note_no.text().strip()
    Reason = popup_win.le_reason.text().strip()
    #Comments = popup_win.te_Comments.toPlainText()
    if select_id == "":
        QMessageBox.warning(None, '警告', '请选中产品数据后，再执行相关操作！', QMessageBox.Ok)
    if select_id != "" and Payment_DT != "" and Amount != "" and Employee_id != "" and Type != "" and Note_no != "":
        result = dbExec("INSERT INTO S_PAYMENT (Pay_date, Amount,Dep_id,Emp_id,Reason,Pay_Type,Note_Code,Pay_Status,Uncollected,Pay_Target,Ord_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (Payment_DT, Amount, 0, Employee_id, Reason, Type, Note_no, '待付款', Amount, 0, select_id))
        if result > 0:
            dbCommit("""DELETE FROM S_GOODS where id not in ( SELECT dt.maxid from (select max(id) maxid from S_GOODS group by Prod_id, Supppiler_id,Brand,Model,Market_DT) dt)""")
    popup_win.close()
    main_window.setEnabled(True)
    main_window.dTabChange(29)

def popup_quit(main_window,popup_win):
    globalvar.pick_suppiler_id = ''
    popup_win.close()
    main_window.setEnabled(True)