import popup_Project
from frm_popup_Purchase_Job_Order import *
from PyQt5.QtWidgets import *
from main import *
from dbtool import *

class main(QMainWindow, Ui_popup_Purchase_Job_Order):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.popup_project = popup_Project.main()
        self.pbtn_Popup.clicked.connect(self.click_popup_show)
        self.popup_project.pbtn_Pick.clicked.connect(self.click_popup_pick)
        self.popup_project.pbtn_Quit.clicked.connect(self.click_popup_quit)

    def click_popup_show(self):
        popup_Project.popup_show(self, self.popup_project)
    def click_popup_pick(self):
        popup_Project.popup_pick(self, self.popup_project)
        if globalvar.pick_project_id != "" :
            result = dbQuery("select Name from S_PROJECT where id = %s", globalvar.pick_project_id)
            self.lEdit_Pjt.setText(str(result[0][0]))
    def click_popup_quit(self):
        popup_Project.popup_quit(self, self.popup_project)

def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.show()
    popup_win.lEdit_Name.setText("")
    popup_win.lEdit_Pjt.setText("")

def popup_save(main_window, popup_win):
    from datetime import datetime
    row_index = main_window.tbw_Purchase_Job.currentIndex().row()
    select_id = main_window.tbw_Purchase_Job.item(row_index, 0).text()
    Job_Name = popup_win.lEdit_Name.text().strip()
    Pjt_id = globalvar.pick_project_id
    if select_id != "" and Job_Name != "" and Pjt_id != "":
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = dbExec("INSERT INTO S_ORDER (`Owner_id`,`Create_Time`,`Type`,`Project_id`,`Name`,`Status`,`Approved_id`,`Prchs_id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    ('1', dt, '采购购买单', Pjt_id, Job_Name, '新建', '1',select_id))
    popup_win.close()
    main_window.setEnabled(True)
    main_window.dTabChange(0)

def popup_quit(main_window,popup_win):
    globalvar.pick_account_id = ''
    popup_win.close()
    main_window.setEnabled(True)