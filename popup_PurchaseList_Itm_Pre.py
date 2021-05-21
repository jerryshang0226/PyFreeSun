import popup_Product
from frm_popup_PurchaseList_Itm_Pre import *
from PyQt5.QtWidgets import *
from main import *
from dbtool import *
from popup_Product import *

class main(QMainWindow, Ui_frm_popup_PurchaseList_Itm_Pre):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.popup_product = popup_Product.main()
        self.pbtn_popup_PurchaseList_Itm_Pre_pick.clicked.connect(self.click_popup_PurchaseList_Itm_Pre_popup)
        self.popup_product.pbtn_Pick.clicked.connect(self.click_popup_PurchaseList_Itm_Pre_pick)
        self.popup_product.pbtn_Quit.clicked.connect(self.click_popup_PurchaseList_Itm_Pre_quit)

    def click_popup_PurchaseList_Itm_Pre_popup(self):
        popup_Product.popup_show(self,self.popup_product)
    def click_popup_PurchaseList_Itm_Pre_pick(self):
        popup_Product.popup_pick(self,self.popup_product)
        if globalvar.pick_product_id != '' :
            result = dbQuery("select Name from S_PRODUCT where id = %s", globalvar.pick_product_id)
            self.le_popup_PurchaseList_Itm_ProdName.setText(str(result[0][0]))
    def click_popup_PurchaseList_Itm_Pre_quit(self):
        popup_Product.popup_quit(self,self.popup_product)

def popup_show(main_window, popup_win):
    popup_win.le_popup_PurchaseList_Itm_ProdUnit.setEnabled(False)
    popup_win.setFixedSize(popup_win.width(), popup_win.height())
    main_window.setEnabled(False)
    popup_win.setEnabled(True)
    popup_win.le_popup_PurchaseList_Itm_ProdName.setText("")
    popup_win.le_popup_PurchaseList_Itm_ProdNum.setText("")
    popup_win.show()

def popup_save(main_window, popup_win):
    row_index = main_window.tbw_Project_PurchaseList_Pre.currentIndex().row()
    select_id = main_window.tbw_Project_PurchaseList_Pre.item(row_index, 0).text()
    ProdNum = popup_win.le_popup_PurchaseList_Itm_ProdNum.text().strip()
    if globalvar.pick_product_id != "" and ProdNum != "" :
        result = dbExec("INSERT INTO S_ORDER_ITEM (Ord_id,Prod_id,Prod_Num,Comments) values(%s,%s,%s,'')",
                    (select_id, globalvar.pick_product_id, ProdNum))
    popup_win.close()
    main_window.click_tbw_Project_PurchaseList_Pre()
    main_window.setEnabled(True)

def popup_quit(main_window,popup_win):
    globalvar.pick_account_id = ''
    popup_win.close()
    main_window.setEnabled(True)