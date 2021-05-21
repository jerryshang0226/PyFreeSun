from PyQt5.QtWidgets import *
from main import *
from dbtool import *
from frm_popup_Purchase_Inquiry import *

class main(QMainWindow, Ui_frm_popup_Purchase_Inquiry):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)

def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.le_num.setText("")
    popup_win.le_price.setText("")
    popup_win.le_cycle.setText("")
    popup_win.te_Comments.setText("")
    popup_win.show()

def popup_save(main_window, popup_win):
    from datetime import datetime
    row_index = main_window.tbw_Purchase_Inquiry.currentIndex().row()
    select_id = main_window.tbw_Purchase_Inquiry.item(row_index, 0).text()
    num = popup_win.le_num.text().strip()
    price = popup_win.le_price.text().strip()
    cycle = popup_win.le_cycle.text().strip()
    Comments = popup_win.te_Comments.toPlainText()
    if select_id == "":
        QMessageBox.warning(None, '警告', '请选中产品数据后，再执行相关操作！', QMessageBox.Ok)
    if select_id != "" and num != "" and price != "" and cycle != "":
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = dbExec("INSERT INTO S_GOODS_INQUIRY (`Goods_id`,`Price`,`Cycle`,`Inquiry_dt`,`Nums`,`Comments`) values(%s,%s,%s,%s,%s,%s)",
                    (select_id,int(price)*1000, cycle, dt, num, Comments))
        if result == 1:
            dbCommit(
                "update S_ORDER_ITEM t1 " +
                "INNER JOIN S_GOODS_INQUIRY t2 on t1.inquiry_id = t2.id " +
                "INNER JOIN S_GOODS t3 on t2.goods_id = t3.id " +
                "set t1.Goods_id = t3.id, t1.Prod_id = t3.Prod_id " +
                "where t1.Inquiry_id is not null and (t1.Goods_id is null or t1.Prod_id is null) ")
    popup_win.close()
    main_window.setEnabled(True)
    main_window.mTabChange(3)
    main_window.dTabChange(0)

def popup_quit(main_window,popup_win):
    popup_win.close()
    main_window.setEnabled(True)