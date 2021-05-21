import popup_Account
from PyQt5.QtWidgets import *
from main import *
from dbtool import *
from frm_popup_Purchase_Job import *

class main(QMainWindow, Ui_popup_Purchase_Job):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.popup_account = popup_Account.main()
        self.pbtn_Purchase_Job_Pick.clicked.connect(self.click_popup_Purchase_Job_Popup)
        self.popup_account.pbtn_Pick.clicked.connect(self.click_popup_Purchase_Job_Pick)
        self.popup_account.pbtn_Quit.clicked.connect(self.click_popup_Purchase_Job_Quit)

    def click_popup_Purchase_Job_Popup(self):
        globalvar.pick_account_id = ""
        popup_Account.popup_show(self,self.popup_account)
    def click_popup_Purchase_Job_Pick(self):
        globalvar.pick_account_id = ""
        popup_Account.popup_pick(self,self.popup_account)
        if globalvar.pick_account_id != "" :
            result = dbQuery("select Name from S_ACCOUNT where id = %s", globalvar.pick_account_id)
            self.lEdit_Purchase_Job_Supppiler.setText(str(result[0][0]))
    def click_popup_Purchase_Job_Quit(self):
        popup_Account.popup_quit(self,self.popup_project)

def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.show()

def popup_save(main_window, popup_win):
    from datetime import datetime
    Job_No = popup_win.lEdit_Purchase_Job_No.text().strip()
    Status = popup_win.lEdit_Purchase_Job_Status.text().strip()
    Supppiler = globalvar.pick_account_id
    if Job_No != "" and Status != "" and Supppiler != "":
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = dbExec("INSERT INTO S_PURCHASE (No,Name,Status,Create_Time,Type,Supppiler_id) values(%s,'pending',%s,%s,'采购任务',%s)",
                    (Job_No, Status, dt,Supppiler))
    popup_win.close()
    main_window.setEnabled(True)
    main_window.mTabChange(6)

def popup_quit(main_window,popup_win):
    globalvar.pick_account_id = ''
    popup_win.close()
    main_window.setEnabled(True)