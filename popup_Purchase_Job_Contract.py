import popup_Account
from PyQt5.QtWidgets import *
from main import *
from dbtool import *
from frm_popup_Purchase_Job_Contract import *

class main(QMainWindow, Ui_frm_popup_Purchase_Job_Contract):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.popup_Account_PartyA = popup_Account.main()
        self.popup_Account_PartyB = popup_Account.main()
        self.pbtn_PartyA_Pick.clicked.connect(self.click_popup_Account_PartyA)
        self.pbtn_PartyB_Pick.clicked.connect(self.click_popup_Account_PartyB)
        self.popup_Account_PartyA.pbtn_Pick.clicked.connect(self.click_popup_Account_PartyA_Pick)
        self.popup_Account_PartyA.pbtn_Quit.clicked.connect(self.click_popup_Account_PartyA_Quit)
        self.popup_Account_PartyB.pbtn_Pick.clicked.connect(self.click_popup_Account_PartyB_Pick)
        self.popup_Account_PartyB.pbtn_Quit.clicked.connect(self.click_popup_Account_PartyB_Quit)

    def click_popup_Account_PartyA(self):
        globalvar.pick_PjtPartyA = ""
        popup_Account.popup_show(self, self.popup_Account_PartyA)
    def click_popup_Account_PartyB(self):
        globalvar.pick_PjtPartyB = ""
        popup_Account.popup_show(self, self.popup_Account_PartyB)
    def click_popup_Account_PartyA_Pick(self):
        globalvar.pick_PjtPartyA = ''
        popup_Account.popup_pick(self, self.popup_Account_PartyA)
        if globalvar.pick_account_id != '':
            globalvar.pick_PjtPartyA = globalvar.pick_account_id
            result = dbQuery("select Name from S_ACCOUNT where id = %s", globalvar.pick_PjtPartyA)
            self.le_PartyA.setText(str(result[0][0]))
    def click_popup_Account_PartyB_Pick(self):
        globalvar.pick_PjtPartyB = ''
        popup_Account.popup_pick(self, self.popup_Account_PartyB)
        if globalvar.pick_account_id != '':
            globalvar.pick_PjtPartyB = globalvar.pick_account_id
            result = dbQuery("select Name from S_ACCOUNT where id = %s", globalvar.pick_PjtPartyB)
            self.le_PartyB.setText(str(result[0][0]))
    def click_popup_Account_PartyA_Quit(self):
        popup_Suppiler.popup_quit(self, self.popup_Account_PartyA)
    def click_popup_Account_PartyB_Quit(self):
        popup_Suppiler.popup_quit(self, self.popup_Account_PartyB)


def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.le_no.setText("")
    popup_win.le_name.setText("")
    popup_win.le_PartyA.setText("")
    popup_win.le_PartyB.setText("")
    popup_win.le_amount.setText("")
    popup_win.le_status.setText("")
    globalvar.pick_PjtPartyA = ""
    globalvar.pick_PjtPartyB = ""
    globalvar.pick_account_id = ""
    popup_win.show()

def popup_save(main_window, popup_win):
    from datetime import datetime
    row_index = main_window.tbw_Purchase_Job.currentIndex().row()
    select_id = main_window.tbw_Purchase_Job.item(row_index, 0).text()
    no = popup_win.le_no.text().strip()
    name = popup_win.le_name.text().strip()
    amount = popup_win.le_amount.text().strip()
    status = popup_win.le_status.text().strip()
    PartyA_id = globalvar.pick_PjtPartyA
    PartyB_id = globalvar.pick_PjtPartyB
    if select_id == "":
        QMessageBox.warning(None, '警告', '请选中产品数据后，再执行相关操作！', QMessageBox.Ok)
    if select_id != "" and no != "" and name != "" and amount != "" and status != "" and PartyA_id != "" and PartyB_id != "":
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = dbExec("INSERT INTO S_CONTRACT (No,Name,Type,PartyA_id,PartyB_id,Amount,Prchs_id,DT_Active,`Status`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (no, name, '采购合同', PartyA_id, PartyB_id, amount, select_id, dt, status))
    popup_win.close()
    main_window.setEnabled(True)
    main_window.dTabChange(2)

def popup_quit(main_window,popup_win):
    globalvar.pick_suppiler_id = ''
    popup_win.close()
    main_window.setEnabled(True)