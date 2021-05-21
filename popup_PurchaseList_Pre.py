from frm_popup_PurchaseList_Pre import *
from PyQt5.QtWidgets import *
from main import *
from dbtool import *

class main(QMainWindow, Ui_frm_popup_PurchaseList_Pre):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)


def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.show()
    popup_win.le_popup_PurchaseList_Name.setText("")
    popup_win.le_popup_PurchaseList_Status.setText("")
    popup_win.le_popup_PurchaseList_Commiter.setText("")
    popup_win.le_popup_PurchaseList_Approver.setText("")

def popup_save(main_window, popup_win):
    from datetime import datetime
    row_index = main_window.tbw_Project.currentIndex().row()
    select_id = main_window.tbw_Project.item(row_index, 0).text()
    PurLst_Name = popup_win.le_popup_PurchaseList_Name.text().strip()
    if PurLst_Name != '':
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = dbExec("insert into S_ORDER (Owner_id,Create_Time,Type,Project_id,  Name, Status) " +
                        "values (1,%s,'采购售前单',%s,%s,'已批准')",
                    (dt, select_id,PurLst_Name))
        if result > 0 :
            dbCommit("""DELETE FROM S_ORDER where id not in ( SELECT dt.maxid from (select max(id) maxid from S_ORDER group by Create_Time, Project_id,`Name`) dt)""")
    popup_win.close()
    main_window.setEnabled(True)

def popup_quit(main_window,popup_win):
    globalvar.pick_account_id = ''
    popup_win.close()
    main_window.setEnabled(True)