import popup_Suppiler
from PyQt5.QtWidgets import *
from main import *
from dbtool import *
from frm_popup_Goods import *

class main(QMainWindow, Ui_frm_popup_Goods):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.popup_suppiler = popup_Suppiler.main()
        self.pbtn_Supppiler_Pick.clicked.connect(self.click_popup_Supppiler_Popup)
        self.popup_suppiler.pbtn_Pick.clicked.connect(self.click_popup_Purchase_Job_Pick)
        self.popup_suppiler.pbtn_Quit.clicked.connect(self.click_popup_Purchase_Job_Quit)

    def click_popup_Supppiler_Popup(self):
        globalvar.pick_suppiler_id = ""
        popup_Suppiler.popup_show(self,self.popup_suppiler)
    def click_popup_Purchase_Job_Pick(self):
        globalvar.pick_suppiler_id = ""
        popup_Suppiler.popup_pick(self,self.popup_suppiler)
        if globalvar.pick_suppiler_id != "" :
            result = dbQuery("select Name from S_ACCOUNT where id = %s", globalvar.pick_suppiler_id)
            self.le_Supppiler.setText(str(result[0][0]))
    def click_popup_Purchase_Job_Quit(self):
        popup_Suppiler.popup_quit(self,self.popup_suppiler)

def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.le_Supppiler.setText("")
    popup_win.le_Brand.setText("")
    popup_win.le_Model.setText("")
    popup_win.le_Price.setText("")
    popup_win.le_Cycle.setText("")
    popup_win.te_Comments.setText("")
    popup_win.show()

def popup_save(main_window, popup_win):
    row_index = main_window.tbw_Product.currentIndex().row()
    select_id = main_window.tbw_Product.item(row_index, 0).text()
    Brand = popup_win.le_Brand.text().strip()
    Model = popup_win.le_Model.text().strip()
    Market_DT = popup_win.dt_Market_DT.text()
    # Price = popup_win.le_Price.text().strip()     #20210508 JerryShang：供应品应不带有价格，其相关记录应储存在供应品报价表中，而且价格往往跟购买数量相关，不是一个定值。
    # Cycle = popup_win.le_Cycle.text().strip()     #20210508 JerryShang：供应品应不带有供货周期，其相关记录应储存在供应品报价表中，而且供货周期往往跟购买数量相关，不是一个定值。
    Comments = popup_win.te_Comments.toPlainText()
    Supppiler = globalvar.pick_suppiler_id
    if select_id == "":
        QMessageBox.warning(None, '警告', '请选中产品数据后，再执行相关操作！', QMessageBox.Ok)
    if select_id != "" and Brand != "" and Model != "" and Market_DT != "" and Supppiler != "":
        result = dbExec("INSERT INTO S_GOODS (Prod_id,Supppiler_id,Brand,Model,Market_DT,Comments) values(%s,%s,%s,%s,%s,%s)",
                    (select_id,Supppiler, Brand, Model, Market_DT, Comments))
        if result > 0:
            dbCommit("""DELETE FROM S_GOODS where id not in ( SELECT dt.maxid from (select max(id) maxid from S_GOODS group by Prod_id, Supppiler_id,Brand,Model,Market_DT) dt)""")
    popup_win.close()
    main_window.setEnabled(True)
    main_window.dTabChange(29)

def popup_quit(main_window,popup_win):
    globalvar.pick_suppiler_id = ''
    popup_win.close()
    main_window.setEnabled(True)