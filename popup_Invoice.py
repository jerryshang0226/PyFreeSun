import globalvar
import popup_Pickup_Employee
from PyQt5.QtWidgets import *
from main import *
from dbtool import *
from frm_popup_Invoice import *

class main(QMainWindow, Ui_popup_Invoice):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.popup_employee = popup_Pickup_Employee.main()
        self.pbtn_buyer_Pick.clicked.connect(self.click_popup_Employee_Popup)
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
    popup_win.le_no.setText("")
    popup_win.le_type.setText("")
    popup_win.le_tax.setText("")
    popup_win.le_amount.setText("")
    popup_win.le_buyer.setText("")
    popup_win.le_seller.setText("")
    popup_win.show()

def popup_save(main_window, popup_win):
    billing_dt = popup_win.de_billing_dt.text()
    return_dt = popup_win.de_return_dt.text()
    no = popup_win.le_no.text().strip()
    type = popup_win.le_type.text().strip()
    tax = popup_win.le_tax.text().strip()
    amount = popup_win.le_amount.text().strip()
    PartyA_id = globalvar.pick_employee_id
    PartyB_id = globalvar.pick_employee_id
    PartyA_id = popup_win.le_buyer.text().strip()
    PartyB_id = popup_win.le_seller.text().strip()
    #Comments = popup_win.te_Comments.toPlainText()
    if billing_dt != "" and return_dt != "" and no != "" and type != "" and tax != "" and amount != "" and PartyA_id != "" and PartyB_id != "":
        result = dbExec("INSERT INTO S_INVOICE (Invoice_Date, Return_Date,Invoice_No,Invoice_Type,Amount,Tax_Rate,Exchange,Buyer_id,Seller_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (billing_dt, return_dt, no, type, amount, tax, amount, PartyA_id, PartyB_id))
        #if result > 0:
        #    dbCommit("""DELETE FROM S_GOODS where id not in ( SELECT dt.maxid from (select max(id) maxid from S_GOODS group by Prod_id, Supppiler_id,Brand,Model,Market_DT) dt)""")
    popup_win.close()
    main_window.setEnabled(True)
    main_window.dTabChange(0)

def popup_quit(main_window,popup_win):
    globalvar.pick_suppiler_id = ''
    popup_win.close()
    main_window.setEnabled(True)