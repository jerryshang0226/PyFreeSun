import popup_Pickup_Goods
from frm_popup_Purchase_Job_Order_Item import *
from PyQt5.QtWidgets import *
from main import *
from dbtool import *

class main(QMainWindow, Ui_popup_Purchase_Job_Order_Item):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.popup_pickup_goods = popup_Pickup_Goods.main()
        self.pbtn_Popup_Goods.clicked.connect(self.click_popup_show)
        self.popup_pickup_goods.pbtn_Pick.clicked.connect(self.click_popup_pick)
        self.popup_pickup_goods.pbtn_Quit.clicked.connect(self.click_popup_quit)

    def click_popup_show(self):
        globalvar.pick_Inquiry_id = ""
        popup_Pickup_Goods.popup_show(self, self.popup_pickup_goods)
    def click_popup_pick(self):
        popup_Pickup_Goods.popup_pick(self, self.popup_pickup_goods)
        if globalvar.pick_Inquiry_id != "":
            result = dbQuery("select t2.id,t3.`Name`,t3.Industry,t3.Scale,t3.Place,t1.Brand,t2.nums,round(t2.Price/1000,4),round((t2.Price/1000)/t2.nums,4),t2.Cycle,t2.Inquiry_dt, t2.comments " +
                "from S_GOODS t1 LEFT JOIN S_GOODS_INQUIRY t2 on t1.id = t2.Goods_id LEFT JOIN S_ACCOUNT t3 on t1.Supppiler_id = t3.id " +
                "where t2.id = %s", globalvar.pick_Inquiry_id)
            self.le_name.setText(str(result[0][1]))
            self.le_nums.setText(str(result[0][6]))
            self.le_sPrice.setText(str(result[0][8]))
    def click_popup_quit(self):
        popup_Pickup_Goods.popup_quit(self, self.popup_pickup_goods)

def popup_show(main_window, popup_win):
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.show()
    popup_win.le_name.setText("")
    popup_win.le_nums.setText("")
    popup_win.le_sPrice.setText("")
    popup_win.te_comments.setText("")

def popup_save(main_window, popup_win):
    from datetime import datetime
    row_index = main_window.tbw_Purchase_Job_Order.currentIndex().row()
    select_id = main_window.tbw_Purchase_Job_Order.item(row_index, 0).text()
    nums = popup_win.le_nums.text().strip()
    Unit = popup_win.le_Unit.text().strip()
    sPrice = popup_win.le_sPrice.text().strip()
    Comments = popup_win.te_comments.toPlainText()
    Inquiry_id = globalvar.pick_Inquiry_id
    if select_id != "" and Inquiry_id != "" and nums != "" and Unit != "" and sPrice != "":
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = dbExec("insert into S_ORDER_ITEM (Ord_id,Inquiry_id,Prod_Num,Unit_Price,Unit_Name,Comments) VALUES (%s,%s,%s,%s,%s,%s)",
                    (select_id, Inquiry_id, nums, sPrice, Unit, Comments))
    popup_win.close()
    main_window.setEnabled(True)
    main_window.dTabChange(0)

def popup_quit(main_window,popup_win):
    globalvar.pick_account_id = ''
    popup_win.close()
    main_window.setEnabled(True)