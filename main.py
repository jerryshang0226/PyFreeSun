import sys
import globalvar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import main_log

import popup_Account
import popup_Goods
import popup_PurchaseList_Pre
import popup_PurchaseList_Itm_Pre
import popup_Purchase_Job
import popup_Purchase_Job_Order
import popup_Purchase_Job_Order_Item
import popup_Suppiler
import popup_Purchase_Inquiry
import popup_Purchase_Job_Contract
import popup_Pickup_Purchase_Plan
import popup_Pickup_Purchase_Plan_Item
import popup_Payment
import popup_Invoice
import popup_M_Pay_Invc

from frm_main_window import *
from dbtool import *
from popup_Account import *
from frm_popup_PurchaseList_Pre import *
from frm_popup_PurchaseList_Itm_Pre import *

# 窗口初始化
class main(QMainWindow, Ui_MainWin):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        # 初始化popup窗口
        self.popup_account = popup_Account.main()
        self.popup_account_projectA = popup_Account.main()
        self.popup_account_projectB = popup_Account.main()
        self.popup_purchaselist_pre = popup_PurchaseList_Pre.main()
        self.popup_purchaseList_itm_pre = popup_PurchaseList_Itm_Pre.main()
        self.popup_purchase_job = popup_Purchase_Job.main()
        self.popup_purchase_job_order = popup_Purchase_Job_Order.main()
        self.popup_purchase_job_order_item = popup_Purchase_Job_Order_Item.main()
        self.popup_goods = popup_Goods.main()
        self.popup_purchase_inquiry = popup_Purchase_Inquiry.main()
        self.popup_purchase_job_contract = popup_Purchase_Job_Contract.main()
        self.popup_pickup_purchase_plan = popup_Pickup_Purchase_Plan.main()
        self.popup_pickup_purchase_plan_item = popup_Pickup_Purchase_Plan_Item.main()
        self.popup_payment = popup_Payment.main()
        self.popup_invoice = popup_Invoice.main()
        self.popup_m_pay_invc = popup_M_Pay_Invc.main()
        # 绑定信号
        self.Tab_Main.currentChanged.connect(self.mTabChange)
        self.Tab_Detail.currentChanged.connect(self.dTabChange)
        self.tbw_Account.itemSelectionChanged.connect(self.click_tbw_Account)
        self.pbtnCreateAccount.clicked.connect(self.click_pbtn_CreateAccount)
        self.pbtnModifyAccount.clicked.connect(self.click_pbtn_ModifyAccount)
        self.pbtnDeleteAccount.clicked.connect(self.click_pbtn_DeleteAccount)
        self.pbtnQueryAccount.clicked.connect(self.click_pbtn_QueryAccount)
        self.tbw_Contact.itemSelectionChanged.connect(self.click_tbw_Contact)
        self.tbw_Project.itemSelectionChanged.connect(self.click_tbw_Project)
        self.tbw_Project_PurchaseList_Pre.itemSelectionChanged.connect(self.click_tbw_Project_PurchaseList_Pre)
        self.tbw_Project_PurchaseList_Plan.itemSelectionChanged.connect(self.click_tbw_Project_PurchaseList_Plan)
        self.tbw_Product.itemSelectionChanged.connect(self.click_tbw_Product)
        self.tbw_Supppiler.itemSelectionChanged.connect(self.click_tbw_Supppiler)
        self.tbw_Purchase_Job.itemSelectionChanged.connect(self.click_tbw_Purchase_Job)
        self.tbw_Purchase_Inquiry.itemSelectionChanged.connect(self.click_tbw_Purchase_Inquiry)
        self.tbw_Purchase_Plan.itemSelectionChanged.connect(self.click_tbw_Purchase_Plan)
        self.tbw_Purchase_Notice.itemSelectionChanged.connect(self.click_tbw_Purchase_Notice)
        self.tbw_Project_Cost_Purchase.itemSelectionChanged.connect(self.click_tbw_Project_Cost_Purchase)
        self.tbw_Purchase_Payment.itemSelectionChanged.connect(self.click_tbw_Purchase_Payment)
        # self.tbw_Account.itemClicked.connect(self.click_tbw_Account)
        self.mTabChange(0)
        # self.dTabChange(0)

    # 客户排版：客户相关：详情
    def dTabAccount(self):
        self.Dtab_Account = QtWidgets.QWidget()
        self.Dtab_Account.setObjectName("Dtab_Account")
        self.label = QtWidgets.QLabel(self.Dtab_Account)
        self.label.setGeometry(QtCore.QRect(60, 120, 71, 16))
        self.label.setObjectName("label")
        self.lEdit_Acnt_Type = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_Type.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.lEdit_Acnt_Type.setObjectName("lEdit_Acnt_Type")
        self.label_2 = QtWidgets.QLabel(self.Dtab_Account)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Dtab_Account)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 61, 16))
        self.label_3.setObjectName("label_3")
        self.lEdit_Acnt_Total = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_Total.setGeometry(QtCore.QRect(140, 220, 113, 20))
        self.lEdit_Acnt_Total.setObjectName("lEdit_Acnt_Total")
        self.lEdit_Acnt_unReturn = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_unReturn.setGeometry(QtCore.QRect(140, 280, 113, 20))
        self.lEdit_Acnt_unReturn.setObjectName("lEdit_Acnt_unReturn")
        self.lEdit_Acnt_OrgCode = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_OrgCode.setGeometry(QtCore.QRect(470, 170, 113, 20))
        self.lEdit_Acnt_OrgCode.setObjectName("lEdit_Acnt_OrgCode")
        self.lEdit_Acnt_Return = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_Return.setGeometry(QtCore.QRect(470, 220, 113, 20))
        self.lEdit_Acnt_Return.setObjectName("lEdit_Acnt_Return")
        self.label_4 = QtWidgets.QLabel(self.Dtab_Account)
        self.label_4.setGeometry(QtCore.QRect(350, 170, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Dtab_Account)
        self.label_5.setGeometry(QtCore.QRect(350, 220, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_Account_Name = QtWidgets.QLabel(self.Dtab_Account)
        self.label_Account_Name.setGeometry(QtCore.QRect(60, 70, 61, 16))
        self.label_Account_Name.setObjectName("label_Account_Name")
        self.lEdit_Account_Name = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Account_Name.setGeometry(QtCore.QRect(140, 70, 441, 21))
        self.lEdit_Account_Name.setObjectName("lEdit_Account_Name")
        self.pbtnQueryAccount = QtWidgets.QPushButton(self.Dtab_Account)
        self.pbtnQueryAccount.setGeometry(QtCore.QRect(790, 10, 88, 23))
        self.pbtnQueryAccount.setObjectName("pbtnQueryAccount")
        self.pbtnCreateAccount = QtWidgets.QPushButton(self.Dtab_Account)
        self.pbtnCreateAccount.setGeometry(QtCore.QRect(610, 10, 88, 23))
        self.pbtnCreateAccount.setObjectName("pbtnCreateAccount")
        self.pbtnModifyAccount = QtWidgets.QPushButton(self.Dtab_Account)
        self.pbtnModifyAccount.setGeometry(QtCore.QRect(1060, 10, 88, 23))
        self.pbtnModifyAccount.setObjectName("pbtnModifyAccount")
        self.pbtnQueryRunAccount = QtWidgets.QPushButton(self.Dtab_Account)
        self.pbtnQueryRunAccount.setGeometry(QtCore.QRect(880, 10, 88, 23))
        self.pbtnQueryRunAccount.setObjectName("pbtnQueryRunAccount")
        self.pbtnCancelAccount = QtWidgets.QPushButton(self.Dtab_Account)
        self.pbtnCancelAccount.setGeometry(QtCore.QRect(970, 10, 88, 23))
        self.pbtnCancelAccount.setObjectName("pbtnCancelAccount")
        self.pbtnDeleteAccount = QtWidgets.QPushButton(self.Dtab_Account)
        self.pbtnDeleteAccount.setGeometry(QtCore.QRect(1240, 10, 88, 23))
        self.pbtnDeleteAccount.setObjectName("pbtnDeleteAccount")
        self.pbtnCommitAccount = QtWidgets.QPushButton(self.Dtab_Account)
        self.pbtnCommitAccount.setGeometry(QtCore.QRect(700, 10, 88, 23))
        self.pbtnCommitAccount.setObjectName("pbtnCommitAccount")
        self.pbtnCommitModifyAccount = QtWidgets.QPushButton(self.Dtab_Account)
        self.pbtnCommitModifyAccount.setGeometry(QtCore.QRect(1150, 10, 88, 23))
        self.pbtnCommitModifyAccount.setObjectName("pbtnCommitModifyAccount")
        self.lEdit_Acnt_tax = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_tax.setGeometry(QtCore.QRect(140, 170, 113, 20))
        self.lEdit_Acnt_tax.setObjectName("lEdit_Acnt_tax")
        self.lb_account_tax = QtWidgets.QLabel(self.Dtab_Account)
        self.lb_account_tax.setGeometry(QtCore.QRect(30, 170, 91, 21))
        self.lb_account_tax.setObjectName("lb_account_tax")
        self.lb_Acnt_Industry = QtWidgets.QLabel(self.Dtab_Account)
        self.lb_Acnt_Industry.setGeometry(QtCore.QRect(380, 120, 61, 21))
        self.lb_Acnt_Industry.setObjectName("lb_Acnt_Industry")
        self.lEdit_Acnt_Industry = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_Industry.setGeometry(QtCore.QRect(470, 120, 113, 20))
        self.lEdit_Acnt_Industry.setObjectName("lEdit_Acnt_Industry")
        self.lb_Acnt_Scale = QtWidgets.QLabel(self.Dtab_Account)
        self.lb_Acnt_Scale.setGeometry(QtCore.QRect(630, 170, 61, 21))
        self.lb_Acnt_Scale.setObjectName("lb_Acnt_Scale")
        self.lEdit_Acnt_Scale = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_Scale.setGeometry(QtCore.QRect(720, 170, 113, 20))
        self.lEdit_Acnt_Scale.setObjectName("lEdit_Acnt_Scale")
        self.lb_Acnt_Place = QtWidgets.QLabel(self.Dtab_Account)
        self.lb_Acnt_Place.setGeometry(QtCore.QRect(630, 120, 61, 21))
        self.lb_Acnt_Place.setObjectName("lb_Acnt_Place")
        self.lEdit_Acnt_Place = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_Place.setGeometry(QtCore.QRect(720, 120, 113, 20))
        self.lEdit_Acnt_Place.setObjectName("lEdit_Acnt_Place")
        self.lEdit_Acnt_unReturnPst = QtWidgets.QLineEdit(self.Dtab_Account)
        self.lEdit_Acnt_unReturnPst.setGeometry(QtCore.QRect(470, 280, 113, 20))
        self.lEdit_Acnt_unReturnPst.setObjectName("lEdit_Acnt_unReturnPst")
        self.label_34 = QtWidgets.QLabel(self.Dtab_Account)
        self.label_34.setGeometry(QtCore.QRect(350, 280, 91, 16))
        self.label_34.setObjectName("label_34")
        self.label.setText("客户类型")
        self.label_2.setText("合同总额")
        self.label_3.setText("未回款金额")
        self.label_4.setText("统一信用编码")
        self.label_5.setText("回款金额")
        self.label_Account_Name.setText("客户名称")
        self.pbtnQueryAccount.setText("查询")
        self.pbtnCreateAccount.setText("新建")
        self.pbtnModifyAccount.setText("修改")
        self.pbtnQueryRunAccount.setText("执行")
        self.pbtnCancelAccount.setText("取消")
        self.pbtnDeleteAccount.setText("删除")
        self.pbtnCommitAccount.setText("保存")
        self.pbtnCommitModifyAccount.setText("更新")
        self.lb_account_tax.setText("纳税人识别号")
        self.lb_Acnt_Industry.setText("行业")
        self.lb_Acnt_Scale.setText("规模")
        self.lb_Acnt_Place.setText("省份")
        self.label_34.setText("未回款比例")
        self.pbtnCommitAccount.setEnabled(False)
        self.pbtnQueryRunAccount.setEnabled(False)
        self.pbtnCancelAccount.setEnabled(False)
        self.pbtnCommitModifyAccount.setEnabled(False)
        self.lEdit_Account_Name.setEnabled(False)
        self.lEdit_Acnt_Type.setEnabled(False)
        self.lEdit_Acnt_Total.setEnabled(False)
        self.lEdit_Acnt_unReturn.setEnabled(False)
        self.lEdit_Acnt_OrgCode.setEnabled(False)
        self.lEdit_Acnt_Return.setEnabled(False)
        self.lEdit_Acnt_unReturnPst.setEnabled(False)
        self.lEdit_Acnt_tax.setEnabled(False)
        self.lEdit_Acnt_Industry.setEnabled(False)
        self.lEdit_Acnt_Scale.setEnabled(False)
        self.lEdit_Acnt_Place.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Account, "客户详情")
        self.pbtnCreateAccount.clicked.connect(self.click_pbtn_CreateAccount)
        self.pbtnModifyAccount.clicked.connect(self.click_pbtn_ModifyAccount)
        self.pbtnDeleteAccount.clicked.connect(self.click_pbtn_DeleteAccount)
        self.pbtnQueryAccount.clicked.connect(self.click_pbtn_QueryAccount)
        self.pbtnQueryRunAccount.clicked.connect(self.click_pbtn_QueryRunAccount)
        self.pbtnCommitAccount.clicked.connect(self.click_pbtn_CommitAccount)
        self.pbtnCancelAccount.clicked.connect(self.click_pbtn_CancelAccount)
        self.pbtnCommitModifyAccount.clicked.connect(self.click_pbtn_ModifyCommitAccount)
    # 客户排版：项目
    def dTabAccountProject(self):
        self.Dtab_Account_Project = QtWidgets.QWidget()
        self.Dtab_Account_Project.setObjectName("Dtab_Account_Project")
        self.tbw_Account_Project = QtWidgets.QTableWidget(self.Dtab_Account_Project)
        self.tbw_Account_Project.setGeometry(QtCore.QRect(0, 10, 1331, 331))
        self.tbw_Account_Project.setObjectName("tbw_Account_Project")
        self.tbw_Account_Project.setColumnCount(0)
        self.tbw_Account_Project.setRowCount(0)
        self.Tab_Detail.addTab(self.Dtab_Account_Project, "客户项目")
        self.tbw_Account_Project.setRowCount(0)
        self.tbw_Account_Project.setColumnCount(7)
        self.tbw_Account_Project.setHorizontalHeaderLabels(['项目Id', '项目名称', '项目经理', '项目合同编号', '业务负责人', '项目阶段', '项目地点'])
        self.tbw_Account_Project.horizontalHeader().setStretchLastSection(True)
        self.tbw_Account_Project.verticalHeader().setVisible(False)
        self.tbw_Account_Project.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Account_Project.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Account_Project.setAlternatingRowColors(True)
        self.tbw_Account_Project.resizeColumnsToContents()
        self.tbw_Account_Project.resizeRowsToContents()
    # 客户排版：合同
    def dTabAccountContract(self):
        self.Dtab_Account_Contract = QtWidgets.QWidget()
        self.Dtab_Account_Contract.setObjectName("Dtab_Account_Contract")
        self.tbw_Account_Contract = QtWidgets.QTableWidget(self.Dtab_Account_Contract)
        self.tbw_Account_Contract.setGeometry(QtCore.QRect(0, 10, 1331, 331))
        self.tbw_Account_Contract.setObjectName("tbw_Account_Contract")
        self.tbw_Account_Contract.setColumnCount(0)
        self.tbw_Account_Contract.setRowCount(0)
        self.Tab_Detail.addTab(self.Dtab_Account_Contract, "客户合同")
        self.tbw_Account_Contract.setRowCount(0)
        self.tbw_Account_Contract.setColumnCount(6)
        self.tbw_Account_Contract.setHorizontalHeaderLabels(['合同Id', '合同编号', '合同名称', '甲方客户', '乙方客户', '合同金额'])
        self.tbw_Account_Contract.horizontalHeader().setStretchLastSection(True)
        self.tbw_Account_Contract.verticalHeader().setVisible(False)
        self.tbw_Account_Contract.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Account_Contract.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Account_Contract.setAlternatingRowColors(True)
        self.tbw_Account_Contract.resizeColumnsToContents()
        self.tbw_Account_Contract.resizeRowsToContents()
    # 客户排版：联系人
    def dTabAccountContact(self):
        self.Dtab_Account_Contact = QtWidgets.QWidget()
        self.Dtab_Account_Contact.setObjectName("Dtab_Account_Contact")
        self.tbw_Account_Contact = QtWidgets.QTableWidget(self.Dtab_Account_Contact)
        self.tbw_Account_Contact.setGeometry(QtCore.QRect(0, 0, 1351, 341))
        self.tbw_Account_Contact.setObjectName("tbw_Account_Contact")
        self.tbw_Account_Contact.setColumnCount(0)
        self.tbw_Account_Contact.setRowCount(0)
        self.Tab_Detail.addTab(self.Dtab_Account_Contact, "客户联系人")
        self.tbw_Account_Contact.setRowCount(0)
        self.tbw_Account_Contact.setColumnCount(8)
        self.tbw_Account_Contact.setHorizontalHeaderLabels(['联系人Id', '姓名', '部门', '职位', '支持度', '年龄', '手机', '电子邮件'])
        self.tbw_Account_Contact.horizontalHeader().setStretchLastSection(True)
        self.tbw_Account_Contact.verticalHeader().setVisible(False)
        self.tbw_Account_Contact.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Account_Contact.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Account_Contact.setAlternatingRowColors(True)
        self.tbw_Account_Contact.resizeColumnsToContents()
        self.tbw_Account_Contact.resizeRowsToContents()
    # 客户排版：主页
    def mTabAccount(self):
        self.dTabAccount()
        self.dTabAccountProject()
        self.dTabAccountContract()
        self.dTabAccountContact()
        self.tbw_Account.setRowCount(0)
        self.tbw_Account.setColumnCount(8)
        self.tbw_Account.setHorizontalHeaderLabels(['客户Id', '客户名称', '客户行业', '客户规模', '客户省份', '机构代码', '税号', '等级'])
        self.tbw_Account.horizontalHeader().setStretchLastSection(True)
    # 客户排版：主页格式
    def mTabAccountFormat(self):
        self.tbw_Account.verticalHeader().setVisible(False)
        self.tbw_Account.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Account.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Account.setAlternatingRowColors(True)
        self.tbw_Account.resizeColumnsToContents()
        self.tbw_Account.resizeRowsToContents()

    # 联系人排版：详情
    def dTabContact(self):
        self.Dtab_Contact = QtWidgets.QWidget()
        self.Dtab_Contact.setObjectName("Dtab_Contact")
        self.lEdit_Cnt_Org = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Org.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lEdit_Cnt_Org.setObjectName("lEdit_Cnt_Org")
        self.lEdit_Cnt_Dept = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Dept.setGeometry(QtCore.QRect(130, 100, 113, 20))
        self.lEdit_Cnt_Dept.setObjectName("lEdit_Cnt_Dept")
        self.lEdit_Cnt_Rank = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Rank.setGeometry(QtCore.QRect(130, 140, 113, 20))
        self.lEdit_Cnt_Rank.setObjectName("lEdit_Cnt_Rank")
        self.lEdit_Cnt_BirtyDay = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_BirtyDay.setGeometry(QtCore.QRect(130, 180, 113, 20))
        self.lEdit_Cnt_BirtyDay.setObjectName("lEdit_Cnt_BirtyDay")
        self.lEdit_Cnt_Phone = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Phone.setGeometry(QtCore.QRect(130, 220, 113, 20))
        self.lEdit_Cnt_Phone.setObjectName("lEdit_Cnt_Phone")
        self.lEdit_Cnt_Address = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Address.setGeometry(QtCore.QRect(130, 260, 113, 20))
        self.lEdit_Cnt_Address.setObjectName("lEdit_Cnt_Address")
        self.lEdit_Cnt_FstName = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_FstName.setGeometry(QtCore.QRect(440, 60, 113, 20))
        self.lEdit_Cnt_FstName.setObjectName("lEdit_Cnt_FstName")
        self.lEdit_Cnt_Postion = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Postion.setGeometry(QtCore.QRect(440, 150, 113, 20))
        self.lEdit_Cnt_Postion.setObjectName("lEdit_Cnt_Postion")
        self.lEdit_Cnt_Sex = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Sex.setGeometry(QtCore.QRect(440, 190, 113, 20))
        self.lEdit_Cnt_Sex.setObjectName("lEdit_Cnt_Sex")
        self.lEdit_Cnt_Character = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Character.setGeometry(QtCore.QRect(440, 230, 113, 20))
        self.lEdit_Cnt_Character.setObjectName("lEdit_Cnt_Character")
        self.lEdit_Cnt_Email = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_Email.setGeometry(QtCore.QRect(440, 270, 113, 20))
        self.lEdit_Cnt_Email.setObjectName("lEdit_Cnt_Email")
        self.label_7 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_7.setGeometry(QtCore.QRect(50, 60, 61, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_8.setGeometry(QtCore.QRect(50, 100, 54, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_9.setGeometry(QtCore.QRect(50, 140, 51, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_10.setGeometry(QtCore.QRect(50, 180, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_11.setGeometry(QtCore.QRect(50, 220, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_12.setGeometry(QtCore.QRect(50, 270, 61, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_13.setGeometry(QtCore.QRect(360, 60, 54, 12))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_14.setGeometry(QtCore.QRect(360, 150, 54, 12))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_15.setGeometry(QtCore.QRect(360, 190, 54, 12))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_16.setGeometry(QtCore.QRect(360, 230, 54, 12))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_17.setGeometry(QtCore.QRect(360, 270, 54, 12))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Dtab_Contact)
        self.label_18.setGeometry(QtCore.QRect(360, 100, 54, 12))
        self.label_18.setObjectName("label_18")
        self.lEdit_Cnt_LstName = QtWidgets.QLineEdit(self.Dtab_Contact)
        self.lEdit_Cnt_LstName.setGeometry(QtCore.QRect(440, 100, 113, 20))
        self.lEdit_Cnt_LstName.setObjectName("lEdit_Cnt_LstName")
        self.pbtn_PopUP_Account = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtn_PopUP_Account.setGeometry(QtCore.QRect(250, 60, 21, 21))
        self.pbtn_PopUP_Account.setObjectName("pbtn_PopUP_Account")
        self.pbtnQueryContact = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtnQueryContact.setGeometry(QtCore.QRect(790, 10, 88, 23))
        self.pbtnQueryContact.setObjectName("pbtnQueryContact")
        self.pbtnCreateContact = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtnCreateContact.setGeometry(QtCore.QRect(610, 10, 88, 23))
        self.pbtnCreateContact.setObjectName("pbtnCreateContact")
        self.pbtnModifyContact = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtnModifyContact.setGeometry(QtCore.QRect(1060, 10, 88, 23))
        self.pbtnModifyContact.setObjectName("pbtnModifyContact")
        self.pbtnQueryRunContact = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtnQueryRunContact.setGeometry(QtCore.QRect(880, 10, 88, 23))
        self.pbtnQueryRunContact.setObjectName("pbtnQueryRunContact")
        self.pbtnCancelContact = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtnCancelContact.setGeometry(QtCore.QRect(970, 10, 88, 23))
        self.pbtnCancelContact.setObjectName("pbtnCancelContact")
        self.pbtnDeleteContact = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtnDeleteContact.setGeometry(QtCore.QRect(1240, 10, 88, 23))
        self.pbtnDeleteContact.setObjectName("pbtnDeleteContact")
        self.pbtnCommitContact = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtnCommitContact.setGeometry(QtCore.QRect(700, 10, 88, 23))
        self.pbtnCommitContact.setObjectName("pbtnCommitContact")
        self.pbtnModifyCommitContact = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtnModifyCommitContact.setGeometry(QtCore.QRect(1150, 10, 88, 23))
        self.pbtnModifyCommitContact.setObjectName("pbtnModifyCommitContact")
        self.pbtn_PopUP_Account = QtWidgets.QPushButton(self.Dtab_Contact)
        self.pbtn_PopUP_Account.setGeometry(QtCore.QRect(250, 60, 21, 21))
        self.pbtn_PopUP_Account.setObjectName("pbtn_PopUP_Account")
        self.label_7.setText("所属组织")
        self.label_8.setText("部门")
        self.label_9.setText("职级")
        self.label_10.setText("出生日期")
        self.label_11.setText("手机号码")
        self.label_12.setText("通讯地址")
        self.label_13.setText("姓氏")
        self.label_14.setText("职位")
        self.label_15.setText("性别")
        self.label_16.setText("性格")
        self.label_17.setText("邮箱")
        self.label_18.setText("名字")
        self.pbtn_PopUP_Account.setText("☺")
        self.pbtnQueryContact.setText("查询")
        self.pbtnCreateContact.setText("新建")
        self.pbtnModifyContact.setText("修改")
        self.pbtnQueryRunContact.setText("执行")
        self.pbtnCancelContact.setText("取消")
        self.pbtnDeleteContact.setText("删除")
        self.pbtnCommitContact.setText("保存")
        self.pbtnModifyCommitContact.setText("更新")
        self.pbtn_PopUP_Account.setEnabled(False)
        self.pbtnQueryRunContact.setEnabled(False)
        self.pbtnCancelContact.setEnabled(False)
        self.pbtnCommitContact.setEnabled(False)
        self.pbtnModifyCommitContact.setEnabled(False)
        self.lEdit_Cnt_Phone.setEnabled(False)
        self.lEdit_Cnt_Org.setEnabled(False)
        self.lEdit_Cnt_Dept.setEnabled(False)
        self.lEdit_Cnt_Rank.setEnabled(False)
        self.lEdit_Cnt_BirtyDay.setEnabled(False)
        self.lEdit_Cnt_Address.setEnabled(False)
        self.lEdit_Cnt_FstName.setEnabled(False)
        self.lEdit_Cnt_LstName.setEnabled(False)
        self.lEdit_Cnt_Postion.setEnabled(False)
        self.lEdit_Cnt_Sex.setEnabled(False)
        self.lEdit_Cnt_Character.setEnabled(False)
        self.lEdit_Cnt_Email.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Contact, "联系人详情")
        self.pbtnCreateContact.clicked.connect(self.click_pbtn_CreateContact)
        self.pbtnModifyContact.clicked.connect(self.click_pbtn_ModifyContact)
        self.pbtnDeleteContact.clicked.connect(self.click_pbtn_DeleteContact)
        self.pbtnQueryContact.clicked.connect(self.click_pbtn_QueryContact)
        self.pbtnQueryRunContact.clicked.connect(self.click_pbtn_QueryRunContact)
        self.pbtnCommitContact.clicked.connect(self.click_pbtn_CommitContact)
        self.pbtnCancelContact.clicked.connect(self.click_pbtn_CancelContact)
        self.pbtnModifyCommitContact.clicked.connect(self.click_pbtn_ModifyCommitContact)
        self.pbtn_PopUP_Account.clicked.connect(self.click_pbtn_PopUpAccount)
        # 绑定popup窗口
        self.popup_account.pbtn_Pick.clicked.connect(self.popup_account_click_pbtn_pick)
        self.popup_account.pbtn_Quit.clicked.connect(self.popup_account_click_pbtn_quit)
    # 联系人排版：地址
    def dTabContactAddress(self):
        self.Dtab_Contact_Address = QtWidgets.QWidget()
        self.Dtab_Contact_Address.setObjectName("Dtab_Contact_Address")
        self.tbw_Contact_Address = QtWidgets.QTableWidget(self.Dtab_Contact_Address)
        self.tbw_Contact_Address.setGeometry(QtCore.QRect(10, 10, 1341, 341))
        self.tbw_Contact_Address.setObjectName("tbw_Contact_Address")
        self.tbw_Contact_Address.setRowCount(0)
        self.tbw_Contact_Address.setRowCount(0)
        self.tbw_Contact_Address.setColumnCount(8)
        self.tbw_Contact_Address.setHorizontalHeaderLabels(['地址Id', '手机号码', '固定电话', '电子邮件', '通信地址', '收件人', '优先级', '备注'])
        self.tbw_Contact_Address.horizontalHeader().setStretchLastSection(True)
        self.tbw_Contact_Address.verticalHeader().setVisible(False)
        self.tbw_Contact_Address.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Contact_Address.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Contact_Address.setAlternatingRowColors(True)
        self.tbw_Contact_Address.resizeColumnsToContents()
        self.tbw_Contact_Address.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Contact_Address, "联系人通讯地址")
    # 联系人排版：项目
    def dTabContactProject(self):
        self.Dtab_Contact_Project = QtWidgets.QWidget()
        self.Dtab_Contact_Project.setObjectName("Dtab_Contact_Project")
        self.tbw_Contact_Project = QtWidgets.QTableWidget(self.Dtab_Contact_Project)
        self.tbw_Contact_Project.setGeometry(QtCore.QRect(0, 10, 1351, 341))
        self.tbw_Contact_Project.setObjectName("tbw_Contact_Project")
        self.tbw_Contact_Project.setRowCount(0)
        self.tbw_Contact_Project.setColumnCount(7)
        self.tbw_Contact_Project.setHorizontalHeaderLabels(['项目Id', '项目名称', '项目经理', '项目合同编号', '业务负责人', '项目阶段', '联系人角色'])
        self.tbw_Contact_Project.horizontalHeader().setStretchLastSection(True)
        self.tbw_Contact_Project.verticalHeader().setVisible(False)
        self.tbw_Contact_Project.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Contact_Project.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Contact_Project.setAlternatingRowColors(True)
        self.tbw_Contact_Project.resizeColumnsToContents()
        self.tbw_Contact_Project.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Contact_Project, "联系人项目")
    # 联系人排版：组织
    def dTabContactOrg(self):
        self.Dtab_Contact_Org = QtWidgets.QWidget()
        self.Dtab_Contact_Org.setObjectName("Dtab_Contact_Org")
        self.tbw_Contact_Org = QtWidgets.QTableWidget(self.Dtab_Contact_Org)
        self.tbw_Contact_Org.setGeometry(QtCore.QRect(10, 10, 1331, 331))
        self.tbw_Contact_Org.setObjectName("tbw_Contact_Org")
        self.tbw_Contact_Org.setRowCount(0)
        self.tbw_Contact_Org.setColumnCount(8)
        self.tbw_Contact_Org.setHorizontalHeaderLabels(['组织Id', '组织类型', '组织名称', '组织行业', '组织规模', '客户省份', '客户类型', '角色类型'])
        self.tbw_Contact_Org.horizontalHeader().setStretchLastSection(True)
        self.tbw_Contact_Org.verticalHeader().setVisible(False)
        self.tbw_Contact_Org.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Contact_Org.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Contact_Org.setAlternatingRowColors(True)
        self.tbw_Contact_Org.resizeColumnsToContents()
        self.tbw_Contact_Org.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Contact_Org, "联系人组织")
    # 联系人排版：主页
    def mTabContact(self):
        self.dTabContact()
        self.dTabContactProject()
        self.dTabContactAddress()
        self.dTabContactOrg()
        self.tbw_Contact.setRowCount(0)
        self.tbw_Contact.setColumnCount(8)
        self.tbw_Contact.setHorizontalHeaderLabels(['联系人Id', '所属组织', '姓名', '部门', '职位', '支持度', '年龄', '手机', '电子邮件'])
        self.tbw_Contact.horizontalHeader().setStretchLastSection(True)
    # 联系人排版：主页格式
    def mTabContactFormat(self):
        self.tbw_Contact.verticalHeader().setVisible(False)
        self.tbw_Contact.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Contact.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Contact.setAlternatingRowColors(True)
        self.tbw_Contact.resizeColumnsToContents()
        self.tbw_Contact.resizeRowsToContents()

    # 项目排版：详细页签（项目详情）
    def dTabProject(self):
        self.Dtab_Project = QtWidgets.QWidget()
        self.Dtab_Project.setObjectName("Dtab_Project")
        self.label_19 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_19.setGeometry(QtCore.QRect(60, 60, 120, 15))
        self.label_19.setObjectName("label_19")
        self.label_19.setText("项目编号：")
        self.label_20 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_20.setGeometry(QtCore.QRect(70, 100, 120, 15))
        self.label_20.setObjectName("label_20")
        self.label_20.setText("甲方")
        self.label_21 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_21.setGeometry(QtCore.QRect(50, 170, 120, 15))
        self.label_21.setObjectName("label_21")
        self.label_21.setText("合同额")
        self.label_22 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_22.setGeometry(QtCore.QRect(60, 130, 120, 15))
        self.label_22.setObjectName("label_22")
        self.label_22.setText("业务负责人")
        self.label_23 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_23.setGeometry(QtCore.QRect(620, 50, 120, 15))
        self.label_23.setObjectName("label_23")
        self.label_23.setText("采购预算费用")
        self.label_24 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_24.setGeometry(QtCore.QRect(620, 90, 120, 15))
        self.label_24.setObjectName("label_24")
        self.label_24.setText("工程预算费用")
        self.label_25 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_25.setGeometry(QtCore.QRect(360, 60, 120, 15))
        self.label_25.setObjectName("label_25")
        self.label_25.setText("项目名称")
        self.label_26 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_26.setGeometry(QtCore.QRect(360, 130, 120, 15))
        self.label_26.setObjectName("label_26")
        self.label_26.setText("项目经理")
        self.label_27 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_27.setGeometry(QtCore.QRect(360, 100, 120, 15))
        self.label_27.setObjectName("label_27")
        self.label_27.setText("乙方")
        self.label_28 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_28.setGeometry(QtCore.QRect(890, 50, 120, 15))
        self.label_28.setObjectName("label_28")
        self.label_28.setText("采购发生金额")
        self.label_29 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_29.setGeometry(QtCore.QRect(360, 160, 120, 15))
        self.label_29.setObjectName("label_29")
        self.label_29.setText("未付款比例")
        self.label_30 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_30.setGeometry(QtCore.QRect(620, 120, 120, 15))
        self.label_30.setObjectName("label_30")
        self.label_30.setText("业务预算费用")
        self.label_31 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_31.setGeometry(QtCore.QRect(620, 160, 120, 15))
        self.label_31.setObjectName("label_31")
        self.label_31.setText("其他预算费用")
        self.label_32 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_32.setGeometry(QtCore.QRect(620, 200, 120, 15))
        self.label_32.setObjectName("label_32")
        self.label_32.setText("预估毛利润")
        self.label_33 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_33.setGeometry(QtCore.QRect(620, 240, 120, 15))
        self.label_33.setObjectName("label_33")
        self.label_33.setText("预估毛利率")
        self.label_67 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_67.setGeometry(QtCore.QRect(890, 80, 120, 15))
        self.label_67.setObjectName("label_67")
        self.label_67.setText("工程发生金额")
        self.label_68 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_68.setGeometry(QtCore.QRect(890, 120, 120, 15))
        self.label_68.setObjectName("label_68")
        self.label_68.setText("业务发生金额")
        self.label_69 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_69.setGeometry(QtCore.QRect(890, 190, 120, 15))
        self.label_69.setObjectName("label_69")
        self.label_69.setText("实际毛利润")
        self.label_70 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_70.setGeometry(QtCore.QRect(890, 150, 120, 15))
        self.label_70.setObjectName("label_70")
        self.label_70.setText("其他发生金额")
        self.label_71 = QtWidgets.QLabel(self.Dtab_Project)
        self.label_71.setGeometry(QtCore.QRect(890, 230, 120, 15))
        self.label_71.setObjectName("label_71")
        self.label_71.setText("实际毛利率")
        self.lEdit_Project_No = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_No.setGeometry(QtCore.QRect(170, 60, 113, 20))
        self.lEdit_Project_No.setObjectName("lEdit_Project_No")
        self.lEdit_Project_PartyA = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_PartyA.setGeometry(QtCore.QRect(170, 100, 113, 20))
        self.lEdit_Project_PartyA.setObjectName("lEdit_Project_PartyA")
        self.lEdit_Project_BL = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_BL.setGeometry(QtCore.QRect(170, 140, 113, 20))
        self.lEdit_Project_BL.setObjectName("lEdit_Project_BL")
        self.lEdit_Project_Amount = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Amount.setGeometry(QtCore.QRect(170, 180, 113, 20))
        self.lEdit_Project_Amount.setObjectName("lEdit_Project_Amount")
        self.lEdit_Project_Name = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Name.setGeometry(QtCore.QRect(460, 60, 113, 20))
        self.lEdit_Project_Name.setObjectName("lEdit_Project_Name")
        self.lEdit_Project_PartyB = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_PartyB.setGeometry(QtCore.QRect(460, 100, 113, 20))
        self.lEdit_Project_PartyB.setObjectName("lEdit_Project_PartyB")
        self.lEdit_Project_PM = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_PM.setGeometry(QtCore.QRect(460, 130, 113, 20))
        self.lEdit_Project_PM.setObjectName("lEdit_Project_PM")
        self.lEdit_Project_UnPayPrc = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_UnPayPrc.setGeometry(QtCore.QRect(460, 160, 113, 20))
        self.lEdit_Project_UnPayPrc.setObjectName("lEdit_Project_UnPayPrc")
        self.lEdit_Project_Purchase_Est = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Purchase_Est.setGeometry(QtCore.QRect(730, 50, 113, 20))
        self.lEdit_Project_Purchase_Est.setObjectName("lEdit_Project_Purchase_Est")
        self.lEdit_Project_Const_Est = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Const_Est.setGeometry(QtCore.QRect(730, 90, 113, 20))
        self.lEdit_Project_Const_Est.setObjectName("lEdit_Project_Const_Est")
        self.lEdit_Project_Bsns_Est = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Bsns_Est.setGeometry(QtCore.QRect(730, 130, 113, 20))
        self.lEdit_Project_Bsns_Est.setObjectName("lEdit_Project_Bsns_Est")
        self.lEdit_Project_Oth_Est = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Oth_Est.setGeometry(QtCore.QRect(730, 170, 113, 20))
        self.lEdit_Project_Oth_Est.setObjectName("lEdit_Project_Oth_Est")
        self.lEdit_Project_GP_Est = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_GP_Est.setGeometry(QtCore.QRect(730, 200, 113, 20))
        self.lEdit_Project_GP_Est.setObjectName("lEdit_Project_GP_Est")
        self.lEdit_Project_GPct_Est = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_GPct_Est.setGeometry(QtCore.QRect(730, 240, 113, 20))
        self.lEdit_Project_GPct_Est.setObjectName("lEdit_Project_GPct_Est")
        self.lEdit_Project_Purchase_Done = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Purchase_Done.setGeometry(QtCore.QRect(1010, 50, 113, 20))
        self.lEdit_Project_Purchase_Done.setObjectName("lEdit_Project_Purchase_Done")
        self.lEdit_Project_Const_Done = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Const_Done.setGeometry(QtCore.QRect(1010, 80, 113, 20))
        self.lEdit_Project_Const_Done.setObjectName("lEdit_Project_Const_Done")
        self.lEdit_Project_Bsns_Done = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Bsns_Done.setGeometry(QtCore.QRect(1010, 120, 113, 20))
        self.lEdit_Project_Bsns_Done.setObjectName("lEdit_Project_Bsns_Done")
        self.lEdit_Project_Oth_Done = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_Oth_Done.setGeometry(QtCore.QRect(1010, 150, 113, 20))
        self.lEdit_Project_Oth_Done.setObjectName("lEdit_Project_Oth_Done")
        self.lEdit_Project_GP_Done = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_GP_Done.setGeometry(QtCore.QRect(1010, 190, 113, 20))
        self.lEdit_Project_GP_Done.setObjectName("lEdit_Project_GP_Done")
        self.lEdit_Project_GPct_Done = QtWidgets.QLineEdit(self.Dtab_Project)
        self.lEdit_Project_GPct_Done.setGeometry(QtCore.QRect(1010, 230, 113, 20))
        self.lEdit_Project_GPct_Done.setObjectName("lEdit_Project_GPct_Done")
        self.lEdit_Project_No.setEnabled(False)
        self.lEdit_Project_PartyA.setEnabled(False)
        self.lEdit_Project_BL.setEnabled(False)
        self.lEdit_Project_Amount.setEnabled(False)
        self.lEdit_Project_Name.setEnabled(False)
        self.lEdit_Project_PartyB.setEnabled(False)
        self.lEdit_Project_PM.setEnabled(False)
        self.lEdit_Project_UnPayPrc.setEnabled(False)
        self.lEdit_Project_Purchase_Est.setEnabled(False)
        self.lEdit_Project_Const_Est.setEnabled(False)
        self.lEdit_Project_Bsns_Est.setEnabled(False)
        self.lEdit_Project_Oth_Est.setEnabled(False)
        self.lEdit_Project_GP_Est.setEnabled(False)
        self.lEdit_Project_GPct_Est.setEnabled(False)
        self.lEdit_Project_Purchase_Done.setEnabled(False)
        self.lEdit_Project_Const_Done.setEnabled(False)
        self.lEdit_Project_Bsns_Done.setEnabled(False)
        self.lEdit_Project_Oth_Done.setEnabled(False)
        self.lEdit_Project_GP_Done.setEnabled(False)
        self.lEdit_Project_GPct_Done.setEnabled(False)
        self.pbtnQueryProject = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtnQueryProject.setGeometry(QtCore.QRect(790, 10, 88, 23))
        self.pbtnQueryProject.setObjectName("pbtnQueryProject")
        self.pbtnNewProject = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtnNewProject.setGeometry(QtCore.QRect(610, 10, 88, 23))
        self.pbtnNewProject.setObjectName("pbtnNewProject")
        self.pbtnModifyProject = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtnModifyProject.setGeometry(QtCore.QRect(1060, 10, 88, 23))
        self.pbtnModifyProject.setObjectName("pbtnModifyProject")
        self.pbtnRunProject = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtnRunProject.setGeometry(QtCore.QRect(880, 10, 88, 23))
        self.pbtnRunProject.setObjectName("pbtnRunProject")
        self.pbtnCancelProject = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtnCancelProject.setGeometry(QtCore.QRect(970, 10, 88, 23))
        self.pbtnCancelProject.setObjectName("pbtnCancelProject")
        self.pbtnDeleteProject = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtnDeleteProject.setGeometry(QtCore.QRect(1240, 10, 88, 23))
        self.pbtnDeleteProject.setObjectName("pbtnDeleteProject")
        self.pbtnCommitProject = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtnCommitProject.setGeometry(QtCore.QRect(700, 10, 88, 23))
        self.pbtnCommitProject.setObjectName("pbtnCommitProject")
        self.pbtnUpdateProject = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtnUpdateProject.setGeometry(QtCore.QRect(1150, 10, 88, 23))
        self.pbtnUpdateProject.setObjectName("pbtnUpdateProject")
        self.pbtn_PopUP_PjtPartyA = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtn_PopUP_PjtPartyA.setGeometry(QtCore.QRect(290, 100, 21, 21))
        self.pbtn_PopUP_PjtPartyA.setObjectName("pbtn_PopUP_PjtPartyA")
        self.pbtn_PopUP_PjtPartyA.setText("☺")
        self.pbtn_PopUP_PjtPartyB = QtWidgets.QPushButton(self.Dtab_Project)
        self.pbtn_PopUP_PjtPartyB.setGeometry(QtCore.QRect(580, 100, 21, 21))
        self.pbtn_PopUP_PjtPartyB.setObjectName("pbtn_PopUP_PjtPartyB")
        self.pbtn_PopUP_PjtPartyB.setText("☺")
        self.pbtn_PopUP_PjtPartyA.setEnabled(False)
        self.pbtn_PopUP_PjtPartyB.setEnabled(False)
        self.pbtnQueryProject.setText("查询")
        self.pbtnNewProject.setText("新建")
        self.pbtnModifyProject.setText("修改")
        self.pbtnRunProject.setText("执行")
        self.pbtnCancelProject.setText("取消")
        self.pbtnDeleteProject.setText("删除")
        self.pbtnCommitProject.setText("保存")
        self.pbtnUpdateProject.setText("更新")
        self.pbtnRunProject.setEnabled(False)
        self.pbtnCancelProject.setEnabled(False)
        self.pbtnCommitProject.setEnabled(False)
        self.pbtnUpdateProject.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Project, "项目详单")
        self.pbtnNewProject.clicked.connect(self.click_pbtn_CreateProject)
        self.pbtnCancelProject.clicked.connect(self.click_pbtn_CancelProject)
        self.pbtnCommitProject.clicked.connect(self.click_pbtn_CommitProject)
        self.pbtnModifyProject.clicked.connect(self.click_pbtn_ModifyProject)
        self.pbtnUpdateProject.clicked.connect(self.click_pbtn_UpdateProject)
        self.pbtn_PopUP_PjtPartyA.clicked.connect(self.click_pbtn_PopUpPartyA)
        self.pbtn_PopUP_PjtPartyB.clicked.connect(self.click_pbtn_PopUpPartyB)
        # 绑定popup窗口
        self.popup_account_projectA.pbtn_Pick.clicked.connect(self.popup_project_click_pbtn_pickA)
        self.popup_account_projectA.pbtn_Quit.clicked.connect(self.popup_project_click_pbtn_quit)
        self.popup_account_projectB.pbtn_Pick.clicked.connect(self.popup_project_click_pbtn_pickB)
        self.popup_account_projectB.pbtn_Quit.clicked.connect(self.popup_project_click_pbtn_quit)
    # 项目排版：详细页签（项目采购售前单）
    def dTabProjectPurchaseListPre(self):
        self.Dtab_Project_PurchaseList_Pre = QtWidgets.QWidget()
        self.Dtab_Project_PurchaseList_Pre.setObjectName("Dtab_Project_PurchaseList_Pre")
        self.tbw_Project_PurchaseList_Pre = QtWidgets.QTableWidget(self.Dtab_Project_PurchaseList_Pre)
        self.tbw_Project_PurchaseList_Pre.setGeometry(QtCore.QRect(10, 50, 1311, 171))
        self.tbw_Project_PurchaseList_Pre.setObjectName("tbw_Project_PurchaseList_Pre")
        self.tbw_Project_PurchaseList_Pre.setRowCount(0)
        self.tbw_Project_PurchaseList_Pre.setColumnCount(5)
        self.tbw_Project_PurchaseList_Pre.setHorizontalHeaderLabels(['采购单id', '采购模块', '状态', '提交人', '审核人'])
        self.tbw_Project_PurchaseList_Pre.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_PurchaseList_Pre.verticalHeader().setVisible(False)
        self.tbw_Project_PurchaseList_Pre.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_PurchaseList_Pre.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_PurchaseList_Pre.setAlternatingRowColors(True)
        self.tbw_Project_PurchaseList_Pre.resizeColumnsToContents()
        self.tbw_Project_PurchaseList_Pre.resizeRowsToContents()
        self.tbw_Project_PurchaseList_Pre_Item = QtWidgets.QTableWidget(self.Dtab_Project_PurchaseList_Pre)
        self.tbw_Project_PurchaseList_Pre_Item.setGeometry(QtCore.QRect(10, 260, 1311, 161))
        self.tbw_Project_PurchaseList_Pre_Item.setObjectName("tbw_Project_PurchaseList_Pre_Item")
        self.tbw_Project_PurchaseList_Pre_Item.setRowCount(0)
        self.tbw_Project_PurchaseList_Pre_Item.setColumnCount(7)
        self.tbw_Project_PurchaseList_Pre_Item.setHorizontalHeaderLabels(
            ['采购项id', '产品名称', '规格型号', '技术标准', '数量', '单位', '备注'])
        self.tbw_Project_PurchaseList_Pre_Item.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_PurchaseList_Pre_Item.verticalHeader().setVisible(False)
        self.tbw_Project_PurchaseList_Pre_Item.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_PurchaseList_Pre_Item.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_PurchaseList_Pre_Item.setAlternatingRowColors(True)
        self.tbw_Project_PurchaseList_Pre_Item.resizeColumnsToContents()
        self.tbw_Project_PurchaseList_Pre_Item.resizeRowsToContents()
        self.label_72 = QtWidgets.QLabel(self.Dtab_Project_PurchaseList_Pre)
        self.label_72.setGeometry(QtCore.QRect(10, 230, 111, 16))
        self.label_72.setObjectName("label_72")
        self.label_72.setText("采购项清单内容↓")
        self.label_121 = QtWidgets.QLabel(self.Dtab_Project_PurchaseList_Pre)
        self.label_121.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_121.setObjectName("label_121")
        self.label_121.setText("采购项清单↓")
        self.pbtn_PurchaseList_Pre_Run = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Run.setGeometry(QtCore.QRect(870, 20, 88, 23))
        self.pbtn_PurchaseList_Pre_Run.setObjectName("pbtn_PurchaseList_Pre_Run")
        self.pbtn_PurchaseList_Pre_Query = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Query.setGeometry(QtCore.QRect(780, 20, 88, 23))
        self.pbtn_PurchaseList_Pre_Query.setObjectName("pbtn_PurchaseList_Pre_Query")
        self.pbtn_PurchaseList_Pre_New = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_New.setGeometry(QtCore.QRect(600, 20, 88, 23))
        self.pbtn_PurchaseList_Pre_New.setObjectName("pbtn_PurchaseList_Pre_New")
        self.pbtn_PurchaseList_Pre_Delete = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Delete.setGeometry(QtCore.QRect(1230, 20, 88, 23))
        self.pbtn_PurchaseList_Pre_Delete.setObjectName("pbtn_PurchaseList_Pre_Delete")
        self.pbtn_PurchaseList_Pre_Modify = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Modify.setGeometry(QtCore.QRect(1050, 20, 88, 23))
        self.pbtn_PurchaseList_Pre_Modify.setObjectName("pbtn_PurchaseList_Pre_Modify")
        self.pbtn_PurchaseList_Pre_Cancel = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Cancel.setGeometry(QtCore.QRect(960, 20, 88, 23))
        self.pbtn_PurchaseList_Pre_Cancel.setObjectName("pbtn_PurchaseList_Pre_Cancel")
        self.pbtn_PurchaseList_Pre_Itm_Delete = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Itm_Delete.setGeometry(QtCore.QRect(1230, 230, 88, 23))
        self.pbtn_PurchaseList_Pre_Itm_Delete.setObjectName("pbtn_PurchaseList_Pre_Itm_Delete")
        self.pbtn_PurchaseList_Pre_Itm_Cancel = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Itm_Cancel.setGeometry(QtCore.QRect(960, 230, 88, 23))
        self.pbtn_PurchaseList_Pre_Itm_Cancel.setObjectName("pbtn_PurchaseList_Pre_Itm_Cancel")
        self.pbtn_PurchaseList_Pre_Itm_New = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Itm_New.setGeometry(QtCore.QRect(600, 230, 88, 23))
        self.pbtn_PurchaseList_Pre_Itm_New.setObjectName("pbtn_PurchaseList_Pre_Itm_New")
        self.pbtn_PurchaseList_Pre_Itm_Query = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Itm_Query.setGeometry(QtCore.QRect(780, 230, 88, 23))
        self.pbtn_PurchaseList_Pre_Itm_Query.setObjectName("pbtn_PurchaseList_Pre_Itm_Query")
        self.pbtn_PurchaseList_Pre_Itm_Run = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Itm_Run.setGeometry(QtCore.QRect(870, 230, 88, 23))
        self.pbtn_PurchaseList_Pre_Itm_Run.setObjectName("pbtn_PurchaseList_Pre_Itm_Run")
        self.pbtn_PurchaseList_Pre_Itm_Modify = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Itm_Modify.setGeometry(QtCore.QRect(1050, 230, 88, 23))
        self.pbtn_PurchaseList_Pre_Itm_Modify.setObjectName("pbtn_PurchaseList_Pre_Itm_Modify")
        self.pbtn_PurchaseList_Pre_Update = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Update.setGeometry(QtCore.QRect(1140, 20, 88, 23))
        self.pbtn_PurchaseList_Pre_Update.setObjectName("pbtn_PurchaseList_Pre_Update")
        self.pbtn_PurchaseList_Pre_Save = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Save.setGeometry(QtCore.QRect(690, 20, 88, 23))
        self.pbtn_PurchaseList_Pre_Save.setObjectName("pbtn_PurchaseList_Pre_Save")
        self.pbtn_PurchaseList_Pre_Itm_Save = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Itm_Save.setGeometry(QtCore.QRect(690, 230, 88, 23))
        self.pbtn_PurchaseList_Pre_Itm_Save.setObjectName("pbtn_PurchaseList_Pre_Itm_Save")
        self.pbtn_PurchaseList_Pre_Itm_Update = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Pre)
        self.pbtn_PurchaseList_Pre_Itm_Update.setGeometry(QtCore.QRect(1140, 230, 88, 23))
        self.pbtn_PurchaseList_Pre_Itm_Update.setObjectName("pbtn_PurchaseList_Pre_Itm_Update")
        self.pbtn_PurchaseList_Pre_Run.setText("执行")
        self.pbtn_PurchaseList_Pre_Query.setText("查询")
        self.pbtn_PurchaseList_Pre_New.setText("新建")
        self.pbtn_PurchaseList_Pre_Save.setText("保存")
        self.pbtn_PurchaseList_Pre_Update.setText("更新")
        self.pbtn_PurchaseList_Pre_Cancel.setText("取消")
        self.pbtn_PurchaseList_Pre_Modify.setText("修改")
        self.pbtn_PurchaseList_Pre_Delete.setText("删除")
        self.pbtn_PurchaseList_Pre_Run.setEnabled(False)
        self.pbtn_PurchaseList_Pre_Save.setEnabled(False)
        self.pbtn_PurchaseList_Pre_Update.setEnabled(False)
        self.pbtn_PurchaseList_Pre_Cancel.setEnabled(False)
        self.pbtn_PurchaseList_Pre_Itm_Delete.setText("删除")
        self.pbtn_PurchaseList_Pre_Itm_Cancel.setText("取消")
        self.pbtn_PurchaseList_Pre_Itm_Query.setText("查询")
        self.pbtn_PurchaseList_Pre_Itm_Run.setText("执行")
        self.pbtn_PurchaseList_Pre_Itm_New.setText("新建")
        self.pbtn_PurchaseList_Pre_Itm_Save.setText("保存")
        self.pbtn_PurchaseList_Pre_Itm_Modify.setText("修改")
        self.pbtn_PurchaseList_Pre_Itm_Update.setText("更新")
        self.pbtn_PurchaseList_Pre_Itm_Run.setEnabled(False)
        self.pbtn_PurchaseList_Pre_Itm_Save.setEnabled(False)
        self.pbtn_PurchaseList_Pre_Itm_Update.setEnabled(False)
        self.pbtn_PurchaseList_Pre_Itm_Cancel.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Project_PurchaseList_Pre, "项目采购售前单")
        self.pbtn_PurchaseList_Pre_New.clicked.connect(self.click_pbtn_PurchaseList_Pre_New)
        self.pbtn_PurchaseList_Pre_Itm_New.clicked.connect(self.click_pbtn_PurchaseList_Pre_Itm_New)
        # 采购项清单
        self.tbw_Project_PurchaseList_Pre.itemSelectionChanged.connect(self.click_tbw_Project_PurchaseList_Pre)
        # 绑定popup窗口
        self.popup_account_projectA.pbtn_Pick.clicked.connect(self.popup_project_click_pbtn_pickA)
        self.popup_account_projectA.pbtn_Quit.clicked.connect(self.popup_project_click_pbtn_quit)
        self.popup_account_projectB.pbtn_Pick.clicked.connect(self.popup_project_click_pbtn_pickB)
        self.popup_account_projectB.pbtn_Quit.clicked.connect(self.popup_project_click_pbtn_quit)
        self.popup_purchaselist_pre.pbtn_popup_PurchaseList_Pre_Save.clicked.connect(
            self.popup_popup_PurchaseList_Pre_Save)
        self.popup_purchaselist_pre.pbtn_popup_PurchaseList_Pre_Cancel.clicked.connect(
            self.popup_popup_PurchaseList_Pre_Cancel)
        self.popup_purchaseList_itm_pre.pbtn_popup_PurchaseList_Itm_Pre_Save.clicked.connect(
            self.popup_popup_PurchaseList_Pre_Itm_Save)
        self.popup_purchaseList_itm_pre.pbtn_popup_PurchaseList_Itm_Pre_Cancel.clicked.connect(
            self.popup_popup_PurchaseList_Pre_Itm_Cancel)
    # 项目排版：详细页签（项目采购计划单）
    def dTabProjectPurchaseListPlan(self):
        self.Dtab_Project_PurchaseList_Plan = QtWidgets.QWidget()
        self.Dtab_Project_PurchaseList_Plan.setObjectName("Dtab_Project_PurchaseList_Plan")
        self.tbw_Project_PurchaseList_Plan = QtWidgets.QTableWidget(self.Dtab_Project_PurchaseList_Plan)
        self.tbw_Project_PurchaseList_Plan.setGeometry(QtCore.QRect(0, 40, 1351, 211))
        self.tbw_Project_PurchaseList_Plan.setObjectName("tbw_Project_PurchaseList_Plan")
        self.tbw_Project_PurchaseList_Plan.setRowCount(0)
        self.tbw_Project_PurchaseList_Plan.setColumnCount(5)
        self.tbw_Project_PurchaseList_Plan.setHorizontalHeaderLabels(['采购单id', '采购模块', '状态', '提交人', '审核人'])
        self.tbw_Project_PurchaseList_Plan.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_PurchaseList_Plan.verticalHeader().setVisible(False)
        self.tbw_Project_PurchaseList_Plan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_PurchaseList_Plan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_PurchaseList_Plan.setAlternatingRowColors(True)
        self.tbw_Project_PurchaseList_Plan.resizeColumnsToContents()
        self.tbw_Project_PurchaseList_Plan.resizeRowsToContents()
        self.tbw_Project_PurchaseList_Plan_Item = QtWidgets.QTableWidget(self.Dtab_Project_PurchaseList_Plan)
        self.tbw_Project_PurchaseList_Plan_Item.setGeometry(QtCore.QRect(0, 290, 1351, 181))
        self.tbw_Project_PurchaseList_Plan_Item.setObjectName("tbw_Project_PurchaseList_Plan_Item")
        self.tbw_Project_PurchaseList_Plan_Item.setRowCount(0)
        self.tbw_Project_PurchaseList_Plan_Item.setColumnCount(16)
        self.tbw_Project_PurchaseList_Plan_Item.setHorizontalHeaderLabels(
            ['采购项id', '产品名称', '规格型号', '技术标准','供应商名称', '行业', '规模', '品牌', '型号', '上市日期', '价格', '供货周期', '数量', '单位', '询价日期', '备注'])
        self.tbw_Project_PurchaseList_Plan_Item.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_PurchaseList_Plan_Item.verticalHeader().setVisible(False)
        self.tbw_Project_PurchaseList_Plan_Item.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_PurchaseList_Plan_Item.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_PurchaseList_Plan_Item.setAlternatingRowColors(True)
        self.tbw_Project_PurchaseList_Plan_Item.resizeColumnsToContents()
        self.tbw_Project_PurchaseList_Plan_Item.resizeRowsToContents()
        self.label_73 = QtWidgets.QLabel(self.Dtab_Project_PurchaseList_Plan)
        self.label_73.setGeometry(QtCore.QRect(10, 260, 150, 16))
        self.label_73.setObjectName("label_73")
        self.label_122 = QtWidgets.QLabel(self.Dtab_Project_PurchaseList_Plan)
        self.label_122.setGeometry(QtCore.QRect(10, 10, 150, 16))
        self.label_122.setObjectName("label_122")
        self.pbtn_Project_PurchaseList_Plan_Query = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Query.setGeometry(QtCore.QRect(790, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Query.setObjectName("pbtn_Project_PurchaseList_Plan_Query")
        self.pbtn_Project_PurchaseList_Plan_Cancel = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Cancel.setGeometry(QtCore.QRect(970, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Cancel.setObjectName("pbtn_Project_PurchaseList_Plan_Cancel")
        self.pbtn_Project_PurchaseList_Plan_Save = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Save.setGeometry(QtCore.QRect(700, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Save.setObjectName("pbtn_Project_PurchaseList_Plan_Save")
        self.pbtn_Project_PurchaseList_Plan_Update = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Update.setGeometry(QtCore.QRect(1150, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Update.setObjectName("pbtn_Project_PurchaseList_Plan_Update")
        self.pbtn_Project_PurchaseList_Plan_Delete = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Delete.setGeometry(QtCore.QRect(1240, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Delete.setObjectName("pbtn_Project_PurchaseList_Plan_Delete")
        self.pbtn_Project_PurchaseList_Plan_Modify = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Modify.setGeometry(QtCore.QRect(1060, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Modify.setObjectName("pbtn_Project_PurchaseList_Plan_Modify")
        self.pbtn_Project_PurchaseList_Plan_Run = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Run.setGeometry(QtCore.QRect(880, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Run.setObjectName("pbtn_Project_PurchaseList_Plan_Run")
        self.pbtn_Project_PurchaseList_Plan_New = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_New.setGeometry(QtCore.QRect(610, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_New.setObjectName("pbtn_Project_PurchaseList_Plan_New")
        self.pbtn_Project_PurchaseList_Plan_Item_Query = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Item_Query.setGeometry(QtCore.QRect(790, 260, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Item_Query.setObjectName("pbtn_Project_PurchaseList_Plan_Item_Query")
        self.pbtn_Project_PurchaseList_Plan_Item_Cancel = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Item_Cancel.setGeometry(QtCore.QRect(970, 260, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Item_Cancel.setObjectName("pbtn_Project_PurchaseList_Plan_Item_Cancel")
        self.pbtn_Project_PurchaseList_Plan_Item_Save = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Item_Save.setGeometry(QtCore.QRect(700, 260, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Item_Save.setObjectName("pbtn_Project_PurchaseList_Plan_Item_Save")
        self.pbtn_Project_PurchaseList_Plan_Item_Update = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Item_Update.setGeometry(QtCore.QRect(1150, 260, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Item_Update.setObjectName("pbtn_Project_PurchaseList_Plan_Item_Update")
        self.pbtn_Project_PurchaseList_Plan_Item_Delete = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Item_Delete.setGeometry(QtCore.QRect(1240, 260, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Item_Delete.setObjectName("pbtn_Project_PurchaseList_Plan_Item_Delete")
        self.pbtn_Project_PurchaseList_Plan_Item_Modify = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Item_Modify.setGeometry(QtCore.QRect(1060, 260, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Item_Modify.setObjectName("pbtn_Project_PurchaseList_Plan_Item_Modify")
        self.pbtn_Project_PurchaseList_Plan_Item_Run = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Item_Run.setGeometry(QtCore.QRect(880, 260, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Item_Run.setObjectName("pbtn_Project_PurchaseList_Plan_Item_Run")
        self.pbtn_Project_PurchaseList_Plan_Item_New = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Item_New.setGeometry(QtCore.QRect(610, 260, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Item_New.setObjectName("pbtn_Project_PurchaseList_Plan_Item_New")
        self.pbtn_Project_PurchaseList_Plan_Auto = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Plan)
        self.pbtn_Project_PurchaseList_Plan_Auto.setGeometry(QtCore.QRect(520, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Plan_Auto.setObjectName("pbtn_Project_PurchaseList_Plan_Auto")
        self.label_73.setText("各模块清单内容↓")
        self.label_122.setText("计划模块清单↓")
        self.pbtn_Project_PurchaseList_Plan_Auto.setText("草案")
        self.pbtn_Project_PurchaseList_Plan_Run.setText("执行")
        self.pbtn_Project_PurchaseList_Plan_Query.setText("查询")
        self.pbtn_Project_PurchaseList_Plan_New.setText("新建")
        self.pbtn_Project_PurchaseList_Plan_Save.setText("保存")
        self.pbtn_Project_PurchaseList_Plan_Update.setText("更新")
        self.pbtn_Project_PurchaseList_Plan_Cancel.setText("取消")
        self.pbtn_Project_PurchaseList_Plan_Modify.setText("修改")
        self.pbtn_Project_PurchaseList_Plan_Delete.setText("删除")
        self.pbtn_Project_PurchaseList_Plan_Item_Delete.setText("删除")
        self.pbtn_Project_PurchaseList_Plan_Item_Cancel.setText("取消")
        self.pbtn_Project_PurchaseList_Plan_Item_Query.setText("查询")
        self.pbtn_Project_PurchaseList_Plan_Item_Run.setText("执行")
        self.pbtn_Project_PurchaseList_Plan_Item_New.setText("新建")
        self.pbtn_Project_PurchaseList_Plan_Item_Save.setText("保存")
        self.pbtn_Project_PurchaseList_Plan_Item_Modify.setText("修改")
        self.pbtn_Project_PurchaseList_Plan_Item_Update.setText("更新")
        self.Tab_Detail.addTab(self.Dtab_Project_PurchaseList_Plan, "项目采购计划单")
        self.pbtn_Project_PurchaseList_Plan_Auto.clicked.connect(self.click_pbtn_Project_PurchaseList_Plan_Auto)
        # 采购项清单
        self.tbw_Project_PurchaseList_Plan.itemSelectionChanged.connect(self.click_tbw_Project_PurchaseList_Plan)
    # 项目排版：详细页签（项目立项单）
    def dTabProjectApproval(self):
        self.Dtab_Project_Approval = QtWidgets.QWidget()
        self.Dtab_Project_Approval.setObjectName("Dtab_Project_Approval")
        self.label_74 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_74.setGeometry(QtCore.QRect(70, 50, 81, 16))
        self.label_74.setObjectName("label_74")
        self.label_74.setText("项目名称：")
        self.label_75 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_75.setGeometry(QtCore.QRect(80, 90, 81, 16))
        self.label_75.setObjectName("label_75")
        self.label_75.setText("建设单位：")
        self.label_76 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_76.setGeometry(QtCore.QRect(80, 130, 71, 16))
        self.label_76.setObjectName("label_76")
        self.label_76.setText("立项人：")
        self.label_77 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_77.setGeometry(QtCore.QRect(70, 160, 91, 21))
        self.label_77.setObjectName("label_77")
        self.label_77.setText("技术负责人：")
        self.label_78 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_78.setGeometry(QtCore.QRect(80, 210, 91, 21))
        self.label_78.setObjectName("label_78")
        self.label_78.setText("项目经理：")
        self.label_79 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_79.setGeometry(QtCore.QRect(80, 260, 91, 21))
        self.label_79.setObjectName("label_79")
        self.label_79.setText("招标方式：")
        self.label_80 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_80.setGeometry(QtCore.QRect(80, 310, 91, 16))
        self.label_80.setObjectName("label_80")
        self.label_80.setText("项目合同额：")
        self.label_81 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_81.setGeometry(QtCore.QRect(70, 350, 101, 16))
        self.label_81.setObjectName("label_81")
        self.label_81.setText("工程部预算：")
        self.label_82 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_82.setGeometry(QtCore.QRect(80, 390, 91, 16))
        self.label_82.setObjectName("label_82")
        self.label_82.setText("采购部预算：")
        self.label_83 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_83.setGeometry(QtCore.QRect(380, 50, 91, 16))
        self.label_83.setObjectName("label_83")
        self.label_83.setText("项目简称：")
        self.label_84 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_84.setGeometry(QtCore.QRect(380, 80, 71, 21))
        self.label_84.setObjectName("label_84")
        self.label_84.setText("项目编号：")
        self.label_85 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_85.setGeometry(QtCore.QRect(380, 120, 81, 16))
        self.label_85.setObjectName("label_85")
        self.label_85.setText("立项时间：")
        self.label_86 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_86.setGeometry(QtCore.QRect(380, 150, 91, 21))
        self.label_86.setObjectName("label_86")
        self.label_86.setText("项目合作方：")
        self.label_87 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_87.setGeometry(QtCore.QRect(380, 200, 91, 21))
        self.label_87.setObjectName("label_87")
        self.label_87.setText("业务负责人：")
        self.label_88 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_88.setGeometry(QtCore.QRect(380, 250, 91, 21))
        self.label_88.setObjectName("label_88")
        self.label_88.setText("中标日期：")
        self.label_89 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_89.setGeometry(QtCore.QRect(380, 300, 91, 16))
        self.label_89.setObjectName("label_89")
        self.label_89.setText("毛利润估算：")
        self.label_90 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_90.setGeometry(QtCore.QRect(380, 340, 91, 21))
        self.label_90.setObjectName("label_90")
        self.label_90.setText("业务部预算：")
        self.label_91 = QtWidgets.QLabel(self.Dtab_Project_Approval)
        self.label_91.setGeometry(QtCore.QRect(380, 390, 120, 15))
        self.label_91.setObjectName("label_91")
        self.label_91.setText("其他预算费用：")
        self.lEdit_PrjApp_Name = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Name.setGeometry(QtCore.QRect(190, 50, 113, 20))
        self.lEdit_PrjApp_Name.setObjectName("lEdit_PrjApp_Name")
        self.lEdit_PrjApp_CnstName = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_CnstName.setGeometry(QtCore.QRect(190, 90, 113, 20))
        self.lEdit_PrjApp_CnstName.setObjectName("lEdit_PrjApp_CnstName")
        self.lEdit_PrjApp_Creator = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Creator.setGeometry(QtCore.QRect(190, 130, 113, 20))
        self.lEdit_PrjApp_Creator.setObjectName("lEdit_PrjApp_Creator")
        self.lEdit_PrjApp_TechMan = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_TechMan.setGeometry(QtCore.QRect(190, 160, 113, 20))
        self.lEdit_PrjApp_TechMan.setObjectName("lEdit_PrjApp_TechMan")
        self.lEdit_PrjApp_PM = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_PM.setGeometry(QtCore.QRect(190, 210, 113, 20))
        self.lEdit_PrjApp_PM.setObjectName("lEdit_PrjApp_PM")
        self.lEdit_PrjApp_Bid = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Bid.setGeometry(QtCore.QRect(190, 260, 113, 20))
        self.lEdit_PrjApp_Bid.setObjectName("lEdit_PrjApp_Bid")
        self.lEdit_PrjApp_Amount = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Amount.setGeometry(QtCore.QRect(190, 310, 113, 20))
        self.lEdit_PrjApp_Amount.setObjectName("lEdit_PrjApp_Amount")
        self.lEdit_PrjApp_Const_Pre = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Const_Pre.setGeometry(QtCore.QRect(190, 350, 113, 20))
        self.lEdit_PrjApp_Const_Pre.setObjectName("lEdit_PrjApp_Const_Pre")
        self.lEdit_PrjApp_Purchase_Pre = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Purchase_Pre.setGeometry(QtCore.QRect(190, 390, 113, 20))
        self.lEdit_PrjApp_Purchase_Pre.setObjectName("lEdit_PrjApp_Purchase_Pre")
        self.lEdit_PrjApp_ShortName = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_ShortName.setGeometry(QtCore.QRect(480, 50, 113, 20))
        self.lEdit_PrjApp_ShortName.setObjectName("lEdit_PrjApp_ShortName")
        self.lEdit_PrjApp_ProjectNo = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_ProjectNo.setGeometry(QtCore.QRect(480, 80, 113, 20))
        self.lEdit_PrjApp_ProjectNo.setObjectName("lEdit_PrjApp_ProjectNo")
        self.lEdit_PrjApp_CreateDT = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_CreateDT.setGeometry(QtCore.QRect(480, 120, 113, 20))
        self.lEdit_PrjApp_CreateDT.setObjectName("lEdit_PrjApp_CreateDT")
        self.lEdit_PrjApp_Partner = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Partner.setGeometry(QtCore.QRect(480, 160, 113, 20))
        self.lEdit_PrjApp_Partner.setObjectName("lEdit_PrjApp_Partner")
        self.lEdit_PrjApp_BL = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_BL.setGeometry(QtCore.QRect(480, 200, 113, 20))
        self.lEdit_PrjApp_BL.setObjectName("lEdit_PrjApp_BL")
        self.lEdit_PrjApp_WinDT = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_WinDT.setGeometry(QtCore.QRect(480, 250, 113, 20))
        self.lEdit_PrjApp_WinDT.setObjectName("lEdit_PrjApp_WinDT")
        self.lEdit_PrjApp_GP_Pre = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_GP_Pre.setGeometry(QtCore.QRect(480, 300, 113, 20))
        self.lEdit_PrjApp_GP_Pre.setObjectName("lEdit_PrjApp_GP_Pre")
        self.lEdit_PrjApp_Bus_Pre = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Bus_Pre.setGeometry(QtCore.QRect(480, 340, 113, 20))
        self.lEdit_PrjApp_Bus_Pre.setObjectName("lEdit_PrjApp_Bus_Pre")
        self.lEdit_PrjApp_Oth_Ore = QtWidgets.QLineEdit(self.Dtab_Project_Approval)
        self.lEdit_PrjApp_Oth_Ore.setGeometry(QtCore.QRect(490, 390, 113, 20))
        self.lEdit_PrjApp_Oth_Ore.setObjectName("lEdit_PrjApp_Oth_Ore")
        self.pbtn_Project_Approval_Query = QtWidgets.QPushButton(self.Dtab_Project_Approval)
        self.pbtn_Project_Approval_Query.setGeometry(QtCore.QRect(790, 10, 88, 23))
        self.pbtn_Project_Approval_Query.setObjectName("pbtn_Project_Approval_Query")
        self.pbtn_Project_Approval_Cancel = QtWidgets.QPushButton(self.Dtab_Project_Approval)
        self.pbtn_Project_Approval_Cancel.setGeometry(QtCore.QRect(970, 10, 88, 23))
        self.pbtn_Project_Approval_Cancel.setObjectName("pbtn_Project_Approval_Cancel")
        self.pbtn_Project_Approval_Save = QtWidgets.QPushButton(self.Dtab_Project_Approval)
        self.pbtn_Project_Approval_Save.setGeometry(QtCore.QRect(700, 10, 88, 23))
        self.pbtn_Project_Approval_Save.setObjectName("pbtn_Project_Approval_Save")
        self.pbtn_Project_Approval_Update = QtWidgets.QPushButton(self.Dtab_Project_Approval)
        self.pbtn_Project_Approval_Update.setGeometry(QtCore.QRect(1150, 10, 88, 23))
        self.pbtn_Project_Approval_Update.setObjectName("pbtn_Project_Approval_Update")
        self.pbtn_Project_Approval_Delete = QtWidgets.QPushButton(self.Dtab_Project_Approval)
        self.pbtn_Project_Approval_Delete.setGeometry(QtCore.QRect(1240, 10, 88, 23))
        self.pbtn_Project_Approval_Delete.setObjectName("pbtn_Project_Approval_Delete")
        self.pbtn_Project_Approval_Modify = QtWidgets.QPushButton(self.Dtab_Project_Approval)
        self.pbtn_Project_Approval_Modify.setGeometry(QtCore.QRect(1060, 10, 88, 23))
        self.pbtn_Project_Approval_Modify.setObjectName("pbtn_Project_Approval_Modify")
        self.pbtn_Project_Approval_Run = QtWidgets.QPushButton(self.Dtab_Project_Approval)
        self.pbtn_Project_Approval_Run.setGeometry(QtCore.QRect(880, 10, 88, 23))
        self.pbtn_Project_Approval_Run.setObjectName("pbtn_Project_Approval_Run")
        self.pbtn_Project_Approval_New = QtWidgets.QPushButton(self.Dtab_Project_Approval)
        self.pbtn_Project_Approval_New.setGeometry(QtCore.QRect(610, 10, 88, 23))
        self.pbtn_Project_Approval_New.setObjectName("pbtn_Project_Approval_New")
        self.pbtn_Project_Approval_Query.setText("查询")
        self.pbtn_Project_Approval_Cancel.setText("取消")
        self.pbtn_Project_Approval_Save.setText("保存")
        self.pbtn_Project_Approval_Update.setText("更新")
        self.pbtn_Project_Approval_Delete.setText("删除")
        self.pbtn_Project_Approval_Modify.setText("修改")
        self.pbtn_Project_Approval_Run.setText("执行")
        self.pbtn_Project_Approval_New.setText("新建")
        self.pbtn_Project_Approval_Query.setEnabled(True)
        self.pbtn_Project_Approval_Cancel.setEnabled(False)
        self.pbtn_Project_Approval_Save.setEnabled(False)
        self.pbtn_Project_Approval_Update.setEnabled(False)
        self.pbtn_Project_Approval_Delete.setEnabled(True)
        self.pbtn_Project_Approval_Modify.setEnabled(True)
        self.pbtn_Project_Approval_Run.setEnabled(False)
        self.pbtn_Project_Approval_New.setEnabled(True)
        self.lEdit_PrjApp_Name.setEnabled(False)
        self.lEdit_PrjApp_ShortName.setEnabled(False)
        self.lEdit_PrjApp_CnstName.setEnabled(False)
        self.lEdit_PrjApp_ProjectNo.setEnabled(False)
        self.lEdit_PrjApp_Creator.setEnabled(False)
        self.lEdit_PrjApp_CreateDT.setEnabled(False)
        self.lEdit_PrjApp_TechMan.setEnabled(False)
        self.lEdit_PrjApp_Partner.setEnabled(False)
        self.lEdit_PrjApp_PM.setEnabled(False)
        self.lEdit_PrjApp_BL.setEnabled(False)
        self.lEdit_PrjApp_Bid.setEnabled(False)
        self.lEdit_PrjApp_WinDT.setEnabled(False)
        self.lEdit_PrjApp_Amount.setEnabled(False)
        self.lEdit_PrjApp_GP_Pre.setEnabled(False)
        self.lEdit_PrjApp_Const_Pre.setEnabled(False)
        self.lEdit_PrjApp_Bus_Pre.setEnabled(False)
        self.lEdit_PrjApp_Purchase_Pre.setEnabled(False)
        self.lEdit_PrjApp_Oth_Ore.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Project_Approval, "项目立项单")
        self.pbtn_Project_Approval_New.clicked.connect(self.click_pbtn_Project_Approval_New)
        self.pbtn_Project_Approval_Save.clicked.connect(self.click_pbtn_Project_Approval_Save)
        self.pbtn_Project_Approval_Cancel.clicked.connect(self.click_pbtn_Project_Approval_Cancel)
    # 项目排版：详细页签（项目采购申请单）
    def dTabProjectPurchaseListAppr(self):
        self.Dtab_Project_PurchaseList_Appr = QtWidgets.QWidget()
        self.Dtab_Project_PurchaseList_Appr.setObjectName("Dtab_Project_PurchaseList_Appr")
        self.tbw_Project_PurchaseList_Appr = QtWidgets.QTableWidget(self.Dtab_Project_PurchaseList_Appr)
        self.tbw_Project_PurchaseList_Appr.setGeometry(QtCore.QRect(0, 40, 1321, 181))
        self.tbw_Project_PurchaseList_Appr.setObjectName("tbw_Project_PurchaseList_Appr")
        self.tbw_Project_PurchaseList_Appr.setColumnCount(0)
        self.tbw_Project_PurchaseList_Appr.setRowCount(0)
        self.pbtn_Project_PurchaseList_Appr_New = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_New.setGeometry(QtCore.QRect(590, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_New.setObjectName("pbtn_Project_PurchaseList_Appr_New")
        self.pbtn_Project_PurchaseList_Appr_Modify = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Modify.setGeometry(QtCore.QRect(1040, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Modify.setObjectName("pbtn_Project_PurchaseList_Appr_Modify")
        self.pbtn_Project_PurchaseList_Appr_Cancel = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Cancel.setGeometry(QtCore.QRect(950, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Cancel.setObjectName("pbtn_Project_PurchaseList_Appr_Cancel")
        self.pbtn_Project_PurchaseList_Appr_Delete = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Delete.setGeometry(QtCore.QRect(1220, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Delete.setObjectName("pbtn_Project_PurchaseList_Appr_Delete")
        self.pbtn_Project_PurchaseList_Appr_Query = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Query.setGeometry(QtCore.QRect(770, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Query.setObjectName("pbtn_Project_PurchaseList_Appr_Query")
        self.pbtn_Project_PurchaseList_Appr_Save = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Save.setGeometry(QtCore.QRect(680, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Save.setObjectName("pbtn_Project_PurchaseList_Appr_Save")
        self.pbtn_Project_PurchaseList_Appr_Run = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Run.setGeometry(QtCore.QRect(860, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Run.setObjectName("pbtn_Project_PurchaseList_Appr_Run")
        self.pbtn_Project_PurchaseList_Appr_Update = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Update.setGeometry(QtCore.QRect(1130, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Update.setObjectName("pbtn_Project_PurchaseList_Appr_Update")
        self.pbtn_Project_PurchaseList_Appr_Auto = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Auto.setGeometry(QtCore.QRect(500, 10, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Auto.setObjectName("pbtn_Project_PurchaseList_Appr_Auto")
        self.pbtn_Project_PurchaseList_Appr_Item_Update = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Item_Update.setGeometry(QtCore.QRect(1130, 230, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Item_Update.setObjectName("pbtn_Project_PurchaseList_Appr_Item_Update")
        self.pbtn_Project_PurchaseList_Appr_Item_Save = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Item_Save.setGeometry(QtCore.QRect(680, 230, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Item_Save.setObjectName("pbtn_Project_PurchaseList_Appr_Item_Save")
        self.pbtn_Project_PurchaseList_Appr_Item_Run = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Item_Run.setGeometry(QtCore.QRect(860, 230, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Item_Run.setObjectName("pbtn_Project_PurchaseList_Appr_Item_Run")
        self.pbtn_Project_PurchaseList_Appr_Item_Cancel = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Item_Cancel.setGeometry(QtCore.QRect(950, 230, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Item_Cancel.setObjectName("pbtn_Project_PurchaseList_Appr_Item_Cancel")
        self.tbw_Project_PurchaseList_Appr_Item = QtWidgets.QTableWidget(self.Dtab_Project_PurchaseList_Appr)
        self.tbw_Project_PurchaseList_Appr_Item.setGeometry(QtCore.QRect(0, 260, 1321, 161))
        self.tbw_Project_PurchaseList_Appr_Item.setObjectName("tbw_Project_PurchaseList_Appr_Item")
        self.tbw_Project_PurchaseList_Appr_Item.setColumnCount(0)
        self.tbw_Project_PurchaseList_Appr_Item.setRowCount(0)
        self.pbtn_Project_PurchaseList_Appr_Item_Query = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Item_Query.setGeometry(QtCore.QRect(770, 230, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Item_Query.setObjectName("pbtn_Project_PurchaseList_Appr_Item_Query")
        self.pbtn_Project_PurchaseList_Appr_Item_New = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Item_New.setGeometry(QtCore.QRect(590, 230, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Item_New.setObjectName("pbtn_Project_PurchaseList_Appr_Item_New")
        self.pbtn_Project_PurchaseList_Appr_Item_Modify = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Item_Modify.setGeometry(QtCore.QRect(1040, 230, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Item_Modify.setObjectName("pbtn_Project_PurchaseList_Appr_Item_Modify")
        self.pbtn_Project_PurchaseList_Appr_Item_Delete = QtWidgets.QPushButton(self.Dtab_Project_PurchaseList_Appr)
        self.pbtn_Project_PurchaseList_Appr_Item_Delete.setGeometry(QtCore.QRect(1220, 230, 88, 23))
        self.pbtn_Project_PurchaseList_Appr_Item_Delete.setObjectName("pbtn_Project_PurchaseList_Appr_Item_Delete")
        self.tbw_Project_PurchaseList_Appr.setColumnCount(6)
        self.tbw_Project_PurchaseList_Appr.setHorizontalHeaderLabels(['申请单id', '申请人', '申请部门', '申请事由', '希望交付日期', '提交日期'])
        self.tbw_Project_PurchaseList_Appr.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_PurchaseList_Appr.verticalHeader().setVisible(False)
        self.tbw_Project_PurchaseList_Appr.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_PurchaseList_Appr.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_PurchaseList_Appr.setAlternatingRowColors(True)
        self.tbw_Project_PurchaseList_Appr.resizeColumnsToContents()
        self.tbw_Project_PurchaseList_Appr.resizeRowsToContents()
        self.tbw_Project_PurchaseList_Appr_Item.setColumnCount(16)
        self.tbw_Project_PurchaseList_Appr_Item.setHorizontalHeaderLabels(
            ['采购项id', '产品名称', '规格型号', '技术标准','供应商名称', '行业', '规模', '品牌', '型号', '上市日期', '价格', '供货周期', '数量', '单位', '询价日期', '备注'])
        self.tbw_Project_PurchaseList_Appr_Item.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_PurchaseList_Appr_Item.verticalHeader().setVisible(False)
        self.tbw_Project_PurchaseList_Appr_Item.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_PurchaseList_Appr_Item.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_PurchaseList_Appr_Item.setAlternatingRowColors(True)
        self.tbw_Project_PurchaseList_Appr_Item.resizeColumnsToContents()
        self.tbw_Project_PurchaseList_Appr_Item.resizeRowsToContents()
        self.pbtn_Project_PurchaseList_Appr_Auto.setText("计划申请")
        self.pbtn_Project_PurchaseList_Appr_Item_Update.setText("更新")
        self.pbtn_Project_PurchaseList_Appr_Item_Save.setText("保存")
        self.pbtn_Project_PurchaseList_Appr_Item_Run.setText("执行")
        self.pbtn_Project_PurchaseList_Appr_Item_Cancel.setText("取消")
        self.pbtn_Project_PurchaseList_Appr_Item_Query.setText("查询")
        self.pbtn_Project_PurchaseList_Appr_Item_New.setText("新建")
        self.pbtn_Project_PurchaseList_Appr_Item_Modify.setText("修改")
        self.pbtn_Project_PurchaseList_Appr_Item_Delete.setText("删除")
        self.pbtn_Project_PurchaseList_Appr_New.setText("新建")
        self.pbtn_Project_PurchaseList_Appr_Modify.setText("修改")
        self.pbtn_Project_PurchaseList_Appr_Cancel.setText("取消")
        self.pbtn_Project_PurchaseList_Appr_Delete.setText("删除")
        self.pbtn_Project_PurchaseList_Appr_Query.setText("查询")
        self.pbtn_Project_PurchaseList_Appr_Save.setText("保存")
        self.pbtn_Project_PurchaseList_Appr_Run.setText("执行")
        self.pbtn_Project_PurchaseList_Appr_Update.setText("更新")
        self.Tab_Detail.addTab(self.Dtab_Project_PurchaseList_Appr, "项目采购申请单")
        self.pbtn_Project_PurchaseList_Appr_Auto.clicked.connect(self.click_pbtn_Project_PurchaseList_Appr_Auto)
        self.popup_pickup_purchase_plan_item.pbtn_Pick.clicked.connect(self.click_pbtn_Project_PurchaseList_Appr_Pick)
        # 采购项清单
        self.tbw_Project_PurchaseList_Pre.itemSelectionChanged.connect(self.click_tbw_Project_PurchaseList_Pre)
        self.tbw_Project_PurchaseList_Appr.itemSelectionChanged.connect(self.click_tbw_Project_PurchaseList_Appr)
        # 绑定popup窗口
        self.popup_account_projectA.pbtn_Pick.clicked.connect(self.popup_project_click_pbtn_pickA)

    # 项目排版：详细页签（项目合同）
    def dTabProjectContract(self):
        self.Dtab_Project_Contract = QtWidgets.QWidget()
        self.Dtab_Project_Contract.setObjectName("Dtab_Project_Contract")
        self.tbw_Project_Contract = QtWidgets.QTableWidget(self.Dtab_Project_Contract)
        self.tbw_Project_Contract.setGeometry(QtCore.QRect(10, 20, 1301, 321))
        self.tbw_Project_Contract.setObjectName("tbw_Project_Contract")
        self.tbw_Project_Contract.setColumnCount(7)
        self.tbw_Project_Contract.setRowCount(0)
        self.tbw_Project_Contract.setHorizontalHeaderLabels(['合同id', '合同编号', '合同类型', '甲方', '乙方', '合同金额', '合同日期'])
        self.tbw_Project_Contract.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_Contract.verticalHeader().setVisible(False)
        self.tbw_Project_Contract.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_Contract.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_Contract.setAlternatingRowColors(True)
        self.tbw_Project_Contract.resizeColumnsToContents()
        self.tbw_Project_Contract.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Project_Contract, "项目合同")
    # 项目排版：详细页签（项目供应商）
    def dTabProjectSuppiler(self):
        self.Dtab_Project_Supppiler = QtWidgets.QWidget()
        self.Dtab_Project_Supppiler.setObjectName("Dtab_Project_Supppiler")
        self.tbw_Project_Supppiler = QtWidgets.QTableWidget(self.Dtab_Project_Supppiler)
        self.tbw_Project_Supppiler.setGeometry(QtCore.QRect(10, 30, 1301, 261))
        self.tbw_Project_Supppiler.setObjectName("tbw_Project_Supppiler")
        self.tbw_Project_Supppiler.setColumnCount(9)
        self.tbw_Project_Supppiler.setRowCount(0)
        self.tbw_Project_Supppiler.setHorizontalHeaderLabels(
            ['供应商id', '供应商名称', '行业', '规模', '省份', '采购总额', '已支付总额', '已回票总额', '回票比率'])
        self.tbw_Project_Supppiler.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_Supppiler.verticalHeader().setVisible(False)
        self.tbw_Project_Supppiler.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_Supppiler.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_Supppiler.setAlternatingRowColors(True)
        self.tbw_Project_Supppiler.resizeColumnsToContents()
        self.tbw_Project_Supppiler.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Project_Supppiler, "项目供应商")
    # 项目排版：详细页签（项目采购订单）
    def dTabProjectCostPurchase(self):
        self.Dtab_Project_Cost_Purchase = QtWidgets.QWidget()
        self.Dtab_Project_Cost_Purchase.setObjectName("Dtab_Project_Cost_Purchase")
        self.tbw_Project_Cost_Purchase = QtWidgets.QTableWidget(self.Dtab_Project_Cost_Purchase)
        self.tbw_Project_Cost_Purchase.setGeometry(QtCore.QRect(10, 30, 1321, 171))
        self.tbw_Project_Cost_Purchase.setObjectName("tbw_Project_Cost_Purchase")
        self.tbw_Project_Cost_Purchase.setColumnCount(7)
        self.tbw_Project_Cost_Purchase.setRowCount(0)
        self.tbw_Project_Cost_Purchase.setHorizontalHeaderLabels(
            ['订单id', '订单名称', '采购合同编号', '供应商', '采购合同总额', '订单金额', '回票总额'])
        self.tbw_Project_Cost_Purchase.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_Cost_Purchase.verticalHeader().setVisible(False)
        self.tbw_Project_Cost_Purchase.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_Cost_Purchase.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_Cost_Purchase.setAlternatingRowColors(True)
        self.tbw_Project_Cost_Purchase.resizeColumnsToContents()
        self.tbw_Project_Cost_Purchase.resizeRowsToContents()
        self.tbw_Project_Cost_Purchase_Payment = QtWidgets.QTableWidget(self.Dtab_Project_Cost_Purchase)
        self.tbw_Project_Cost_Purchase_Payment.setGeometry(QtCore.QRect(10, 230, 681, 211))
        self.tbw_Project_Cost_Purchase_Payment.setObjectName("tbw_Project_Cost_Purchase_Payment")
        self.tbw_Project_Cost_Purchase_Payment.setColumnCount(8)
        self.tbw_Project_Cost_Purchase_Payment.setRowCount(0)
        self.tbw_Project_Cost_Purchase_Payment.setHorizontalHeaderLabels(
            ['支款单id', '支款日期', '支款原因', '支款金额(含税)', '支款部门', '支款人', '支款方式', '支票号'])
        self.tbw_Project_Cost_Purchase_Payment.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_Cost_Purchase_Payment.verticalHeader().setVisible(False)
        self.tbw_Project_Cost_Purchase_Payment.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_Cost_Purchase_Payment.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_Cost_Purchase_Payment.setAlternatingRowColors(True)
        self.tbw_Project_Cost_Purchase_Payment.resizeColumnsToContents()
        self.tbw_Project_Cost_Purchase_Payment.resizeRowsToContents()
        self.tbw_Project_Cost_Purchase_Invoice = QtWidgets.QTableWidget(self.Dtab_Project_Cost_Purchase)
        self.tbw_Project_Cost_Purchase_Invoice.setGeometry(QtCore.QRect(710, 230, 621, 211))
        self.tbw_Project_Cost_Purchase_Invoice.setObjectName("tbw_Project_Cost_Purchase_Invoice")
        self.tbw_Project_Cost_Purchase_Invoice.setColumnCount(9)
        self.tbw_Project_Cost_Purchase_Invoice.setRowCount(0)
        self.tbw_Project_Cost_Purchase_Invoice.setHorizontalHeaderLabels(
            ['发票id', '回票日期', '开票日期', '发票号码', '价税合计', '税率', '票兑余额', '销售方', '购买方'])
        self.tbw_Project_Cost_Purchase_Invoice.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_Cost_Purchase_Invoice.verticalHeader().setVisible(False)
        self.tbw_Project_Cost_Purchase_Invoice.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_Cost_Purchase_Invoice.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_Cost_Purchase_Invoice.setAlternatingRowColors(True)
        self.tbw_Project_Cost_Purchase_Invoice.resizeColumnsToContents()
        self.tbw_Project_Cost_Purchase_Invoice.resizeRowsToContents()
        self.label_92 = QtWidgets.QLabel(self.Dtab_Project_Cost_Purchase)
        self.label_92.setGeometry(QtCore.QRect(20, 10, 120, 15))
        self.label_92.setObjectName("label_92")
        self.label_92.setText("采购单↓")
        self.label_93 = QtWidgets.QLabel(self.Dtab_Project_Cost_Purchase)
        self.label_93.setGeometry(QtCore.QRect(20, 210, 120, 15))
        self.label_93.setObjectName("label_93")
        self.label_93.setText("支款单↓")
        self.label_94 = QtWidgets.QLabel(self.Dtab_Project_Cost_Purchase)
        self.label_94.setGeometry(QtCore.QRect(710, 210, 120, 15))
        self.label_94.setObjectName("label_94")
        self.label_94.setText("发票单↓")
        self.pbtn_Project_Cost_Purchase_Payment_New = QtWidgets.QPushButton(self.Dtab_Project_Cost_Purchase)
        self.pbtn_Project_Cost_Purchase_Payment_New.setGeometry(QtCore.QRect(600, 210, 88, 23))
        self.pbtn_Project_Cost_Purchase_Payment_New.setObjectName("pbtn_Project_Cost_Purchase_Payment_New")
        self.pbtn_Project_Cost_Purchase_Payment_New.setText("新建")
        self.Tab_Detail.addTab(self.Dtab_Project_Cost_Purchase, "项目采购订单")
        self.pbtn_Project_Cost_Purchase_Payment_New.clicked.connect(self.click_pbtn_Project_Cost_Purchase_Payment_New)
        self.popup_payment.pbtn_Save.clicked.connect(self.click_pbtn_Project_Cost_Purchase_Payment_Save)
        self.popup_payment.pbtn_Cancel.clicked.connect(self.click_pbtn_Project_Cost_Purchase_Payment_Cancel)
        self.tbw_Project_Cost_Purchase.itemSelectionChanged.connect(self.click_tbw_Project_Cost_Purchase)
        self.tbw_Project_Cost_Purchase_Payment.itemSelectionChanged.connect(self.click_tbw_Project_Cost_Purchase_Payment)
    # 项目排版：详细页签（项目开票及回款）
    def dTabProjectCostReturn(self):
        self.Dtab_Project_Cost_Return = QtWidgets.QWidget()
        self.Dtab_Project_Cost_Return.setObjectName("Dtab_Project_Cost_Return")
        self.tbw_Project_Cost_Return_Invoice = QtWidgets.QTableWidget(self.Dtab_Project_Cost_Return)
        self.tbw_Project_Cost_Return_Invoice.setGeometry(QtCore.QRect(0, 30, 1291, 181))
        self.tbw_Project_Cost_Return_Invoice.setObjectName("tbw_Project_Cost_Return_Invoice")
        self.tbw_Project_Cost_Return_Invoice.setColumnCount(11)
        self.tbw_Project_Cost_Return_Invoice.setRowCount(0)
        self.tbw_Project_Cost_Return_Invoice.setHorizontalHeaderLabels(
            ['开票id', '所属项目', '开票日期', '销售方', '购买方', '发票号码', '发票种类', '发票金额', '税率', '备注', '已开票未回款金额'])
        self.tbw_Project_Cost_Return_Invoice.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_Cost_Return_Invoice.verticalHeader().setVisible(False)
        self.tbw_Project_Cost_Return_Invoice.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_Cost_Return_Invoice.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_Cost_Return_Invoice.setAlternatingRowColors(True)
        self.tbw_Project_Cost_Return_Invoice.resizeColumnsToContents()
        self.tbw_Project_Cost_Return_Invoice.resizeRowsToContents()
        self.tbw_Project_Cost_Return_Payment = QtWidgets.QTableWidget(self.Dtab_Project_Cost_Return)
        self.tbw_Project_Cost_Return_Payment.setGeometry(QtCore.QRect(0, 240, 1291, 161))
        self.tbw_Project_Cost_Return_Payment.setObjectName("tbw_Project_Cost_Return_Payment")
        self.tbw_Project_Cost_Return_Payment.setColumnCount(7)
        self.tbw_Project_Cost_Return_Payment.setRowCount(0)
        self.tbw_Project_Cost_Return_Payment.setHorizontalHeaderLabels(
            ['回款id', '回款日期', '回款类型', '票据类型', '票据编码', '经办人', '回款金额'])
        self.tbw_Project_Cost_Return_Payment.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_Cost_Return_Payment.verticalHeader().setVisible(False)
        self.tbw_Project_Cost_Return_Payment.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_Cost_Return_Payment.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_Cost_Return_Payment.setAlternatingRowColors(True)
        self.tbw_Project_Cost_Return_Payment.resizeColumnsToContents()
        self.tbw_Project_Cost_Return_Payment.resizeRowsToContents()
        self.label_95 = QtWidgets.QLabel(self.Dtab_Project_Cost_Return)
        self.label_95.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_95.setObjectName("label_95")
        self.label_95.setText("开票信息↓")
        self.label_96 = QtWidgets.QLabel(self.Dtab_Project_Cost_Return)
        self.label_96.setGeometry(QtCore.QRect(10, 220, 71, 16))
        self.label_96.setObjectName("label_96")
        self.label_96.setText("回款信息↓")
        self.Tab_Detail.addTab(self.Dtab_Project_Cost_Return, "项目开票及回款")
    # 项目排版：详细页签（项目干系人）
    def dTabProjectContact(self):
        self.Dtab_Project_Contact = QtWidgets.QWidget()
        self.Dtab_Project_Contact.setObjectName("Dtab_Project_Contact")
        self.tbw_Project_Contact = QtWidgets.QTableWidget(self.Dtab_Project_Contact)
        self.tbw_Project_Contact.setGeometry(QtCore.QRect(0, 30, 1291, 261))
        self.tbw_Project_Contact.setObjectName("tbw_Project_Contact")
        self.tbw_Project_Contact.setColumnCount(11)
        self.tbw_Project_Contact.setRowCount(0)
        self.tbw_Project_Contact.setHorizontalHeaderLabels(
            ['人员id', '组织类型', '组织名称', '组织类型', '省份', '角色类型', '姓名', '部门', '职位', '职级', '性别'])
        self.tbw_Project_Contact.horizontalHeader().setStretchLastSection(True)
        self.tbw_Project_Contact.verticalHeader().setVisible(False)
        self.tbw_Project_Contact.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project_Contact.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project_Contact.setAlternatingRowColors(True)
        self.tbw_Project_Contact.resizeColumnsToContents()
        self.tbw_Project_Contact.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Project_Contact, "项目干系人")
    # 项目排版：主页签（项目）
    def mTabProject(self):
        self.dTabProject()
        self.dTabProjectPurchaseListPre()
        self.dTabProjectPurchaseListPlan()
        self.dTabProjectApproval()
        self.dTabProjectPurchaseListAppr()
        self.dTabProjectContract()
        self.dTabProjectSuppiler()
        self.dTabProjectCostPurchase()
        self.dTabProjectCostReturn()
        self.dTabProjectContact()
        self.tbw_Project.setRowCount(0)
        self.tbw_Project.setColumnCount(16)
        self.tbw_Project.setHorizontalHeaderLabels(
            ['项目id', '项目编号', '项目名称', '甲方', '乙方', '业务负责人', '项目经理', '合同款', '保证金', '采购预算费用', '采购发生比例',
             '工程预算费用', '工程发生比例', '业务费用', '毛利润', '毛利率'])
        self.tbw_Project.horizontalHeader().setStretchLastSection(True)
    # 项目排版：主页签（项目格式）
    def mTabProjectFormat(self):
        self.tbw_Project.verticalHeader().setVisible(False)
        self.tbw_Project.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Project.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Project.setAlternatingRowColors(True)
        self.tbw_Project.resizeColumnsToContents()
        self.tbw_Project.resizeRowsToContents()

    # 采购询价排版：询价记录
    def dTabPurchaseInquiryRec(self):
        self.tbw_Purchase_Inquiry_Rec = QtWidgets.QTableWidget(self.Dtab_Purchase_Inquiry)
        self.tbw_Purchase_Inquiry_Rec.setGeometry(QtCore.QRect(10, 40, 1311, 331))
        self.tbw_Purchase_Inquiry_Rec.setObjectName("tbw_Purchase_Inquiry_Rec")
        self.tbw_Purchase_Inquiry_Rec.setRowCount(0)
        self.tbw_Purchase_Inquiry_Rec.setColumnCount(12)
        self.tbw_Purchase_Inquiry_Rec.setHorizontalHeaderLabels(
            ['询价id','供应商名称', '行业', '规模', '省份', '品牌', '数量', '总价', '单价', '供货周期', '询价日期', '备注'])
        self.label_120 = QtWidgets.QLabel(self.Dtab_Purchase_Inquiry)
        self.label_120.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label_120.setObjectName("label_120")
        self.pbtn_Purchase_Inquiry_Rec_Cancel = QtWidgets.QPushButton(self.Dtab_Purchase_Inquiry)
        self.pbtn_Purchase_Inquiry_Rec_Cancel.setGeometry(QtCore.QRect(960, 10, 88, 23))
        self.pbtn_Purchase_Inquiry_Rec_Cancel.setObjectName("pbtn_Purchase_Inquiry_Rec_Cancel")
        self.pbtn_Purchase_Inquiry_Rec_Update = QtWidgets.QPushButton(self.Dtab_Purchase_Inquiry)
        self.pbtn_Purchase_Inquiry_Rec_Update.setGeometry(QtCore.QRect(1140, 10, 88, 23))
        self.pbtn_Purchase_Inquiry_Rec_Update.setObjectName("pbtn_Purchase_Inquiry_Rec_Update")
        self.pbtn_Purchase_Inquiry_Rec_Delete = QtWidgets.QPushButton(self.Dtab_Purchase_Inquiry)
        self.pbtn_Purchase_Inquiry_Rec_Delete.setGeometry(QtCore.QRect(1230, 10, 88, 23))
        self.pbtn_Purchase_Inquiry_Rec_Delete.setObjectName("pbtn_Purchase_Inquiry_Rec_Delete")
        self.pbtn_Purchase_Inquiry_Rec_Save = QtWidgets.QPushButton(self.Dtab_Purchase_Inquiry)
        self.pbtn_Purchase_Inquiry_Rec_Save.setGeometry(QtCore.QRect(690, 10, 88, 23))
        self.pbtn_Purchase_Inquiry_Rec_Save.setObjectName("pbtn_Purchase_Inquiry_Rec_Save")
        self.pbtn_Purchase_Inquiry_Rec_New = QtWidgets.QPushButton(self.Dtab_Purchase_Inquiry)
        self.pbtn_Purchase_Inquiry_Rec_New.setGeometry(QtCore.QRect(600, 10, 88, 23))
        self.pbtn_Purchase_Inquiry_Rec_New.setObjectName("pbtn_Purchase_Inquiry_Rec_New")
        self.pbtn_Purchase_Inquiry_Rec_Modify = QtWidgets.QPushButton(self.Dtab_Purchase_Inquiry)
        self.pbtn_Purchase_Inquiry_Rec_Modify.setGeometry(QtCore.QRect(1050, 10, 88, 23))
        self.pbtn_Purchase_Inquiry_Rec_Modify.setObjectName("pbtn_Purchase_Inquiry_Rec_Modify")
        self.pbtn_Purchase_Inquiry_Rec_Query = QtWidgets.QPushButton(self.Dtab_Purchase_Inquiry)
        self.pbtn_Purchase_Inquiry_Rec_Query.setGeometry(QtCore.QRect(780, 10, 88, 23))
        self.pbtn_Purchase_Inquiry_Rec_Query.setObjectName("pbtn_Purchase_Inquiry_Rec_Query")
        self.pbtn_Purchase_Inquiry_Rec_Run = QtWidgets.QPushButton(self.Dtab_Purchase_Inquiry)
        self.pbtn_Purchase_Inquiry_Rec_Run.setGeometry(QtCore.QRect(870, 10, 88, 23))
        self.pbtn_Purchase_Inquiry_Rec_Run.setObjectName("pbtn_Purchase_Inquiry_Rec_Run")
        self.pbtn_Purchase_Inquiry_Rec_Cancel.setText("取消")
        self.pbtn_Purchase_Inquiry_Rec_Update.setText("更新")
        self.pbtn_Purchase_Inquiry_Rec_Delete.setText("删除")
        self.pbtn_Purchase_Inquiry_Rec_Save.setText("保存")
        self.pbtn_Purchase_Inquiry_Rec_New.setText("新建")
        self.pbtn_Purchase_Inquiry_Rec_Modify.setText("修改")
        self.pbtn_Purchase_Inquiry_Rec_Query.setText("查询")
        self.pbtn_Purchase_Inquiry_Rec_Run.setText("执行")
        self.label_120.setText("询价记录：")
        self.pbtn_Purchase_Inquiry_Rec_Save.setEnabled(False)
        self.pbtn_Purchase_Inquiry_Rec_Run.setEnabled(False)
        self.pbtn_Purchase_Inquiry_Rec_Update.setEnabled(False)
        self.pbtn_Purchase_Inquiry_Rec_Cancel.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Purchase_Inquiry, "询价记录")
        self.pbtn_Purchase_Inquiry_Rec_New.clicked.connect(self.popup_Purchase_Inquiry_Rec_Show)
        self.popup_purchase_inquiry.pbtn_Save.clicked.connect(self.popup_Purchase_Inquiry_Rec_Save)
        self.popup_purchase_inquiry.pbtn_Cancel.clicked.connect(self.popup_Purchase_Inquiry_Rec_Cancel)
    # 采购询价排版：清单
    def mTabPurchaseInquiry(self):
        self.dTabPurchaseInquiryRec()
        self.tbw_Purchase_Inquiry.setColumnCount(7)
        self.tbw_Purchase_Inquiry.setRowCount(0)
        self.tbw_Purchase_Inquiry.setHorizontalHeaderLabels(
            ['商品id','商品名称', '供应商', '商品品牌', '商品型号', '上市日期', '最近询价日期'])
        self.tbw_Purchase_Inquiry.horizontalHeader().setStretchLastSection(True)

    # 采购计划排版:主页
    def dTabPurchasePlanProd(self):
        self.tbw_Purchase_Plan_Prod = QtWidgets.QTableWidget(self.Dtab_Purchase_Plan)
        self.tbw_Purchase_Plan_Prod.setGeometry(QtCore.QRect(10, 40, 1311, 201))
        self.tbw_Purchase_Plan_Prod.setObjectName("tbw_Purchase_Plan_Prod")
        self.tbw_Purchase_Plan_Prod.setColumnCount(0)
        self.tbw_Purchase_Plan_Prod.setRowCount(0)
        self.tbw_Purchase_Plan_Goods = QtWidgets.QTableWidget(self.Dtab_Purchase_Plan)
        self.tbw_Purchase_Plan_Goods.setGeometry(QtCore.QRect(10, 280, 1311, 151))
        self.tbw_Purchase_Plan_Goods.setObjectName("tbw_Purchase_Plan_Goods")
        self.tbw_Purchase_Plan_Goods.setColumnCount(0)
        self.tbw_Purchase_Plan_Goods.setRowCount(0)
        self.label_118 = QtWidgets.QLabel(self.Dtab_Purchase_Plan)
        self.label_118.setGeometry(QtCore.QRect(30, 10, 81, 16))
        self.label_118.setObjectName("label_118")
        self.label_119 = QtWidgets.QLabel(self.Dtab_Purchase_Plan)
        self.label_119.setGeometry(QtCore.QRect(20, 250, 91, 21))
        self.label_119.setObjectName("label_119")
        self.pbtn_Purchase_Plan_Prod_Delete = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Prod_Delete.setGeometry(QtCore.QRect(1220, 10, 88, 23))
        self.pbtn_Purchase_Plan_Prod_Delete.setObjectName("pbtn_Purchase_Plan_Prod_Delete")
        self.pbtn_Purchase_Plan_Prod_Update = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Prod_Update.setGeometry(QtCore.QRect(1130, 10, 88, 23))
        self.pbtn_Purchase_Plan_Prod_Update.setObjectName("pbtn_Purchase_Plan_Prod_Update")
        self.pbtn_Purchase_Plan_Prod_Modify = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Prod_Modify.setGeometry(QtCore.QRect(1040, 10, 88, 23))
        self.pbtn_Purchase_Plan_Prod_Modify.setObjectName("pbtn_Purchase_Plan_Prod_Modify")
        self.pbtn_Purchase_Plan_Prod_Run = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Prod_Run.setGeometry(QtCore.QRect(860, 10, 88, 23))
        self.pbtn_Purchase_Plan_Prod_Run.setObjectName("pbtn_Purchase_Plan_Prod_Run")
        self.pbtn_Purchase_Plan_Prod_Cancel = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Prod_Cancel.setGeometry(QtCore.QRect(950, 10, 88, 23))
        self.pbtn_Purchase_Plan_Prod_Cancel.setObjectName("pbtn_Purchase_Plan_Prod_Cancel")
        self.pbtn_Purchase_Plan_Prod_New = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Prod_New.setGeometry(QtCore.QRect(590, 10, 88, 23))
        self.pbtn_Purchase_Plan_Prod_New.setObjectName("pbtn_Purchase_Plan_Prod_New")
        self.pbtn_Purchase_Plan_Prod_Query = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Prod_Query.setGeometry(QtCore.QRect(770, 10, 88, 23))
        self.pbtn_Purchase_Plan_Prod_Query.setObjectName("pbtn_Purchase_Plan_Prod_Query")
        self.pbtn_Purchase_Plan_Prod_Save = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Prod_Save.setGeometry(QtCore.QRect(680, 10, 88, 23))
        self.pbtn_Purchase_Plan_Prod_Save.setObjectName("pbtn_Purchase_Plan_Prod_Save")
        self.pbtn_Purchase_Plan_Goods_Delete = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Goods_Delete.setGeometry(QtCore.QRect(1220, 250, 88, 23))
        self.pbtn_Purchase_Plan_Goods_Delete.setObjectName("pbtn_Purchase_Plan_Goods_Delete")
        self.pbtn_Purchase_Plan_Goods_Update = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Goods_Update.setGeometry(QtCore.QRect(1130, 250, 88, 23))
        self.pbtn_Purchase_Plan_Goods_Update.setObjectName("pbtn_Purchase_Plan_Goods_Update")
        self.pbtn_Purchase_Plan_Goods_Modify = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Goods_Modify.setGeometry(QtCore.QRect(1040, 250, 88, 23))
        self.pbtn_Purchase_Plan_Goods_Modify.setObjectName("pbtn_Purchase_Plan_Goods_Modify")
        self.pbtn_Purchase_Plan_Goods_Run = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Goods_Run.setGeometry(QtCore.QRect(860, 250, 88, 23))
        self.pbtn_Purchase_Plan_Goods_Run.setObjectName("pbtn_Purchase_Plan_Goods_Run")
        self.pbtn_Purchase_Plan_Goods_Cancel = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Goods_Cancel.setGeometry(QtCore.QRect(950, 250, 88, 23))
        self.pbtn_Purchase_Plan_Goods_Cancel.setObjectName("pbtn_Purchase_Plan_Goods_Cancel")
        self.pbtn_Purchase_Plan_Goods_New = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Goods_New.setGeometry(QtCore.QRect(590, 250, 88, 23))
        self.pbtn_Purchase_Plan_Goods_New.setObjectName("pbtn_Purchase_Plan_Goods_New")
        self.pbtn_Purchase_Plan_Goods_Query = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Goods_Query.setGeometry(QtCore.QRect(770, 250, 88, 23))
        self.pbtn_Purchase_Plan_Goods_Query.setObjectName("pbtn_Purchase_Plan_Goods_Query")
        self.pbtn_Purchase_Plan_Goods_Save = QtWidgets.QPushButton(self.Dtab_Purchase_Plan)
        self.pbtn_Purchase_Plan_Goods_Save.setGeometry(QtCore.QRect(680, 250, 88, 23))
        self.pbtn_Purchase_Plan_Goods_Save.setObjectName("pbtn_Purchase_Plan_Goods_Save")
        self.tbw_Purchase_Plan_Prod.setColumnCount(7)
        self.tbw_Purchase_Plan_Prod.setHorizontalHeaderLabels(
            ['采购项id', '产品大类', '产品小类', '产品名称', '规格型号','数量', '备注'])
        self.tbw_Purchase_Plan_Prod.horizontalHeader().setStretchLastSection(True)
        self.tbw_Purchase_Plan_Goods.setColumnCount(10)
        self.tbw_Purchase_Plan_Goods.setHorizontalHeaderLabels(
            ['询价id', '供应商名称', '行业', '规模', '品牌', '型号', '上市日期','单价','供货周期','询价日期'])
        self.tbw_Purchase_Plan_Goods.horizontalHeader().setStretchLastSection(True)
        self.tbw_Purchase_Plan_Prod.verticalHeader().setVisible(False)
        self.tbw_Purchase_Plan_Prod.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Plan_Prod.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Plan_Prod.setAlternatingRowColors(True)
        self.tbw_Purchase_Plan_Prod.resizeColumnsToContents()
        self.tbw_Purchase_Plan_Prod.resizeRowsToContents()
        self.tbw_Purchase_Plan_Goods.verticalHeader().setVisible(False)
        self.tbw_Purchase_Plan_Goods.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Plan_Goods.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Plan_Goods.setAlternatingRowColors(True)
        self.tbw_Purchase_Plan_Goods.resizeColumnsToContents()
        self.tbw_Purchase_Plan_Goods.resizeRowsToContents()
        self.label_118.setText("商品清单：")
        self.label_119.setText("供应计划：")
        self.pbtn_Purchase_Plan_Prod_Delete.setText("删除")
        self.pbtn_Purchase_Plan_Prod_Update.setText("更新")
        self.pbtn_Purchase_Plan_Prod_Modify.setText("修改")
        self.pbtn_Purchase_Plan_Prod_Run.setText("执行")
        self.pbtn_Purchase_Plan_Prod_Cancel.setText("取消")
        self.pbtn_Purchase_Plan_Prod_New.setText("新建")
        self.pbtn_Purchase_Plan_Prod_Query.setText("查询")
        self.pbtn_Purchase_Plan_Prod_Save.setText("保存")
        self.pbtn_Purchase_Plan_Goods_Delete.setText("删除")
        self.pbtn_Purchase_Plan_Goods_Update.setText("更新")
        self.pbtn_Purchase_Plan_Goods_Modify.setText("修改")
        self.pbtn_Purchase_Plan_Goods_Run.setText("执行")
        self.pbtn_Purchase_Plan_Goods_Cancel.setText("取消")
        self.pbtn_Purchase_Plan_Goods_New.setText("新建")
        self.pbtn_Purchase_Plan_Goods_Query.setText("查询")
        self.pbtn_Purchase_Plan_Goods_Save.setText("保存")
        self.Tab_Detail.addTab(self.Dtab_Purchase_Plan, "计划内容")
        self.tbw_Purchase_Plan_Prod.itemSelectionChanged.connect(self.click_tbw_Purchase_Plan_Prod)
    # 采购计划排版:主页
    def mTabPurchasePlan(self):
        self.dTabPurchasePlanProd()
        self.tbw_Purchase_Plan.setRowCount(0)
        self.tbw_Purchase_Plan.setColumnCount(9)
        self.tbw_Purchase_Plan.setHorizontalHeaderLabels(
            ['计划id', '项目名称', '计划名称', '甲方', '乙方', '业务负责人', '项目经理','预估采购总额','状态'])
        self.tbw_Purchase_Plan.horizontalHeader().setStretchLastSection(True)
    # 采购计划排版:主页格式
    def mTabPurchasePlanFormat(self):
        self.tbw_Purchase_Plan.verticalHeader().setVisible(False)
        self.tbw_Purchase_Plan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Plan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Plan.setAlternatingRowColors(True)
        self.tbw_Purchase_Plan.resizeColumnsToContents()
        self.tbw_Purchase_Plan.resizeRowsToContents()

    # 采购提醒排版
    def dTabPurchaseNotice(self):
        self.tbw_Purchase_Notice_Purchase = QtWidgets.QTableWidget(self.Dtab_Purchase_Notice)
        self.tbw_Purchase_Notice_Purchase.setGeometry(QtCore.QRect(10, 60, 1311, 331))
        self.tbw_Purchase_Notice_Purchase.setObjectName("tbw_Purchase_Notice_Purchase")
        self.tbw_Purchase_Notice_Purchase.setRowCount(0)
        self.label_117 = QtWidgets.QLabel(self.Dtab_Purchase_Notice)
        self.label_117.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_117.setObjectName("label_117")
        self.label_117.setText("供应列表")
        self.tbw_Purchase_Notice_Purchase.setColumnCount(12)
        self.tbw_Purchase_Notice_Purchase.setHorizontalHeaderLabels(
            ['供应id', '供应商', '行业', '规模', '省份', '品牌', '型号', '询价单价', '询价数量', '总额', '供货周期','询价日期'])
        self.tbw_Purchase_Notice_Purchase.horizontalHeader().setStretchLastSection(True)
        self.tbw_Purchase_Notice_Purchase.verticalHeader().setVisible(False)
        self.tbw_Purchase_Notice_Purchase.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Notice_Purchase.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Notice_Purchase.setAlternatingRowColors(True)
        self.tbw_Purchase_Notice_Purchase.resizeColumnsToContents()
        self.tbw_Purchase_Notice_Purchase.resizeRowsToContents()
        self.pbtn_Purchase_Notice__Purchase_Change = QtWidgets.QPushButton(self.Dtab_Purchase_Notice)
        self.pbtn_Purchase_Notice__Purchase_Change.setGeometry(QtCore.QRect(650, 20, 88, 23))
        self.pbtn_Purchase_Notice__Purchase_Change.setObjectName("pbtn_Purchase_Notice__Purchase_Change")
        self.pbtn_Purchase_Notice__Purchase_Change.setText("修改供应源")
        self.Tab_Detail.addTab(self.Dtab_Purchase_Notice, "采购提醒")
        # 绑定槽函数
        self.pbtn_Purchase_Notice__Purchase_Change.clicked.connect(self.popup_pbtn_Purchase_Notice__Purchase_Change)
    def mTabPurchaseNotice(self):
        self.dTabPurchaseNotice()
        self.tbw_Purchase_Notice.setRowCount(0)
        self.tbw_Purchase_Notice.setColumnCount(13)
        self.tbw_Purchase_Notice.setHorizontalHeaderLabels(
            ['采购项id', '预示来源', '产品名称', '产品型号', '供应商','供应品品牌', '供应品型号','采购数量', '计量单位', '单价','总计','期望交付日期','备注'])
        self.tbw_Purchase_Notice.horizontalHeader().setStretchLastSection(True)
    def mTabPurchaseNoticeFormat(self):
        self.tbw_Purchase_Notice.verticalHeader().setVisible(False)
        self.tbw_Purchase_Notice.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Notice.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Notice.setAlternatingRowColors(True)
        self.tbw_Purchase_Notice.resizeColumnsToContents()
        self.tbw_Purchase_Notice.resizeRowsToContents()
    # 采购询价排版：清单格式
    def mTabPurchaseInquiryFormat(self):
        self.tbw_Purchase_Inquiry.verticalHeader().setVisible(False)
        self.tbw_Purchase_Inquiry.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Inquiry.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Inquiry.setAlternatingRowColors(True)
        self.tbw_Purchase_Inquiry.resizeColumnsToContents()
        self.tbw_Purchase_Inquiry.resizeRowsToContents()
    # 采购任务排版：任务订单
    def dTabPurchaseJobOrder(self):
        self.Dtab_Purchase_Job_Order = QtWidgets.QWidget()
        self.Dtab_Purchase_Job_Order.setObjectName("Dtab_Purchase_Job_Order")
        self.tbw_Purchase_Job_Order = QtWidgets.QTableWidget(self.Dtab_Purchase_Job_Order)
        self.tbw_Purchase_Job_Order.setGeometry(QtCore.QRect(0, 50, 1331, 181))
        self.tbw_Purchase_Job_Order.setObjectName("tbw_Purchase_Job_Order")
        self.tbw_Purchase_Job_Order_Item = QtWidgets.QTableWidget(self.Dtab_Purchase_Job_Order)
        self.tbw_Purchase_Job_Order_Item.setGeometry(QtCore.QRect(0, 270, 1331, 171))
        self.tbw_Purchase_Job_Order_Item.setObjectName("tbw_Purchase_Job_Order_Item")
        self.label_115 = QtWidgets.QLabel(self.Dtab_Purchase_Job_Order)
        self.label_115.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label_115.setObjectName("label_115")
        self.label_116 = QtWidgets.QLabel(self.Dtab_Purchase_Job_Order)
        self.label_116.setGeometry(QtCore.QRect(10, 240, 71, 16))
        self.label_116.setObjectName("label_116")
        self.pbtn_Purchase_Job_Order_Query = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Query.setGeometry(QtCore.QRect(790, 20, 88, 23))
        self.pbtn_Purchase_Job_Order_Query.setObjectName("pbtn_Purchase_Job_Order_Query")
        self.pbtn_Purchase_Job_Order_Cancel = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Cancel.setGeometry(QtCore.QRect(970, 20, 88, 23))
        self.pbtn_Purchase_Job_Order_Cancel.setObjectName("pbtn_Purchase_Job_Order_Cancel")
        self.pbtn_Purchase_Job_Order_Save = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Save.setGeometry(QtCore.QRect(700, 20, 88, 23))
        self.pbtn_Purchase_Job_Order_Save.setObjectName("pbtn_Purchase_Job_Order_Save")
        self.pbtn_Purchase_Job_Order_Update = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Update.setGeometry(QtCore.QRect(1150, 20, 88, 23))
        self.pbtn_Purchase_Job_Order_Update.setObjectName("pbtn_Purchase_Job_Order_Update")
        self.pbtn_Purchase_Job_Order_Delete = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Delete.setGeometry(QtCore.QRect(1240, 20, 88, 23))
        self.pbtn_Purchase_Job_Order_Delete.setObjectName("pbtn_Purchase_Job_Order_Delete")
        self.pbtn_Purchase_Job_Order_Modify = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Modify.setGeometry(QtCore.QRect(1060, 20, 88, 23))
        self.pbtn_Purchase_Job_Order_Modify.setObjectName("pbtn_Purchase_Job_Order_Modify")
        self.pbtn_Purchase_Job_Order_Run = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Run.setGeometry(QtCore.QRect(880, 20, 88, 23))
        self.pbtn_Purchase_Job_Order_Run.setObjectName("pbtn_Purchase_Job_Order_Run")
        self.pbtn_Purchase_Job_Order_New = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_New.setGeometry(QtCore.QRect(610, 20, 88, 23))
        self.pbtn_Purchase_Job_Order_New.setObjectName("pbtn_Purchase_Job_Order_New")
        self.pbtn_Purchase_Job_Order_Item_Query = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Item_Query.setGeometry(QtCore.QRect(790, 240, 88, 23))
        self.pbtn_Purchase_Job_Order_Item_Query.setObjectName("pbtn_Purchase_Job_Order_Item_Query")
        self.pbtn_Purchase_Job_Order_Item_Cancel = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Item_Cancel.setGeometry(QtCore.QRect(970, 240, 88, 23))
        self.pbtn_Purchase_Job_Order_Item_Cancel.setObjectName("pbtn_Purchase_Job_Order_Item_Cancel")
        self.pbtn_Purchase_Job_Order_Item_Save = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Item_Save.setGeometry(QtCore.QRect(700, 240, 88, 23))
        self.pbtn_Purchase_Job_Order_Item_Save.setObjectName("pbtn_Purchase_Job_Order_Item_Save")
        self.pbtn_Purchase_Job_Order_Item_Update = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Item_Update.setGeometry(QtCore.QRect(1150, 240, 88, 23))
        self.pbtn_Purchase_Job_Order_Item_Update.setObjectName("pbtn_Purchase_Job_Order_Item_Update")
        self.pbtn_Purchase_Job_Order_Item_Delete = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Item_Delete.setGeometry(QtCore.QRect(1240, 240, 88, 23))
        self.pbtn_Purchase_Job_Order_Item_Delete.setObjectName("pbtn_Purchase_Job_Order_Item_Delete")
        self.pbtn_Purchase_Job_Order_Item_Modify = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Item_Modify.setGeometry(QtCore.QRect(1060, 240, 88, 23))
        self.pbtn_Purchase_Job_Order_Item_Modify.setObjectName("pbtn_Purchase_Job_Order_Item_Modify")
        self.pbtn_Purchase_Job_Order_Item_Run = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Item_Run.setGeometry(QtCore.QRect(880, 240, 88, 23))
        self.pbtn_Purchase_Job_Order_Item_Run.setObjectName("pbtn_Purchase_Job_Order_Item_Run")
        self.pbtn_Purchase_Job_Order_Item_New = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Order)
        self.pbtn_Purchase_Job_Order_Item_New.setGeometry(QtCore.QRect(610, 240, 88, 23))
        self.pbtn_Purchase_Job_Order_Item_New.setObjectName("pbtn_Purchase_Job_Order_Item_New")
        self.tbw_Purchase_Job_Order.setColumnCount(6)
        self.tbw_Purchase_Job_Order.setRowCount(0)
        self.tbw_Purchase_Job_Order.setHorizontalHeaderLabels(['订单id', '订单类型', '订单时间', '订单金额', '收货地址', '项目名称'])
        self.tbw_Purchase_Job_Order.horizontalHeader().setStretchLastSection(True)
        self.tbw_Purchase_Job_Order.verticalHeader().setVisible(False)
        self.tbw_Purchase_Job_Order.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Job_Order.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Job_Order.setAlternatingRowColors(True)
        self.tbw_Purchase_Job_Order.resizeColumnsToContents()
        self.tbw_Purchase_Job_Order.resizeRowsToContents()
        self.tbw_Purchase_Job_Order_Item.setColumnCount(8)
        self.tbw_Purchase_Job_Order_Item.setRowCount(0)
        self.tbw_Purchase_Job_Order_Item.setHorizontalHeaderLabels(['订单项id', '产品名称', '型号', '数量', '单位', '单价', '总额', '备注'])
        self.tbw_Purchase_Job_Order_Item.horizontalHeader().setStretchLastSection(True)
        self.tbw_Purchase_Job_Order_Item.verticalHeader().setVisible(False)
        self.tbw_Purchase_Job_Order_Item.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Job_Order_Item.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Job_Order_Item.setAlternatingRowColors(True)
        self.tbw_Purchase_Job_Order_Item.resizeColumnsToContents()
        self.tbw_Purchase_Job_Order_Item.resizeRowsToContents()
        self.label_115.setText("订单：")
        self.label_116.setText("订单项：")
        self.pbtn_Purchase_Job_Order_Query.setText("查询")
        self.pbtn_Purchase_Job_Order_Cancel.setText("取消")
        self.pbtn_Purchase_Job_Order_Save.setText("保存")
        self.pbtn_Purchase_Job_Order_Update.setText("更新")
        self.pbtn_Purchase_Job_Order_Delete.setText("删除")
        self.pbtn_Purchase_Job_Order_Modify.setText("修改")
        self.pbtn_Purchase_Job_Order_Run.setText("执行")
        self.pbtn_Purchase_Job_Order_New.setText("新建")
        self.pbtn_Purchase_Job_Order_Item_Query.setText("查询")
        self.pbtn_Purchase_Job_Order_Item_Cancel.setText("取消")
        self.pbtn_Purchase_Job_Order_Item_Save.setText("保存")
        self.pbtn_Purchase_Job_Order_Item_Update.setText("更新")
        self.pbtn_Purchase_Job_Order_Item_Delete.setText("删除")
        self.pbtn_Purchase_Job_Order_Item_Modify.setText("修改")
        self.pbtn_Purchase_Job_Order_Item_Run.setText("执行")
        self.pbtn_Purchase_Job_Order_Item_New.setText("新建")
        self.Tab_Detail.addTab(self.Dtab_Purchase_Job_Order, "采购订单")
        self.pbtn_Purchase_Job_Order_New.clicked.connect(self.popup_Purchase_Job_Order_New)
        self.popup_purchase_job_order.pbtn_Pick.clicked.connect(self.popup_Purchase_Job_Order_Save)
        self.popup_purchase_job_order.pbtn_Quit.clicked.connect(self.popup_Purchase_Job_Order_Quit)
        self.pbtn_Purchase_Job_Order_Item_New.clicked.connect(self.popup_Purchase_Job_Order_Item_New)
        self.popup_purchase_job_order_item.pbtn_Pick.clicked.connect(self.popup_Purchase_Job_Order_Item_Save)
        self.popup_purchase_job_order_item.pbtn_Quit.clicked.connect(self.popup_Purchase_Job_Order_Item_Quit)
        # 采购项清单
        self.tbw_Purchase_Job_Order.itemSelectionChanged.connect(self.click_tbw_Purchase_Job_Order)
    # 采购任务排版：任务合同
    def dTabPurchaseJobContract(self):
        self.Dtab_Purchase_Job_Contract = QtWidgets.QWidget()
        self.Dtab_Purchase_Job_Contract.setObjectName("Dtab_Purchase_Job_Contract")
        self.tbw_Purchase_Job_Contract = QtWidgets.QTableWidget(self.Dtab_Purchase_Job_Contract)
        self.tbw_Purchase_Job_Contract.setGeometry(QtCore.QRect(10, 40, 1311, 291))
        self.tbw_Purchase_Job_Contract.setObjectName("tbw_Purchase_Job_Contract")
        self.tbw_Purchase_Job_Contract.setRowCount(0)
        self.tbw_Purchase_Job_Contract.setColumnCount(7)
        self.tbw_Purchase_Job_Contract.setHorizontalHeaderLabels(
            ['合同id', '合同编号', '合同名称', '甲方客户', '乙方客户', '合同金额', '合同状态'])
        self.tbw_Purchase_Job_Contract.horizontalHeader().setStretchLastSection(True)
        self.pbtn_Purchase_Job_Contract_Query = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Contract)
        self.pbtn_Purchase_Job_Contract_Query.setGeometry(QtCore.QRect(780, 10, 88, 23))
        self.pbtn_Purchase_Job_Contract_Query.setObjectName("pbtn_Purchase_Job_Contract_Query")
        self.pbtn_Purchase_Job_Contract_Cancel = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Contract)
        self.pbtn_Purchase_Job_Contract_Cancel.setGeometry(QtCore.QRect(960, 10, 88, 23))
        self.pbtn_Purchase_Job_Contract_Cancel.setObjectName("pbtn_Purchase_Job_Contract_Cancel")
        self.pbtn_Purchase_Job_Contract_Save = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Contract)
        self.pbtn_Purchase_Job_Contract_Save.setGeometry(QtCore.QRect(690, 10, 88, 23))
        self.pbtn_Purchase_Job_Contract_Save.setObjectName("pbtn_Purchase_Job_Contract_Save")
        self.pbtn_Purchase_Job_Contract_Update = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Contract)
        self.pbtn_Purchase_Job_Contract_Update.setGeometry(QtCore.QRect(1140, 10, 88, 23))
        self.pbtn_Purchase_Job_Contract_Update.setObjectName("pbtn_Purchase_Job_Contract_Update")
        self.pbtn_Purchase_Job_Contract_Delete = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Contract)
        self.pbtn_Purchase_Job_Contract_Delete.setGeometry(QtCore.QRect(1230, 10, 88, 23))
        self.pbtn_Purchase_Job_Contract_Delete.setObjectName("pbtn_Purchase_Job_Contract_Delete")
        self.pbtn_Purchase_Job_Contract_Modify = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Contract)
        self.pbtn_Purchase_Job_Contract_Modify.setGeometry(QtCore.QRect(1050, 10, 88, 23))
        self.pbtn_Purchase_Job_Contract_Modify.setObjectName("pbtn_Purchase_Job_Contract_Modify")
        self.pbtn_Purchase_Job_Contract_Run = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Contract)
        self.pbtn_Purchase_Job_Contract_Run.setGeometry(QtCore.QRect(870, 10, 88, 23))
        self.pbtn_Purchase_Job_Contract_Run.setObjectName("pbtn_Purchase_Job_Contract_Run")
        self.pbtn_Purchase_Job_Contract_New = QtWidgets.QPushButton(self.Dtab_Purchase_Job_Contract)
        self.pbtn_Purchase_Job_Contract_New.setGeometry(QtCore.QRect(600, 10, 88, 23))
        self.pbtn_Purchase_Job_Contract_New.setObjectName("pbtn_Purchase_Job_Contract_New")
        self.pbtn_Purchase_Job_Contract_Query.setText("查询")
        self.pbtn_Purchase_Job_Contract_Cancel.setText("取消")
        self.pbtn_Purchase_Job_Contract_Save.setText("保存")
        self.pbtn_Purchase_Job_Contract_Update.setText("更新")
        self.pbtn_Purchase_Job_Contract_Delete.setText("删除")
        self.pbtn_Purchase_Job_Contract_Modify.setText("修改")
        self.pbtn_Purchase_Job_Contract_Run.setText("执行")
        self.pbtn_Purchase_Job_Contract_New.setText("新建")
        self.pbtn_Purchase_Job_Contract_Query.setEnabled(False)
        self.pbtn_Purchase_Job_Contract_Cancel.setEnabled(False)
        self.pbtn_Purchase_Job_Contract_Save.setEnabled(False)
        self.pbtn_Purchase_Job_Contract_Update.setEnabled(False)
        self.pbtn_Purchase_Job_Contract_Delete.setEnabled(False)
        self.pbtn_Purchase_Job_Contract_Modify.setEnabled(False)
        self.pbtn_Purchase_Job_Contract_Run.setEnabled(False)
        self.pbtn_Purchase_Job_Contract_New.setEnabled(True)
        self.Tab_Detail.addTab(self.Dtab_Purchase_Job_Contract, "采购合同")
        self.pbtn_Purchase_Job_Contract_New.clicked.connect(self.popup_Purchase_Job_Contract_Show)
        self.popup_purchase_job_contract.pbtn_Save.clicked.connect(self.popup_Purchase_Job_Contract_Save)
        self.popup_purchase_job_contract.pbtn_Cancel.clicked.connect(self.popup_Purchase_Job_Contract_Cancel)
    # 采购任务排版：任务项目
    def dTabPurchaseJobProject(self):
        self.Dtab_Purchase_Job_Project = QtWidgets.QWidget()
        self.Dtab_Purchase_Job_Project.setObjectName("Dtab_Purchase_Job_Project")
        self.tbw_Purchase_Job_Project = QtWidgets.QTableWidget(self.Dtab_Purchase_Job_Project)
        self.tbw_Purchase_Job_Project.setGeometry(QtCore.QRect(10, 20, 1331, 381))
        self.tbw_Purchase_Job_Project.setObjectName("tbw_Purchase_Job_Project")
        self.tbw_Purchase_Job_Project.setColumnCount(16)
        self.tbw_Purchase_Job_Project.setRowCount(0)
        self.tbw_Purchase_Job_Project.setHorizontalHeaderLabels(['项目id', '项目编号', '项目名称', '甲方', '乙方', '业务负责人', '项目经理', '合同款', '保证金', '采购预算费用', '采购发生比例',
             '工程预算费用', '工程发生比例', '业务费用', '毛利润', '毛利率'])
        self.tbw_Purchase_Job_Project.horizontalHeader().setStretchLastSection(True)
        self.tbw_Purchase_Job_Project.verticalHeader().setVisible(False)
        self.tbw_Purchase_Job_Project.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Job_Project.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Job_Project.setAlternatingRowColors(True)
        self.tbw_Purchase_Job_Project.resizeColumnsToContents()
        self.tbw_Purchase_Job_Project.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Purchase_Job_Project, "采购项目")
    # 采购任务排版：主页
    def mTabPurchaseJob(self):
        self.dTabPurchaseJobOrder()
        self.dTabPurchaseJobContract()
        self.dTabPurchaseJobProject()
        self.tbw_Purchase_Job.setRowCount(0)
        self.tbw_Purchase_Job.setColumnCount(7)
        self.tbw_Purchase_Job.setHorizontalHeaderLabels(
            ['采购id', '采购编号','采购名称', '供应商', '建立时间', '状态', '采购员'])
        self.tbw_Purchase_Job.horizontalHeader().setStretchLastSection(True)
        self.popup_purchase_job.pbtn_Purchase_Job_Save.clicked.connect(self.popup_Purchase_Job_Save)
        self.popup_purchase_job.pbtn_Purchase_Job_Cancel.clicked.connect(self.popup_aPurchase_Job_Cancel)
        self.pbtn_Purchase_Job_New.clicked.connect(self.popup_Purchase_Job_Show)
    # 采购任务排版：主页格式
    def mTabPurchaseJobFormat(self):
        self.tbw_Purchase_Job.verticalHeader().setVisible(False)
        self.tbw_Purchase_Job.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Job.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Job.setAlternatingRowColors(True)
        self.tbw_Purchase_Job.resizeColumnsToContents()
        self.tbw_Purchase_Job.resizeRowsToContents()

    # 采购任务排版
    def dTabPurchasePayment_Invoice(self):
        self.Dtab_Purchase_Payment = QtWidgets.QWidget()
        self.Dtab_Purchase_Payment.setObjectName("Dtab_Purchase_Payment")
        self.tbw_Purchase_Payment_Invoice = QtWidgets.QTableWidget(self.Dtab_Purchase_Payment)
        self.tbw_Purchase_Payment_Invoice.setGeometry(QtCore.QRect(10, 40, 1321, 361))
        self.tbw_Purchase_Payment_Invoice.setObjectName("tbw_Purchase_Payment_Invoice")
        self.tbw_Purchase_Payment_Invoice.setColumnCount(0)
        self.tbw_Purchase_Payment_Invoice.setRowCount(0)
        self.pbtn_Purchase_Payment_Invoice_New = QtWidgets.QPushButton(self.Dtab_Purchase_Payment)
        self.pbtn_Purchase_Payment_Invoice_New.setGeometry(QtCore.QRect(600, 10, 88, 23))
        self.pbtn_Purchase_Payment_Invoice_New.setObjectName("pbtn_Purchase_Payment_Invoice_New")
        self.pbtn_Purchase_Payment_Invoice_Save = QtWidgets.QPushButton(self.Dtab_Purchase_Payment)
        self.pbtn_Purchase_Payment_Invoice_Save.setGeometry(QtCore.QRect(690, 10, 88, 23))
        self.pbtn_Purchase_Payment_Invoice_Save.setObjectName("pbtn_Purchase_Payment_Invoice_Save")
        self.pbtn_Purchase_Payment_Invoice_Cancel = QtWidgets.QPushButton(self.Dtab_Purchase_Payment)
        self.pbtn_Purchase_Payment_Invoice_Cancel.setGeometry(QtCore.QRect(960, 10, 88, 23))
        self.pbtn_Purchase_Payment_Invoice_Cancel.setObjectName("pbtn_Purchase_Payment_Invoice_Cancel")
        self.pbtn_Purchase_Payment_Invoice_Run = QtWidgets.QPushButton(self.Dtab_Purchase_Payment)
        self.pbtn_Purchase_Payment_Invoice_Run.setGeometry(QtCore.QRect(870, 10, 88, 23))
        self.pbtn_Purchase_Payment_Invoice_Run.setObjectName("pbtn_Purchase_Payment_Invoice_Run")
        self.pbtn_Purchase_Payment_Invoice_Modify = QtWidgets.QPushButton(self.Dtab_Purchase_Payment)
        self.pbtn_Purchase_Payment_Invoice_Modify.setGeometry(QtCore.QRect(1050, 10, 88, 23))
        self.pbtn_Purchase_Payment_Invoice_Modify.setObjectName("pbtn_Purchase_Payment_Invoice_Modify")
        self.pbtn_Purchase_Payment_Invoice_Update = QtWidgets.QPushButton(self.Dtab_Purchase_Payment)
        self.pbtn_Purchase_Payment_Invoice_Update.setGeometry(QtCore.QRect(1140, 10, 88, 23))
        self.pbtn_Purchase_Payment_Invoice_Update.setObjectName("pbtn_Purchase_Payment_Invoice_Update")
        self.pbtn_Purchase_Payment_Invoice_Delete = QtWidgets.QPushButton(self.Dtab_Purchase_Payment)
        self.pbtn_Purchase_Payment_Invoice_Delete.setGeometry(QtCore.QRect(1230, 10, 88, 23))
        self.pbtn_Purchase_Payment_Invoice_Delete.setObjectName("pbtn_Purchase_Payment_Invoice_Delete")
        self.pbtn_Purchase_Payment_Invoice_Query = QtWidgets.QPushButton(self.Dtab_Purchase_Payment)
        self.pbtn_Purchase_Payment_Invoice_Query.setGeometry(QtCore.QRect(780, 10, 88, 23))
        self.pbtn_Purchase_Payment_Invoice_Query.setObjectName("pbtn_Purchase_Payment_Invoice_Query")
        self.pbtn_Purchase_Payment_Invoice_New.setText("新建")
        self.pbtn_Purchase_Payment_Invoice_Save.setText("保存")
        self.pbtn_Purchase_Payment_Invoice_Cancel.setText("取消")
        self.pbtn_Purchase_Payment_Invoice_Run.setText("执行")
        self.pbtn_Purchase_Payment_Invoice_Modify.setText("修改")
        self.pbtn_Purchase_Payment_Invoice_Update.setText("更新")
        self.pbtn_Purchase_Payment_Invoice_Delete.setText("删除")
        self.pbtn_Purchase_Payment_Invoice_Query.setText("查询")
        self.tbw_Purchase_Payment_Invoice.setColumnCount(8)
        self.tbw_Purchase_Payment_Invoice.setHorizontalHeaderLabels(
            ['支款单id', '支款日期', '支款原因', '支款金额(含税)', '支款部门', '支款人', '支款方式', '支票号'])
        self.Tab_Detail.addTab(self.Dtab_Purchase_Payment, "支付单关联")
        # 绑定槽函数
        self.pbtn_Purchase_Payment_Invoice_New.clicked.connect(self.click_pbtn_Purchase_Payment_Invoice_New)
        self.popup_m_pay_invc.pbtn_Save.clicked.connect(self.click_pbtn_Purchase_Payment_Invoice_Save)
        self.popup_m_pay_invc.pbtn_Cancel.clicked.connect(self.click_pbtn_Purchase_Payment_Invoice_Cancel)
    def mTabPurchasePayment(self):
        self.dTabPurchasePayment_Invoice()
        self.tbw_Purchase_Payment.setRowCount(0)
        self.tbw_Purchase_Payment.setColumnCount(9)
        self.tbw_Purchase_Payment.setHorizontalHeaderLabels(
            ['发票id', '回票日期', '开票日期', '发票号码', '价税合计', '税率', '票兑余额', '销售方', '购买方'])
        self.tbw_Purchase_Payment.horizontalHeader().setStretchLastSection(True)
        self.pbtn_tbw_Purchase_Payment_New.clicked.connect(self.click_pbtn_tbw_Purchase_Payment_New)
        self.popup_invoice.pbtn_Save.clicked.connect(self.click_pbtn_tbw_Purchase_Payment_Save)
        self.popup_invoice.pbtn_Cancel.clicked.connect(self.click_pbtn_tbw_Purchase_Payment_Cancel)
    def mTabPurchasePaymentFormat(self):
        self.tbw_Purchase_Payment.verticalHeader().setVisible(False)
        self.tbw_Purchase_Payment.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Purchase_Payment.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Purchase_Payment.setAlternatingRowColors(True)
        self.tbw_Purchase_Payment.resizeColumnsToContents()
        self.tbw_Purchase_Payment.resizeRowsToContents()

    # 内容排版：详细页签（供应商详情）
    def dTabSuppiler(self):
        self.Dtab_Supppiler = QtWidgets.QWidget()
        self.Dtab_Supppiler.setObjectName("Dtab_Supppiler")
        self.lb_Supppiler_OrgCode = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_OrgCode.setGeometry(QtCore.QRect(300, 160, 101, 16))
        self.lb_Supppiler_OrgCode.setObjectName("lb_Supppiler_OrgCode")
        self.lb_Supppiler_Level = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Level.setGeometry(QtCore.QRect(50, 210, 81, 21))
        self.lb_Supppiler_Level.setObjectName("lb_Supppiler_Level")
        self.lb_Supppiler_CreateDT = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_CreateDT.setGeometry(QtCore.QRect(60, 300, 71, 16))
        self.lb_Supppiler_CreateDT.setObjectName("lb_Supppiler_CreateDT")
        self.lb_Supppiler_LevelDT = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_LevelDT.setGeometry(QtCore.QRect(60, 260, 81, 21))
        self.lb_Supppiler_LevelDT.setObjectName("lb_Supppiler_LevelDT")
        self.lb_Supppiler_Tax = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Tax.setGeometry(QtCore.QRect(40, 160, 101, 21))
        self.lb_Supppiler_Tax.setObjectName("lb_Supppiler_Tax")
        self.lb_Supppiler_Payed = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Payed.setGeometry(QtCore.QRect(300, 260, 81, 16))
        self.lb_Supppiler_Payed.setObjectName("lb_Supppiler_Payed")
        self.lb_Supppiler_Amount = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Amount.setGeometry(QtCore.QRect(300, 210, 81, 16))
        self.lb_Supppiler_Amount.setObjectName("lb_Supppiler_Amount")
        self.lb_Supppiler_UnPayPct = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_UnPayPct.setGeometry(QtCore.QRect(300, 300, 91, 21))
        self.lb_Supppiler_UnPayPct.setObjectName("lb_Supppiler_UnPayPct")
        self.lEdit_Supppiler_BusinessNo = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_BusinessNo.setGeometry(QtCore.QRect(410, 160, 113, 20))
        self.lEdit_Supppiler_BusinessNo.setObjectName("lEdit_Supppiler_BusinessNo")
        self.lEdit_Supppiler_Level = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_Level.setGeometry(QtCore.QRect(170, 210, 113, 20))
        self.lEdit_Supppiler_Level.setObjectName("lEdit_Supppiler_Level")
        self.lEdit_Supppiler_FstDT = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_FstDT.setGeometry(QtCore.QRect(170, 300, 113, 20))
        self.lEdit_Supppiler_FstDT.setObjectName("lEdit_Supppiler_FstDT")
        self.lEdit_Supppiler_CheckDT = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_CheckDT.setGeometry(QtCore.QRect(170, 260, 113, 20))
        self.lEdit_Supppiler_CheckDT.setObjectName("lEdit_Supppiler_CheckDT")
        self.lEdit_Supppiler_TaxNo = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_TaxNo.setGeometry(QtCore.QRect(170, 160, 113, 20))
        self.lEdit_Supppiler_TaxNo.setObjectName("lEdit_Supppiler_TaxNo")
        self.lEdit_Supppiler_Amount = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_Amount.setGeometry(QtCore.QRect(410, 210, 113, 20))
        self.lEdit_Supppiler_Amount.setObjectName("lEdit_Supppiler_Amount")
        self.lEdit_Supppiler_Pay = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_Pay.setGeometry(QtCore.QRect(410, 260, 113, 20))
        self.lEdit_Supppiler_Pay.setObjectName("lEdit_Supppiler_Pay")
        self.lEdit_Supppiler_unPayPct = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_unPayPct.setGeometry(QtCore.QRect(410, 300, 113, 20))
        self.lEdit_Supppiler_unPayPct.setObjectName("lEdit_Supppiler_unPayPct")
        self.pbtn_Supppiler_Query = QtWidgets.QPushButton(self.Dtab_Supppiler)
        self.pbtn_Supppiler_Query.setGeometry(QtCore.QRect(770, 10, 88, 23))
        self.pbtn_Supppiler_Query.setObjectName("pbtn_Supppiler_Query")
        self.pbtn_Supppiler_Cancel = QtWidgets.QPushButton(self.Dtab_Supppiler)
        self.pbtn_Supppiler_Cancel.setGeometry(QtCore.QRect(950, 10, 88, 23))
        self.pbtn_Supppiler_Cancel.setObjectName("pbtn_Supppiler_Cancel")
        self.pbtn_Supppiler_Save = QtWidgets.QPushButton(self.Dtab_Supppiler)
        self.pbtn_Supppiler_Save.setGeometry(QtCore.QRect(680, 10, 88, 23))
        self.pbtn_Supppiler_Save.setObjectName("pbtn_Supppiler_Save")
        self.pbtn_Supppiler_Update = QtWidgets.QPushButton(self.Dtab_Supppiler)
        self.pbtn_Supppiler_Update.setGeometry(QtCore.QRect(1130, 10, 88, 23))
        self.pbtn_Supppiler_Update.setObjectName("pbtn_Supppiler_Update")
        self.pbtn_Supppiler_Delete = QtWidgets.QPushButton(self.Dtab_Supppiler)
        self.pbtn_Supppiler_Delete.setGeometry(QtCore.QRect(1220, 10, 88, 23))
        self.pbtn_Supppiler_Delete.setObjectName("pbtn_Supppiler_Delete")
        self.pbtn_Supppiler_Modify = QtWidgets.QPushButton(self.Dtab_Supppiler)
        self.pbtn_Supppiler_Modify.setGeometry(QtCore.QRect(1040, 10, 88, 23))
        self.pbtn_Supppiler_Modify.setObjectName("pbtn_Supppiler_Modify")
        self.pbtn_Supppiler_Run = QtWidgets.QPushButton(self.Dtab_Supppiler)
        self.pbtn_Supppiler_Run.setGeometry(QtCore.QRect(860, 10, 88, 23))
        self.pbtn_Supppiler_Run.setObjectName("pbtn_Supppiler_Run")
        self.pbtn_Supppiler_New = QtWidgets.QPushButton(self.Dtab_Supppiler)
        self.pbtn_Supppiler_New.setGeometry(QtCore.QRect(590, 10, 88, 23))
        self.pbtn_Supppiler_New.setObjectName("pbtn_Supppiler_New")
        self.lEdit_Supppiler_Name = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_Name.setGeometry(QtCore.QRect(170, 60, 321, 21))
        self.lEdit_Supppiler_Name.setObjectName("lEdit_Supppiler_Name")
        self.lb_Supppiler_Name = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Name.setGeometry(QtCore.QRect(50, 60, 91, 16))
        self.lb_Supppiler_Name.setObjectName("lb_Supppiler_Name")
        self.lb_Supppiler_Scale = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Scale.setGeometry(QtCore.QRect(570, 160, 61, 21))
        self.lb_Supppiler_Scale.setObjectName("lb_Supppiler_Scale")
        self.lEdit_Supppiler_Scale = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_Scale.setGeometry(QtCore.QRect(660, 160, 113, 20))
        self.lEdit_Supppiler_Scale.setObjectName("lEdit_Supppiler_Scale")
        self.lb_Supppiler_Place = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Place.setGeometry(QtCore.QRect(570, 110, 61, 21))
        self.lb_Supppiler_Place.setObjectName("lb_Supppiler_Place")
        self.lb_Supppiler_Type = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Type.setGeometry(QtCore.QRect(60, 110, 71, 16))
        self.lb_Supppiler_Type.setObjectName("lb_Supppiler_Type")
        self.lEdit_Supppiler_Industry = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_Industry.setGeometry(QtCore.QRect(410, 110, 113, 20))
        self.lEdit_Supppiler_Industry.setObjectName("lEdit_Supppiler_Industry")
        self.lb_Supppiler_Industry = QtWidgets.QLabel(self.Dtab_Supppiler)
        self.lb_Supppiler_Industry.setGeometry(QtCore.QRect(320, 110, 61, 21))
        self.lb_Supppiler_Industry.setObjectName("lb_Supppiler_Industry")
        self.lEdit_Supppiler_Place = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_Place.setGeometry(QtCore.QRect(660, 110, 113, 20))
        self.lEdit_Supppiler_Place.setObjectName("lEdit_Supppiler_Place")
        self.lEdit_Supppiler_Type = QtWidgets.QLineEdit(self.Dtab_Supppiler)
        self.lEdit_Supppiler_Type.setGeometry(QtCore.QRect(170, 110, 113, 20))
        self.lEdit_Supppiler_Type.setObjectName("lEdit_Supppiler_Type")
        self.lb_Supppiler_OrgCode.setText("统一信用编码")
        self.lb_Supppiler_Level.setText("供应商级别")
        self.lb_Supppiler_CreateDT.setText("初供日期")
        self.lb_Supppiler_LevelDT.setText("评审日期")
        self.lb_Supppiler_Tax.setText("纳税人识别号")
        self.lb_Supppiler_Payed.setText("已付金额")
        self.lb_Supppiler_Amount.setText("合同总额")
        self.lb_Supppiler_UnPayPct.setText("未付款比例")
        self.pbtn_Supppiler_Query.setText("查询")
        self.pbtn_Supppiler_Cancel.setText("取消")
        self.pbtn_Supppiler_Save.setText("保存")
        self.pbtn_Supppiler_Update.setText("更新")
        self.pbtn_Supppiler_Delete.setText("删除")
        self.pbtn_Supppiler_Modify.setText("修改")
        self.pbtn_Supppiler_Run.setText("执行")
        self.pbtn_Supppiler_New.setText("新建")
        self.lb_Supppiler_Name.setText("供应商名称")
        self.lb_Supppiler_Scale.setText("规模")
        self.lb_Supppiler_Place.setText("省份")
        self.lb_Supppiler_Type.setText("客户类型")
        self.lb_Supppiler_Industry.setText("行业")
        self.pbtn_Supppiler_Query.setEnabled(True)
        self.pbtn_Supppiler_Cancel.setEnabled(False)
        self.pbtn_Supppiler_Save.setEnabled(False)
        self.pbtn_Supppiler_Update.setEnabled(False)
        self.pbtn_Supppiler_Delete.setEnabled(True)
        self.pbtn_Supppiler_Modify.setEnabled(True)
        self.pbtn_Supppiler_Run.setEnabled(False)
        self.pbtn_Supppiler_New.setEnabled(True)
        self.lEdit_Supppiler_BusinessNo.setEnabled(False)
        self.lEdit_Supppiler_TaxNo.setEnabled(False)
        self.lEdit_Supppiler_Level.setEnabled(False)
        self.lEdit_Supppiler_Amount.setEnabled(False)
        self.lEdit_Supppiler_FstDT.setEnabled(False)
        self.lEdit_Supppiler_Pay.setEnabled(False)
        self.lEdit_Supppiler_CheckDT.setEnabled(False)
        self.lEdit_Supppiler_unPayPct.setEnabled(False)
        self.lEdit_Supppiler_Name.setEnabled(False)
        self.lEdit_Supppiler_Scale.setEnabled(False)
        self.lEdit_Supppiler_Place.setEnabled(False)
        self.lEdit_Supppiler_Type.setEnabled(False)
        self.lEdit_Supppiler_Industry.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Supppiler, "供应商详情")
        # 绑定槽函数
        self.pbtn_Supppiler_New.clicked.connect(self.click_pbtn_Supppiler_New)
        self.pbtn_Supppiler_Save.clicked.connect(self.click_pbtn_Supppiler_Save)
        self.pbtn_Supppiler_Cancel.clicked.connect(self.click_pbtn_Supppiler_Cancel)
    # 内容排版：详细页签（供应商采购合同）
    def dTabSuppilerContract(self):
        self.Dtab_Supppiler_Contract = QtWidgets.QWidget()
        self.Dtab_Supppiler_Contract.setObjectName("Dtab_Supppiler_Contract")
        self.tbw_Supppiler_Contract = QtWidgets.QTableWidget(self.Dtab_Supppiler_Contract)
        self.tbw_Supppiler_Contract.setGeometry(QtCore.QRect(0, 10, 1341, 351))
        self.tbw_Supppiler_Contract.setObjectName("tbw_Supppiler_Contract")
        self.tbw_Supppiler_Contract.setColumnCount(7)
        self.tbw_Supppiler_Contract.setRowCount(0)
        self.tbw_Supppiler_Contract.setHorizontalHeaderLabels(['合同id', '合同编号', '合同名称', '甲方', '乙方', '合同金额', '采购人'])
        self.tbw_Supppiler_Contract.horizontalHeader().setStretchLastSection(True)
        self.tbw_Supppiler_Contract.verticalHeader().setVisible(False)
        self.tbw_Supppiler_Contract.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Supppiler_Contract.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Supppiler_Contract.setAlternatingRowColors(True)
        self.tbw_Supppiler_Contract.resizeColumnsToContents()
        self.tbw_Supppiler_Contract.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Supppiler_Contract, "供应商合同")
    # 内容排版：详细页签（供应商项目）
    def dTabSuppilerProject(self):
        self.Dtab_Supppiler_Project = QtWidgets.QWidget()
        self.Dtab_Supppiler_Project.setObjectName("Dtab_Supppiler_Project")
        self.tbw_Supppiler_Project = QtWidgets.QTableWidget(self.Dtab_Supppiler_Project)
        self.tbw_Supppiler_Project.setGeometry(QtCore.QRect(20, 10, 1321, 361))
        self.tbw_Supppiler_Project.setObjectName("tbw_Supppiler_Project")
        self.tbw_Supppiler_Project.setColumnCount(6)
        self.tbw_Supppiler_Project.setRowCount(0)
        self.tbw_Supppiler_Project.setHorizontalHeaderLabels(['项目id', '项目名称', '项目经理', '项目合同编号', '业务负责人', '项目经理'])
        self.tbw_Supppiler_Project.horizontalHeader().setStretchLastSection(True)
        self.tbw_Supppiler_Project.verticalHeader().setVisible(False)
        self.tbw_Supppiler_Project.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Supppiler_Project.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Supppiler_Project.setAlternatingRowColors(True)
        self.tbw_Supppiler_Project.resizeColumnsToContents()
        self.tbw_Supppiler_Project.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Supppiler_Project, "供应商项目")
    # 内容排版：详细页签（供应商联系人）
    def dTabSuppilerContact(self):
        self.Dtab_Supppiler_Contact = QtWidgets.QWidget()
        self.Dtab_Supppiler_Contact.setObjectName("Dtab_Supppiler_Contact")
        self.tbw_Supppiler_Contact = QtWidgets.QTableWidget(self.Dtab_Supppiler_Contact)
        self.tbw_Supppiler_Contact.setGeometry(QtCore.QRect(10, 10, 1331, 381))
        self.tbw_Supppiler_Contact.setObjectName("tbw_Supppiler_Contact")
        self.tbw_Supppiler_Contact.setColumnCount(7)
        self.tbw_Supppiler_Contact.setRowCount(0)
        self.tbw_Supppiler_Contact.setHorizontalHeaderLabels(['联系人id', '姓名', '部门', '职位', '好感度', '年龄', '手机', '邮件'])
        self.tbw_Supppiler_Contact.horizontalHeader().setStretchLastSection(True)
        self.tbw_Supppiler_Contact.verticalHeader().setVisible(False)
        self.tbw_Supppiler_Contact.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Supppiler_Contact.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Supppiler_Contact.setAlternatingRowColors(True)
        self.tbw_Supppiler_Contact.resizeColumnsToContents()
        self.tbw_Supppiler_Contact.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Supppiler_Contact, "供应商干系人")
    # 内容排版：主页签（供应商）
    def mTabSuppiler(self):
        self.dTabSuppiler()
        self.dTabSuppilerContract()
        self.dTabSuppilerProject()
        self.dTabSuppilerContact()
        self.tbw_Supppiler.setRowCount(0)
        self.tbw_Supppiler.setColumnCount(7)
        self.tbw_Supppiler.setHorizontalHeaderLabels(
            ['供应商id', '供应商名称', '行业', '规模', '省份', '合同总额', '未付金额'])
        self.tbw_Supppiler.horizontalHeader().setStretchLastSection(True)
    def mTabSuppilerFormat(self):
        self.tbw_Supppiler.verticalHeader().setVisible(False)
        self.tbw_Supppiler.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Supppiler.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Supppiler.setAlternatingRowColors(True)
        self.tbw_Supppiler.resizeColumnsToContents()
        self.tbw_Supppiler.resizeRowsToContents()

    # 内容排版：详细页签（产品详情）
    def dTabProduct(self):
        self.Dtab_Product = QtWidgets.QWidget()
        self.Dtab_Product.setObjectName("Dtab_Product")
        self.lEdit_Prod_No = QtWidgets.QLineEdit(self.Dtab_Product)
        self.lEdit_Prod_No.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.lEdit_Prod_No.setObjectName("lEdit_Prod_No")
        self.label_106 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_106.setGeometry(QtCore.QRect(30, 30, 71, 21))
        self.label_106.setObjectName("label_106")
        self.label_106.setText("产品编号：")
        self.label_107 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_107.setGeometry(QtCore.QRect(30, 90, 71, 21))
        self.label_107.setObjectName("label_107")
        self.label_107.setText("产品大类：")
        self.cBox_Prod_TypeA = QtWidgets.QComboBox(self.Dtab_Product)
        self.cBox_Prod_TypeA.setGeometry(QtCore.QRect(130, 90, 87, 22))
        self.cBox_Prod_TypeA.setObjectName("cBox_Prod_TypeA")
        self.lEdit_Prod_TypeName = QtWidgets.QLineEdit(self.Dtab_Product)
        self.lEdit_Prod_TypeName.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.lEdit_Prod_TypeName.setObjectName("lEdit_Prod_TypeName")
        self.label_108 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_108.setGeometry(QtCore.QRect(30, 140, 71, 21))
        self.label_108.setObjectName("label_108")
        self.label_108.setText("规格型号：")
        self.lEdit_Prod_TechStandard = QtWidgets.QLineEdit(self.Dtab_Product)
        self.lEdit_Prod_TechStandard.setGeometry(QtCore.QRect(120, 190, 113, 20))
        self.lEdit_Prod_TechStandard.setObjectName("lEdit_Prod_TechStandard")
        self.label_109 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_109.setGeometry(QtCore.QRect(30, 190, 71, 21))
        self.label_109.setObjectName("label_109")
        self.label_109.setText("技术标准")
        self.lEdit_Prod_Name = QtWidgets.QLineEdit(self.Dtab_Product)
        self.lEdit_Prod_Name.setGeometry(QtCore.QRect(400, 30, 113, 20))
        self.lEdit_Prod_Name.setObjectName("lEdit_Prod_Name")
        self.label_110 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_110.setGeometry(QtCore.QRect(310, 30, 71, 21))
        self.label_110.setObjectName("label_110")
        self.label_110.setText("产品名称")
        self.label_111 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_111.setGeometry(QtCore.QRect(310, 90, 71, 21))
        self.label_111.setObjectName("label_111")
        self.label_111.setText("产品小类")
        self.cBox_Prod_TypeB = QtWidgets.QComboBox(self.Dtab_Product)
        self.cBox_Prod_TypeB.setGeometry(QtCore.QRect(400, 90, 87, 22))
        self.cBox_Prod_TypeB.setObjectName("cBox_Prod_TypeB")
        self.label_112 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_112.setGeometry(QtCore.QRect(310, 140, 71, 21))
        self.label_112.setObjectName("label_112")
        self.label_112.setText("国产/进口")
        self.lEdit_Prod_Unit = QtWidgets.QLineEdit(self.Dtab_Product)
        self.lEdit_Prod_Unit.setGeometry(QtCore.QRect(400, 190, 113, 20))
        self.lEdit_Prod_Unit.setObjectName("lEdit_Prod_Unit")
        self.label_113 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_113.setGeometry(QtCore.QRect(300, 190, 71, 21))
        self.label_113.setObjectName("label_113")
        self.label_113.setText("计量单位")
        self.tbw_Product_parameter = QtWidgets.QTableWidget(self.Dtab_Product)
        self.tbw_Product_parameter.setGeometry(QtCore.QRect(10, 260, 1291, 141))
        self.tbw_Product_parameter.setObjectName("tbw_Product_parameter")
        self.tbw_Product_parameter.setColumnCount(4)
        self.tbw_Product_parameter.setRowCount(0)
        self.tbw_Product_parameter.setHorizontalHeaderLabels(['参数','条件', '值', '备注'])
        self.tbw_Product_parameter.horizontalHeader().setStretchLastSection(True)
        self.tbw_Product_parameter.verticalHeader().setVisible(False)
        self.tbw_Product_parameter.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Product_parameter.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Product_parameter.setAlternatingRowColors(True)
        self.tbw_Product_parameter.resizeColumnsToContents()
        self.tbw_Product_parameter.resizeRowsToContents()
        self.label_114 = QtWidgets.QLabel(self.Dtab_Product)
        self.label_114.setGeometry(QtCore.QRect(20, 240, 150, 18))
        self.label_114.setObjectName("label_114")
        self.label_114.setText("备注&限定参数清单")
        self.pbtn_Product_Query = QtWidgets.QPushButton(self.Dtab_Product)
        self.pbtn_Product_Query.setGeometry(QtCore.QRect(780, 10, 88, 23))
        self.pbtn_Product_Query.setObjectName("pbtn_Product_Query")
        self.pbtn_Product_Cancel = QtWidgets.QPushButton(self.Dtab_Product)
        self.pbtn_Product_Cancel.setGeometry(QtCore.QRect(960, 10, 88, 23))
        self.pbtn_Product_Cancel.setObjectName("pbtn_Product_Cancel")
        self.pbtn_Product_Save = QtWidgets.QPushButton(self.Dtab_Product)
        self.pbtn_Product_Save.setGeometry(QtCore.QRect(690, 10, 88, 23))
        self.pbtn_Product_Save.setObjectName("pbtn_Product_Save")
        self.pbtn_Product_Update = QtWidgets.QPushButton(self.Dtab_Product)
        self.pbtn_Product_Update.setGeometry(QtCore.QRect(1140, 10, 88, 23))
        self.pbtn_Product_Update.setObjectName("pbtn_Product_Update")
        self.pbtn_Product_Delete = QtWidgets.QPushButton(self.Dtab_Product)
        self.pbtn_Product_Delete.setGeometry(QtCore.QRect(1230, 10, 88, 23))
        self.pbtn_Product_Delete.setObjectName("pbtn_Product_Delete")
        self.pbtn_Product_Modify = QtWidgets.QPushButton(self.Dtab_Product)
        self.pbtn_Product_Modify.setGeometry(QtCore.QRect(1050, 10, 88, 23))
        self.pbtn_Product_Modify.setObjectName("pbtn_Product_Modify")
        self.pbtn_Product_Run = QtWidgets.QPushButton(self.Dtab_Product)
        self.pbtn_Product_Run.setGeometry(QtCore.QRect(870, 10, 88, 23))
        self.pbtn_Product_Run.setObjectName("pbtn_Product_Run")
        self.pbtn_Product_New = QtWidgets.QPushButton(self.Dtab_Product)
        self.pbtn_Product_New.setGeometry(QtCore.QRect(600, 10, 88, 23))
        self.pbtn_Product_New.setObjectName("pbtn_Product_New")
        self.cBox_Prod_Origin = QtWidgets.QComboBox(self.Dtab_Product)
        self.cBox_Prod_Origin.setGeometry(QtCore.QRect(550, 140, 87, 22))
        self.cBox_Prod_Origin.setObjectName("cBox_Prod_Origin")
        self.pbtn_Product_Query.setText("查询")
        self.pbtn_Product_Cancel.setText("取消")
        self.pbtn_Product_Save.setText("保存")
        self.pbtn_Product_Update.setText("更新")
        self.pbtn_Product_Delete.setText("删除")
        self.pbtn_Product_Modify.setText("修改")
        self.pbtn_Product_Run.setText("执行")
        self.pbtn_Product_New.setText("新建")
        self.pbtn_Product_Query.setVisible(True)
        self.pbtn_Product_Cancel.setVisible(False)
        self.pbtn_Product_Save.setVisible(False)
        self.pbtn_Product_Update.setVisible(False)
        self.pbtn_Product_Delete.setVisible(True)
        self.pbtn_Product_Modify.setVisible(True)
        self.pbtn_Product_Run.setVisible(False)
        self.pbtn_Product_New.setVisible(True)
        self.lEdit_Prod_No.setEnabled(False)
        self.lEdit_Prod_Name.setEnabled(False)
        self.lEdit_Prod_TypeName.setEnabled(False)
        self.cBox_Prod_Origin.setEnabled(False)
        self.lEdit_Prod_TechStandard.setEnabled(False)
        self.lEdit_Prod_Unit.setEnabled(False)
        self.cBox_Prod_TypeA.setEnabled(False)
        self.cBox_Prod_TypeB.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Product, "产品详情")
        # 绑定槽函数
        self.pbtn_Product_New.clicked.connect(self.click_pbtn_Product_New)
        self.pbtn_Product_Save.clicked.connect(self.click_pbtn_Product_Save)
        self.pbtn_Product_Cancel.clicked.connect(self.click_pbtn_Product_Cancel)
        self.cBox_Prod_TypeA.activated.connect(self.click_cBox_Prod_TypeA)
    # 内容排版：详细页签（产品供应）
    def dTabProductGoods(self):
        self.Dtab_Product_Goods = QtWidgets.QWidget()
        self.Dtab_Product_Goods.setObjectName("Dtab_Product_Goods")
        self.tbw_Product_Goods = QtWidgets.QTableWidget(self.Dtab_Product_Goods)
        self.tbw_Product_Goods.setGeometry(QtCore.QRect(0, 40, 1331, 311))
        self.tbw_Product_Goods.setObjectName("tbw_Product_Goods")
        self.pbtn_Product_Goods_Query = QtWidgets.QPushButton(self.Dtab_Product_Goods)
        self.pbtn_Product_Goods_Query.setGeometry(QtCore.QRect(790, 10, 88, 23))
        self.pbtn_Product_Goods_Query.setObjectName("pbtn_Product_Goods_Query")
        self.pbtn_Product_Goods_New = QtWidgets.QPushButton(self.Dtab_Product_Goods)
        self.pbtn_Product_Goods_New.setGeometry(QtCore.QRect(610, 10, 88, 23))
        self.pbtn_Product_Goods_New.setObjectName("pbtn_Product_Goods_New")
        self.pbtn_Product_Goods_Modify = QtWidgets.QPushButton(self.Dtab_Product_Goods)
        self.pbtn_Product_Goods_Modify.setGeometry(QtCore.QRect(1060, 10, 88, 23))
        self.pbtn_Product_Goods_Modify.setObjectName("pbtn_Product_Goods_Modify")
        self.pbtn_Product_Goods_Run = QtWidgets.QPushButton(self.Dtab_Product_Goods)
        self.pbtn_Product_Goods_Run.setGeometry(QtCore.QRect(880, 10, 88, 23))
        self.pbtn_Product_Goods_Run.setObjectName("pbtn_Product_Goods_Run")
        self.pbtn_Product_Goods_Cancel = QtWidgets.QPushButton(self.Dtab_Product_Goods)
        self.pbtn_Product_Goods_Cancel.setGeometry(QtCore.QRect(970, 10, 88, 23))
        self.pbtn_Product_Goods_Cancel.setObjectName("pbtn_Product_Goods_Cancel")
        self.pbtn_Product_Goods_Delete = QtWidgets.QPushButton(self.Dtab_Product_Goods)
        self.pbtn_Product_Goods_Delete.setGeometry(QtCore.QRect(1240, 10, 88, 23))
        self.pbtn_Product_Goods_Delete.setObjectName("pbtn_Product_Goods_Delete")
        self.pbtn_Product_Goods_Save = QtWidgets.QPushButton(self.Dtab_Product_Goods)
        self.pbtn_Product_Goods_Save.setGeometry(QtCore.QRect(700, 10, 88, 23))
        self.pbtn_Product_Goods_Save.setObjectName("pbtn_Product_Goods_Save")
        self.pbtn_Product_Goods_Update = QtWidgets.QPushButton(self.Dtab_Product_Goods)
        self.pbtn_Product_Goods_Update.setGeometry(QtCore.QRect(1150, 10, 88, 23))
        self.pbtn_Product_Goods_Update.setObjectName("pbtn_Product_Goods_Update")
        self.tbw_Product_Goods.setColumnCount(10)
        self.tbw_Product_Goods.setRowCount(0)
        self.tbw_Product_Goods.setHorizontalHeaderLabels(['供应品id', '供应商名称', '行业', '规模', '品牌', '型号', '上市日期', '价格' , '供货周期','最近询价日期'])
        self.tbw_Product_Goods.horizontalHeader().setStretchLastSection(True)
        self.tbw_Product_Goods.verticalHeader().setVisible(False)
        self.tbw_Product_Goods.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Product_Goods.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Product_Goods.setAlternatingRowColors(True)
        self.tbw_Product_Goods.resizeColumnsToContents()
        self.tbw_Product_Goods.resizeRowsToContents()
        self.pbtn_Product_Goods_Query.setText("查询")
        self.pbtn_Product_Goods_New.setText("新建")
        self.pbtn_Product_Goods_Modify.setText("修改")
        self.pbtn_Product_Goods_Run.setText("执行")
        self.pbtn_Product_Goods_Cancel.setText("取消")
        self.pbtn_Product_Goods_Delete.setText("删除")
        self.pbtn_Product_Goods_Save.setText("保存")
        self.pbtn_Product_Goods_Update.setText("更新")
        self.pbtn_Product_Goods_Run.setEnabled(False)
        self.pbtn_Product_Goods_Cancel.setEnabled(False)
        self.pbtn_Product_Goods_Save.setEnabled(False)
        self.pbtn_Product_Goods_Update.setEnabled(False)
        self.Tab_Detail.addTab(self.Dtab_Product_Goods, "产品供应品")
        self.pbtn_Product_Goods_New.clicked.connect(self.popup_Goods_Show)
        self.popup_goods.pbtn_Save.clicked.connect(self.popup_Goods_Save)
        self.popup_goods.pbtn_Cancel.clicked.connect(self.popup_Goods_Cancel)
    # 内容排版：详细页签（产品历史报价）
    def dTabProductHisPrice(self):
        self.Dtab_Product_HisPrice = QtWidgets.QWidget()
        self.Dtab_Product_HisPrice.setObjectName("Dtab_Product_HisPrice")
        self.tbw_Product_HisPrice = QtWidgets.QTableWidget(self.Dtab_Product_HisPrice)
        self.tbw_Product_HisPrice.setGeometry(QtCore.QRect(10, 20, 1331, 411))
        self.tbw_Product_HisPrice.setObjectName("tbw_Product_HisPrice")
        self.tbw_Product_HisPrice.setColumnCount(12)
        self.tbw_Product_HisPrice.setRowCount(0)
        self.tbw_Product_HisPrice.setHorizontalHeaderLabels(['报价id', '供应商名称', '行业', '规模', '省份', '品牌', '数量','价格', '单个均价','供货周期', '报价日期', '是否采买'])
        self.tbw_Product_HisPrice.horizontalHeader().setStretchLastSection(True)
        self.tbw_Product_HisPrice.verticalHeader().setVisible(False)
        self.tbw_Product_HisPrice.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Product_HisPrice.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Product_HisPrice.setAlternatingRowColors(True)
        self.tbw_Product_HisPrice.resizeColumnsToContents()
        self.tbw_Product_HisPrice.resizeRowsToContents()
        self.Tab_Detail.addTab(self.Dtab_Product_HisPrice, "产品历史报价")
    # 内容排版：主页签（产品）
    def mTabProduct(self):
        self.dTabProduct()
        self.dTabProductGoods()
        self.dTabProductHisPrice()
        self.tbw_Product.setRowCount(0)
        self.tbw_Product.setColumnCount(6)
        self.tbw_Product.setHorizontalHeaderLabels(
            ['产品id', '产品大类', '产品小类', '产品名称', '规格型号', '国产/进口'])
        self.tbw_Supppiler.horizontalHeader().setStretchLastSection(True)
    def mTabProductFormat(self):
        self.tbw_Product.verticalHeader().setVisible(False)
        self.tbw_Product.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbw_Product.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbw_Product.setAlternatingRowColors(True)
        self.tbw_Product.resizeColumnsToContents()
        self.tbw_Product.resizeRowsToContents()

    # 槽函数：客户相关
    def click_pbtn_CreateAccount(self):
        # 按钮变化
        self.pbtnCreateAccount.setEnabled(False)
        self.pbtnQueryAccount.setEnabled(False)
        self.pbtnDeleteAccount.setEnabled(False)
        self.pbtnModifyAccount.setEnabled(False)
        self.pbtnCommitAccount.setEnabled(True)
        self.pbtnCancelAccount.setEnabled(True)
        # 客户显示置空
        self.tbw_Account.setRowCount(0)
        self.lEdit_Acnt_Type.setText("")
        self.lEdit_Acnt_Total.setText("")
        self.lEdit_Acnt_unReturn.setText("")
        self.lEdit_Acnt_OrgCode.setText("")
        self.lEdit_Acnt_Return.setText("")
        self.lEdit_Acnt_unReturnPst.setText("")
        self.lEdit_Account_Name.setText("")
        self.lEdit_Acnt_tax.setText("")
        self.lEdit_Acnt_Industry.setText("")
        self.lEdit_Acnt_Scale.setText("")
        self.lEdit_Acnt_Place.setText("")
        # 打开文本框编辑
        self.lEdit_Acnt_Type.setEnabled(True)
        self.lEdit_Acnt_OrgCode.setEnabled(True)
        self.lEdit_Account_Name.setEnabled(True)
        self.lEdit_Acnt_tax.setEnabled(True)
        self.lEdit_Acnt_Industry.setEnabled(True)
        self.lEdit_Acnt_Scale.setEnabled(True)
        self.lEdit_Acnt_Place.setEnabled(True)
    def click_pbtn_ModifyAccount(self):
        # 按钮变化
        self.pbtnCreateAccount.setEnabled(False)
        self.pbtnQueryAccount.setEnabled(False)
        self.pbtnDeleteAccount.setEnabled(False)
        self.pbtnModifyAccount.setEnabled(False)
        self.pbtnCommitModifyAccount.setEnabled(True)
        self.pbtnCancelAccount.setEnabled(True)
        # 打开文本框编辑
        self.lEdit_Acnt_Type.setEnabled(True)
        self.lEdit_Acnt_OrgCode.setEnabled(True)
        self.lEdit_Account_Name.setEnabled(True)
    def click_pbtn_ModifyCommitAccount(self):
        AcntType = self.lEdit_Acnt_Type.text().strip()
        AcntOrgCode = self.lEdit_Acnt_OrgCode.text().strip()
        AcntName = self.lEdit_Account_Name.text().strip()
        row_index = self.tbw_Account.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            if AcntType == '' or AcntOrgCode == '' or AcntName == '':
                QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
            else:
                select_id = self.tbw_Account.item(row_index, 0).text()
                result = dbExec("update `S_ACCOUNT` set `Name` = %s ,`Business_license_No` = %s ,`Industry`  = %s where `id` = %s",(AcntName,AcntOrgCode,AcntType,select_id))
                if result > 0:
                    self.mTabChange(0)
                else:
                    QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_DeleteAccount(self):
        row_index = self.tbw_Account.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Account.item(row_index, 0).text()
            result = dbExec("update `S_ACCOUNT` set `Active_Flg` = 'N' where `id` = %s",(select_id))
            if result > 0:
                self.mTabChange(0)
            else:
                QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_QueryAccount(self):
        # 按钮变化
        self.pbtnCreateAccount.setEnabled(False)
        self.pbtnQueryAccount.setEnabled(False)
        self.pbtnDeleteAccount.setEnabled(False)
        self.pbtnModifyAccount.setEnabled(False)
        self.pbtnQueryRunAccount.setEnabled(True)
        self.pbtnCancelAccount.setEnabled(True)
        # 客户显示置空
        self.tbw_Account.setRowCount(0)
        self.lEdit_Acnt_Type.setText("")
        self.lEdit_Acnt_Total.setText("")
        self.lEdit_Acnt_unReturn.setText("")
        self.lEdit_Acnt_OrgCode.setText("")
        self.lEdit_Acnt_Return.setText("")
        self.lEdit_Acnt_unReturnPst.setText("")
        self.lEdit_Account_Name.setText("")
        # 打开文本框编辑
        self.lEdit_Account_Name.setEnabled(True)
    def click_pbtn_QueryRunAccount(self):
        AcntName = self.lEdit_Account_Name.text().strip()
        if AcntName == '':
            QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            # 绑定数据
            result = dbQueryFull(
                "select id,Name,Industry,Scale,Place,Business_license_No,Tax_No,Level from S_ACCOUNT where id != 0 and Active_Flg = 'Y' and Custmoer_Flg = 'Y' and Name like '%" + AcntName + "%'")
            row = len(result)
            vol = self.tbw_Account.columnCount()
            self.tbw_Account.setRowCount(row)
            if row >0 :
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Account.setItem(fi, fj, data)
                self.tbw_Account.selectRow(0)
            # 按钮变化
            self.pbtnCreateAccount.setEnabled(True)
            self.pbtnQueryAccount.setEnabled(True)
            self.pbtnDeleteAccount.setEnabled(True)
            self.pbtnModifyAccount.setEnabled(True)
            self.pbtnQueryRunAccount.setEnabled(False)
            self.pbtnCancelAccount.setEnabled(False)
            # 打开文本框编辑
            self.lEdit_Account_Name.setEnabled(False)
    def click_pbtn_CommitAccount(self):
        AcntType = self.lEdit_Acnt_Type.text().strip()
        AcntOrgCode = self.lEdit_Acnt_OrgCode.text().strip()
        AcntName = self.lEdit_Account_Name.text().strip()
        AcntTax = self.lEdit_Acnt_tax.text().strip()
        AcntIndustry = self.lEdit_Acnt_Industry.text().strip()
        AcntScale = self.lEdit_Acnt_Scale.text().strip()
        AcntPlace = self.lEdit_Acnt_Place.text().strip()
        if AcntType == '' or AcntOrgCode == '' or AcntName == '' or AcntTax == '' or AcntIndustry == '' or AcntScale == '' or AcntPlace == '':
            QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            result = dbExec("insert into `S_ACCOUNT` (`Name`,`Business_license_No`,`Industry`, Scale, Place, Tax_No, Type, Level,Custmoer_Flg) " +
                            " values(%s,%s,%s,%s,%s,%s,%s,60,'Y')",(AcntName,AcntOrgCode,AcntIndustry,AcntScale,AcntPlace,AcntTax,AcntType))
            if result >0 :
                dbCommit("COMMIT")
                self.mTabChange(0)
            else:
                QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_CancelAccount(self):
        # 按钮变化
        self.pbtnCreateAccount.setEnabled(True)
        self.pbtnQueryAccount.setEnabled(True)
        self.pbtnDeleteAccount.setEnabled(True)
        self.pbtnModifyAccount.setEnabled(True)
        self.pbtnCommitAccount.setEnabled(False)
        self.pbtnCancelAccount.setEnabled(False)
        # 客户显示置空
        self.tbw_Account.setRowCount(0)
        self.lEdit_Acnt_Type.setText("")
        self.lEdit_Acnt_Total.setText("")
        self.lEdit_Acnt_unReturn.setText("")
        self.lEdit_Acnt_OrgCode.setText("")
        self.lEdit_Acnt_Return.setText("")
        self.lEdit_Acnt_unReturnPst.setText("")
        self.lEdit_Account_Name.setText("")
        # 打开文本框编辑
        self.lEdit_Acnt_Type.setEnabled(False)
        self.lEdit_Acnt_OrgCode.setEnabled(False)
        self.lEdit_Account_Name.setEnabled(False)
        # 返回原界面
        self.mTabChange(0)

    # 槽函数：联系人相关
    def click_pbtn_CreateContact(self):
        # 按钮变化
        self.pbtnCreateContact.setEnabled(False)
        self.pbtnQueryContact.setEnabled(False)
        self.pbtnDeleteContact.setEnabled(False)
        self.pbtnModifyContact.setEnabled(False)
        self.pbtnCommitContact.setEnabled(True)
        self.pbtnCancelContact.setEnabled(True)
        self.pbtn_PopUP_Account.setEnabled(True)
        # 客户显示置空
        self.tbw_Contact.setRowCount(0)
        self.lEdit_Cnt_Org.setText("")
        self.lEdit_Cnt_Dept.setText("")
        self.lEdit_Cnt_Rank.setText("")
        self.lEdit_Cnt_BirtyDay.setText("")
        self.lEdit_Cnt_Phone.setText("")
        self.lEdit_Cnt_Address.setText("")
        self.lEdit_Cnt_FstName.setText("")
        self.lEdit_Cnt_LstName.setText("")
        self.lEdit_Cnt_Postion.setText("")
        self.lEdit_Cnt_Sex.setText("")
        self.lEdit_Cnt_Character.setText("")
        self.lEdit_Cnt_Email.setText("")
        # 打开文本框编辑
        self.lEdit_Cnt_FstName.setEnabled(True)
        self.lEdit_Cnt_LstName.setEnabled(True)
        self.lEdit_Cnt_Phone.setEnabled(True)
        self.lEdit_Cnt_Org.setEnabled(True)
        # 设置pick变量为空
        globalvar.pick_account_id = ''
    def click_pbtn_CommitContact(self):
        CntFstName = self.lEdit_Cnt_FstName.text().strip()
        CntLstName = self.lEdit_Cnt_LstName.text().strip()
        CntPhone = self.lEdit_Cnt_Phone.text().strip()
        CntOrg = self.lEdit_Cnt_Org.text().strip()
        if CntFstName == '' or CntLstName == '' or CntPhone == '' or CntOrg == '':
            QMessageBox.warning(None, '警告', '请输入完整数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            if globalvar.pick_account_id == '' :
                QMessageBox.warning(None, '警告', '所属组织必须使用窗口选择，不可自行输入！', QMessageBox.Ok)
            else:
                result = dbExec("insert into S_CONTACT (Fst_Name, Lst_Name, Phone,Account_id) values (%s,%s,%s,%s);",(CntFstName,CntLstName,CntPhone,globalvar.pick_account_id))
                if result >0 :
                    self.mTabChange(1)
                else:
                    QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_ModifyContact(self):
        # 按钮变化
        self.pbtnCreateContact.setEnabled(False)
        self.pbtnQueryContact.setEnabled(False)
        self.pbtnDeleteContact.setEnabled(False)
        self.pbtnModifyContact.setEnabled(False)
        self.pbtnModifyCommitContact.setEnabled(True)
        self.pbtnCancelContact.setEnabled(True)
        # 打开文本框编辑
        self.lEdit_Cnt_FstName.setEnabled(True)
        self.lEdit_Cnt_LstName.setEnabled(True)
        self.lEdit_Cnt_Phone.setEnabled(True)
    def click_pbtn_ModifyCommitContact(self):
        CntFstName = self.lEdit_Cnt_FstName.text().strip()
        CntLstName = self.lEdit_Cnt_LstName.text().strip()
        CntPhone = self.lEdit_Cnt_Phone.text().strip()
        row_index = self.tbw_Contact.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            if CntFstName == '' or CntLstName == '' or CntPhone == '':
                QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
            else:
                select_id = self.tbw_Contact.item(row_index, 0).text()
                result = dbExec("update S_CONTACT set `Fst_Name` = %s ,`Lst_Name` = %s ,`Phone`  = %s where `id` = %s",(CntFstName,CntLstName,CntPhone,select_id))
                if result > 0:
                    self.mTabChange(1)
                else:
                    QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_DeleteContact(self):
        row_index = self.tbw_Contact.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Contact.item(row_index, 0).text()
            result = dbExec("update S_CONTACT set `Active_Flg` = 'N' where `id` = %s",(select_id))
            if result > 0:
                self.mTabChange(1)
            else:
                QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_QueryContact(self):
        # 按钮变化
        self.pbtnCreateContact.setEnabled(False)
        self.pbtnQueryContact.setEnabled(False)
        self.pbtnDeleteContact.setEnabled(False)
        self.pbtnModifyContact.setEnabled(False)
        self.pbtnQueryRunContact.setEnabled(True)
        self.pbtnCancelContact.setEnabled(True)
        # 客户显示置空
        # 客户显示置空
        self.tbw_Contact.setRowCount(0)
        self.lEdit_Cnt_Org.setText("")
        self.lEdit_Cnt_Dept.setText("")
        self.lEdit_Cnt_Rank.setText("")
        self.lEdit_Cnt_BirtyDay.setText("")
        self.lEdit_Cnt_Phone.setText("")
        self.lEdit_Cnt_Address.setText("")
        self.lEdit_Cnt_FstName.setText("")
        self.lEdit_Cnt_LstName.setText("")
        self.lEdit_Cnt_Postion.setText("")
        self.lEdit_Cnt_Sex.setText("")
        self.lEdit_Cnt_Character.setText("")
        self.lEdit_Cnt_Email.setText("")
        # 打开文本框编辑
        self.lEdit_Cnt_Phone.setEnabled(True)
        self.lEdit_Cnt_Org.setEnabled(False)
        self.lEdit_Cnt_Dept.setEnabled(False)
        self.lEdit_Cnt_Rank.setEnabled(False)
        self.lEdit_Cnt_BirtyDay.setEnabled(False)
        self.lEdit_Cnt_Address.setEnabled(False)
        self.lEdit_Cnt_FstName.setEnabled(False)
        self.lEdit_Cnt_LstName.setEnabled(False)
        self.lEdit_Cnt_Postion.setEnabled(False)
        self.lEdit_Cnt_Sex.setEnabled(False)
        self.lEdit_Cnt_Character.setEnabled(False)
        self.lEdit_Cnt_Email.setEnabled(False)
    def click_pbtn_QueryRunContact(self):
        CntPhone = self.lEdit_Cnt_Phone.text().strip()
        if CntPhone == '':
            QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            # 绑定数据
            result = dbQueryFull("""select t1.id, t2.`Name`, CONCAT(t1.Fst_Name,t1.Lst_Name) "full_name",  '' as "department", '' as "position"  , 
                                    '' as sup_num, '' as age , '18612345678' as phone , '123@123.com' as mail
                                    from S_CONTACT t1 LEFT JOIN S_ACCOUNT t2 on t1.Account_id = t2.id where t1.Active_Flg = 'Y' and t1.Phone like '%""" + CntPhone + "%'")
            row = len(result)
            vol = self.tbw_Contact.columnCount()
            self.tbw_Contact.setRowCount(row)
            if row >0 :
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Contact.setItem(fi, fj, data)
                self.tbw_Contact.selectRow(0)
            # 按钮变化
            self.pbtnCreateContact.setEnabled(True)
            self.pbtnQueryContact.setEnabled(True)
            self.pbtnDeleteContact.setEnabled(True)
            self.pbtnModifyContact.setEnabled(True)
            self.pbtnQueryRunContact.setEnabled(False)
            self.pbtnCancelContact.setEnabled(False)
            # 打开文本框编辑
            self.lEdit_Cnt_Phone.setEnabled(False)
    def click_pbtn_CancelContact(self):
        # 按钮变化
        self.pbtnCreateContact.setEnabled(True)
        self.pbtnQueryContact.setEnabled(True)
        self.pbtnDeleteContact.setEnabled(True)
        self.pbtnModifyContact.setEnabled(True)
        self.pbtnCommitContact.setEnabled(False)
        self.pbtnCancelContact.setEnabled(False)
        # 客户显示置空
        self.tbw_Contact.setRowCount(0)
        self.lEdit_Cnt_Org.setText("")
        self.lEdit_Cnt_Dept.setText("")
        self.lEdit_Cnt_Rank.setText("")
        self.lEdit_Cnt_BirtyDay.setText("")
        self.lEdit_Cnt_Phone.setText("")
        self.lEdit_Cnt_Address.setText("")
        self.lEdit_Cnt_FstName.setText("")
        self.lEdit_Cnt_LstName.setText("")
        self.lEdit_Cnt_Postion.setText("")
        self.lEdit_Cnt_Sex.setText("")
        self.lEdit_Cnt_Character.setText("")
        self.lEdit_Cnt_Email.setText("")
        # 关闭文本框编辑
        self.lEdit_Cnt_FstName.setEnabled(False)
        self.lEdit_Cnt_LstName.setEnabled(False)
        self.lEdit_Cnt_Phone.setEnabled(False)
        # 返回原界面
        self.mTabChange(1)
    # 槽函数：客户popup相关
    def click_pbtn_PopUpAccount(self):
        popup_Account.popup_show(self,self.popup_account)
    def popup_account_click_pbtn_pick(self):
        popup_Account.popup_pick(self,self.popup_account)
        if globalvar.pick_account_id != '' :
            result = dbQuery("select Name from S_ACCOUNT where id = %s",globalvar.pick_account_id)
            self.lEdit_Cnt_Org.setText(str(result[0][0]))
    def popup_account_click_pbtn_quit(self):
        popup_Account.popup_quit(self,self.popup_account)

    # 槽函数：项目
    def click_pbtn_CreateProject(self):
        # 按钮变化
        self.pbtnCancelProject.setEnabled(True)
        self.pbtnCommitProject.setEnabled(True)
        self.pbtnNewProject.setEnabled(False)
        self.pbtnQueryProject.setEnabled(False)
        self.pbtnModifyProject.setEnabled(False)
        self.pbtnDeleteProject.setEnabled(False)
        self.pbtn_PopUP_PjtPartyA.setEnabled(True)
        self.pbtn_PopUP_PjtPartyB.setEnabled(True)
        # 文本框内容置空
        self.lEdit_Project_No.setText("")
        self.lEdit_Project_PartyA.setText("")
        self.lEdit_Project_BL.setText("")
        self.lEdit_Project_Amount.setText("")
        self.lEdit_Project_Name.setText("")
        self.lEdit_Project_PartyB.setText("")
        self.lEdit_Project_PM.setText("")
        self.lEdit_Project_UnPayPrc.setText("")
        self.lEdit_Project_Purchase_Est.setText("")
        self.lEdit_Project_Const_Est.setText("")
        self.lEdit_Project_Bsns_Est.setText("")
        self.lEdit_Project_Oth_Est.setText("")
        self.lEdit_Project_GP_Est.setText("")
        self.lEdit_Project_GPct_Est.setText("")
        self.lEdit_Project_Purchase_Done.setText("")
        self.lEdit_Project_Const_Done.setText("")
        self.lEdit_Project_Bsns_Done.setText("")
        self.lEdit_Project_Oth_Done.setText("")
        self.lEdit_Project_GP_Done.setText("")
        self.lEdit_Project_GPct_Done.setText("")
        # 打开文本框
        self.lEdit_Project_No.setEnabled(True)
        self.lEdit_Project_Name.setEnabled(True)
    def click_pbtn_ModifyProject(self):
        # 按钮变化
        self.pbtnCancelProject.setEnabled(True)
        self.pbtnUpdateProject.setEnabled(True)
        self.pbtnNewProject.setEnabled(False)
        self.pbtnQueryProject.setEnabled(False)
        self.pbtnModifyProject.setEnabled(False)
        self.pbtnDeleteProject.setEnabled(False)
        self.pbtn_PopUP_PjtPartyA.setEnabled(True)
        self.pbtn_PopUP_PjtPartyB.setEnabled(True)
        # 打开文本框
        self.lEdit_Project_No.setEnabled(True)
        self.lEdit_Project_Name.setEnabled(True)
    def click_pbtn_CancelProject(self):
        self.pbtnCancelProject.setEnabled(False)
        self.pbtnCommitProject.setEnabled(False)
        self.pbtnNewProject.setEnabled(True)
        self.pbtnQueryProject.setEnabled(True)
        self.pbtnModifyProject.setEnabled(True)
        self.pbtnDeleteProject.setEnabled(True)
        self.pbtn_PopUP_PjtPartyA.setEnabled(False)
        self.pbtn_PopUP_PjtPartyB.setEnabled(False)
        # 关闭文本框
        self.lEdit_Project_No.setEnabled(False)
        self.lEdit_Project_Name.setEnabled(False)
    def click_pbtn_UpdateProject(self):
        PjtNo = self.lEdit_Project_No.text().strip()
        PjtName = self.lEdit_Project_Name.text().strip()
        row_index = self.tbw_Project.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            if PjtNo == '' or PjtName == '':
                QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
            else:
                select_id = self.tbw_Project.item(row_index, 0).text()
                result = dbExec("update S_PROJECT set `Name` = %s ,`ProjectNo` = %s where `id` = %s",(PjtName,PjtNo,select_id))
                if result > 0:
                    self.mTabChange(2)
                else:
                    QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请选中数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_CommitProject(self):
        PjtNo = self.lEdit_Project_No.text().strip()
        PjtName = self.lEdit_Project_Name.text().strip()
        PjtPartyA = globalvar.pick_PjtPartyA
        PjtPartyB = globalvar.pick_PjtPartyB
        if PjtNo == '' or PjtName == '' or PjtPartyA == '' or PjtPartyB == '' :
            QMessageBox.warning(None, '警告', '请输入完整数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            result = dbExec("INSERT S_PROJECT (Name, PartyA_id, PartyB_id,ProjectNo,Status) values (%s,%s,%s,%s,%s);"
                            ,(PjtName,PjtPartyA,PjtPartyB,PjtNo,'已立项'))
            if result >0 :
                self.mTabChange(2)
            else:
                QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
    ## 槽函数：项目popup
    def click_pbtn_PopUpPartyA(self):
        popup_Account.popup_show(self, self.popup_account_projectA)
    def click_pbtn_PopUpPartyB(self):
        popup_Account.popup_show(self, self.popup_account_projectB)
    def popup_project_click_pbtn_pickA(self):
        globalvar.pick_PjtPartyA = ''
        popup_Account.popup_pick(self,self.popup_account_projectA)
        if globalvar.pick_account_id != '' :
            globalvar.pick_PjtPartyA = globalvar.pick_account_id
            result = dbQuery("select Name from S_ACCOUNT where id = %s",globalvar.pick_PjtPartyA)
            self.lEdit_Project_PartyA.setText(str(result[0][0]))
    def popup_project_click_pbtn_pickB(self):
        globalvar.pick_PjtPartyB = ''
        popup_Account.popup_pick(self,self.popup_account_projectB)
        if globalvar.pick_account_id != '' :
            globalvar.pick_PjtPartyB = globalvar.pick_account_id
            result = dbQuery("select Name from S_ACCOUNT where id = %s",globalvar.pick_PjtPartyB)
            self.lEdit_Project_PartyB.setText(str(result[0][0]))
    def popup_project_click_pbtn_quit(self):
        popup_Account.popup_quit(self,self.popup_account)
    ## 槽函数：项目采购售前单popup
    def click_pbtn_PurchaseList_Pre_New(self):
        row_index = self.tbw_Project.currentIndex().row()
        if row_index >=0 :
            select_id = self.tbw_Project.item(row_index, 0).text()
            if select_id != '':
                popup_PurchaseList_Pre.popup_show(self, self.popup_purchaselist_pre)
        else :
            QMessageBox.warning(None, '警告', '请选中项目记录后，再执行相关操作！', QMessageBox.Ok)
    def popup_popup_PurchaseList_Pre_Cancel(self):
        popup_PurchaseList_Pre.popup_quit(self,self.popup_purchaselist_pre)
    def popup_popup_PurchaseList_Pre_Save(self):
        popup_PurchaseList_Pre.popup_save(self, self.popup_purchaselist_pre)
        self.dTabChange(2)
    ## 槽函数：项目采购售前单内容项popup
    def click_pbtn_PurchaseList_Pre_Itm_New(self):
        row_index = self.tbw_Project_PurchaseList_Pre.currentIndex().row()
        if row_index >=0 :
            select_id = self.tbw_Project_PurchaseList_Pre.item(row_index, 0).text()
            if select_id != '':
                popup_PurchaseList_Itm_Pre.popup_show(self, self.popup_purchaseList_itm_pre)
        else :
            QMessageBox.warning(None, '警告', '请选中采购项清单记录后，再执行相关操作！', QMessageBox.Ok)
    def popup_popup_PurchaseList_Pre_Itm_Cancel(self):
        popup_PurchaseList_Itm_Pre.popup_quit(self,self.popup_purchaseList_itm_pre)
    def popup_popup_PurchaseList_Pre_Itm_Save(self):
        popup_PurchaseList_Itm_Pre.popup_save(self, self.popup_purchaseList_itm_pre)
    ## 槽函数：项目采购计划单
    def click_pbtn_Project_PurchaseList_Plan_Auto(self):
        row_index = self.tbw_Project.currentIndex().row()
        if row_index >= 0:
            select_id = self.tbw_Project.item(row_index, 0).text()
            result = dbQuery("select id from S_ORDER where Type = '采购计划单' and Project_id = %s",(select_id))
            if len(result) == 0 :
                result = dbExec("""INSERT INTO S_ORDER (Owner_id,Create_Time,Type,Project_id,`Name`,`Status`,Prchs_id) 
(select Owner_id,now(),'采购计划单',Project_id,`Name`,'状态Pending',Prchs_id from S_ORDER where type = '采购售前单' and Project_id = %s)""",(select_id))
                if result > 0 :
                    result = dbExec("""INSERT INTO S_ORDER_ITEM(Ord_id,Prod_id,Goods_id,Inquiry_id,Prod_Num,Unit_Name)
select ordn.id,itm.Prod_id, tg.id as "Goods_id",tgi.id as "Inquiry_id",itm.Prod_Num,itm.Unit_Name 
from S_ORDER ord 
INNER JOIN S_ORDER_ITEM itm on ord.id = itm.Ord_id
inner join S_ORDER ordo on itm.Ord_id = ordo.id and ordo.type = '采购售前单'
inner join S_ORDER ordn on ordo.project_id = ordn.project_id and ordo.`Name` = ordn.`Name` and ordn.type = '采购计划单'
Left JOIN (
SELECT
	s1.prod_id,
	s1.id,
	s1.sprice 
FROM
	(
	SELECT
		t1.prod_id,
		t1.id,
		t2.sprice 
	FROM
		S_GOODS t1
		INNER JOIN ( SELECT Goods_id, min( Price / Nums ) sprice FROM S_GOODS_INQUIRY GROUP BY Goods_id ) t2 ON t1.id = t2.Goods_id 
	) s1
	INNER JOIN (
	SELECT
		t1.prod_id,
		min( t2.sprice ) sprice 
	FROM
		S_GOODS t1
		INNER JOIN ( SELECT Goods_id, min( Price / Nums ) sprice FROM S_GOODS_INQUIRY GROUP BY Goods_id ) t2 ON t1.id = t2.Goods_id 
	GROUP BY
		t1.prod_id 
	) s2 ON s1.prod_id = s2.prod_id 
	AND s1.sprice = s2.sprice
) tg on itm.Prod_id = tg.prod_id
INNER JOIN (SELECT
	t1.id,
	t1.goods_id,
	t1.price,
	t1.Nums,
	t1.Cycle,
	t2.sprice 
FROM
	S_GOODS_INQUIRY t1
	INNER JOIN ( SELECT Goods_id, min( Price / Nums ) sprice FROM S_GOODS_INQUIRY GROUP BY Goods_id ) t2 ON t1.Goods_id = t2.Goods_id 
	AND t1.Price / t1.Nums = t2.sprice) tgi on tg.id = tgi.goods_id
where ord.type = '采购售前单' and ord.Project_id = %s""",(select_id))
            else:
                QMessageBox.warning(None, '警告', '项目已存在对应采购计划单，不可再次操作！', QMessageBox.Ok)
        else :
            QMessageBox.warning(None, '警告', '请选中一条项目数据后，再执行相关操作！', QMessageBox.Ok)
    ## 槽函数：项目立项单
    def click_pbtn_Project_Approval_New(self):
        # 按钮变化
        self.pbtn_Project_Approval_Query.setEnabled(False)
        self.pbtn_Project_Approval_Cancel.setEnabled(True)
        self.pbtn_Project_Approval_Save.setEnabled(True)
        self.pbtn_Project_Approval_Update.setEnabled(False)
        self.pbtn_Project_Approval_Delete.setEnabled(False)
        self.pbtn_Project_Approval_Modify.setEnabled(False)
        self.pbtn_Project_Approval_Run.setEnabled(False)
        self.pbtn_Project_Approval_New.setEnabled(False)
        # 打开文本框
        self.lEdit_PrjApp_Name.setEnabled(True)
        self.lEdit_PrjApp_ShortName.setEnabled(True)
        self.lEdit_PrjApp_CnstName.setEnabled(True)
        self.lEdit_PrjApp_ProjectNo.setEnabled(True)
        self.lEdit_PrjApp_Creator.setEnabled(True)
        self.lEdit_PrjApp_CreateDT.setEnabled(True)
        self.lEdit_PrjApp_TechMan.setEnabled(True)
        self.lEdit_PrjApp_Partner.setEnabled(True)
        self.lEdit_PrjApp_PM.setEnabled(True)
        self.lEdit_PrjApp_BL.setEnabled(True)
        self.lEdit_PrjApp_Bid.setEnabled(True)
        self.lEdit_PrjApp_WinDT.setEnabled(True)
        self.lEdit_PrjApp_Amount.setEnabled(True)
        self.lEdit_PrjApp_GP_Pre.setEnabled(True)
        self.lEdit_PrjApp_Const_Pre.setEnabled(True)
        self.lEdit_PrjApp_Bus_Pre.setEnabled(True)
        self.lEdit_PrjApp_Purchase_Pre.setEnabled(True)
        self.lEdit_PrjApp_Oth_Ore.setEnabled(True)
        # 文本框置空
        self.lEdit_PrjApp_Name.setText("")
        self.lEdit_PrjApp_ShortName.setText("")
        self.lEdit_PrjApp_CnstName.setText("")
        self.lEdit_PrjApp_ProjectNo.setText("")
        self.lEdit_PrjApp_Creator.setText("")
        self.lEdit_PrjApp_CreateDT.setText("")
        self.lEdit_PrjApp_TechMan.setText("")
        self.lEdit_PrjApp_Partner.setText("")
        self.lEdit_PrjApp_PM.setText("")
        self.lEdit_PrjApp_BL.setText("")
        self.lEdit_PrjApp_Bid.setText("")
        self.lEdit_PrjApp_WinDT.setText("")
        self.lEdit_PrjApp_Amount.setText("")
        self.lEdit_PrjApp_GP_Pre.setText("")
        self.lEdit_PrjApp_Const_Pre.setText("")
        self.lEdit_PrjApp_Bus_Pre.setText("")
        self.lEdit_PrjApp_Purchase_Pre.setText("")
        self.lEdit_PrjApp_Oth_Ore.setText("")
    def click_pbtn_Project_Approval_Save(self):
        row_index = self.tbw_Project.currentIndex().row()
        if row_index >= 0:
            pjt_id = self.tbw_Project.item(row_index, 0).text()
            Name = self.lEdit_PrjApp_Name.text().strip()
            ShortName = self.lEdit_PrjApp_ShortName.text().strip()
            CnstName = self.lEdit_PrjApp_CnstName.text().strip()
            ProjectNo = self.lEdit_PrjApp_ProjectNo.text().strip()
            Creator = self.lEdit_PrjApp_Creator.text().strip()
            CreateDT = self.lEdit_PrjApp_CreateDT.text().strip()
            TechMan = self.lEdit_PrjApp_TechMan.text().strip()
            Partner = self.lEdit_PrjApp_Partner.text().strip()
            PM = self.lEdit_PrjApp_PM.text().strip()
            BL = self.lEdit_PrjApp_BL.text().strip()
            Bid = self.lEdit_PrjApp_Bid.text().strip()
            WinDT = self.lEdit_PrjApp_WinDT.text().strip()
            Amount = self.lEdit_PrjApp_Amount.text().strip()
            GP_Pre = self.lEdit_PrjApp_GP_Pre.text().strip()
            Const_Pre = self.lEdit_PrjApp_Const_Pre.text().strip()
            Bus_Pre = self.lEdit_PrjApp_Bus_Pre.text().strip()
            Purchase_Pre = self.lEdit_PrjApp_Purchase_Pre.text().strip()
            Oth_Ore = self.lEdit_PrjApp_Oth_Ore.text().strip()
            if pjt_id != "" and Name != "" and ShortName != "" and CnstName != "" and ProjectNo != "" and Creator != "" and CreateDT != "" \
                    and TechMan != "" and Partner != "" and PM != "" and BL != "" and Bid != "" and WinDT != "" \
                    and Amount != "" and GP_Pre != "" and Const_Pre != "" and Bus_Pre != "" and Purchase_Pre != "" and Oth_Ore != "":
                row_index = self.tbw_Project.currentIndex().row()
                select_id = self.tbw_Project.item(row_index, 0).text()
                result = dbExec(
                    "INSERT INTO `S_PROJECT_APPROVAL` (Name,ShortName,CnstName,ProjectNo,Creator,CreateDT,TechMan,Partner,PM," +
                    "BL,Bid,WinDT,Amount,GP_Pre,Const_Pre,Bus_Pre,Purchase_Pre,Oth_Pre,pjt_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (Name,ShortName,CnstName,ProjectNo,Creator,CreateDT,TechMan,Partner,PM,BL,Bid,WinDT,Amount,GP_Pre,Const_Pre,Bus_Pre,Purchase_Pre,Oth_Ore,pjt_id))
                if result > 0:
                    self.mTabChange(0)
                else:
                    QMessageBox.warning(None, '警告', '新建失败！', QMessageBox.Ok)
            else:
                QMessageBox.warning(None, '警告', '请输入完整数据后，再执行相关操作！', QMessageBox.Ok)
        else :
            QMessageBox.warning(None, '警告', '请选中一条项目数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_Project_Approval_Cancel(self):
        # 按钮变化
        self.pbtn_Project_Approval_Query.setEnabled(True)
        self.pbtn_Project_Approval_Cancel.setEnabled(False)
        self.pbtn_Project_Approval_Save.setEnabled(False)
        self.pbtn_Project_Approval_Update.setEnabled(False)
        self.pbtn_Project_Approval_Delete.setEnabled(True)
        self.pbtn_Project_Approval_Modify.setEnabled(True)
        self.pbtn_Project_Approval_Run.setEnabled(False)
        self.pbtn_Project_Approval_New.setEnabled(True)
        # 关闭文本框
        self.lEdit_PrjApp_Name.setEnabled(False)
        self.lEdit_PrjApp_ShortName.setEnabled(False)
        self.lEdit_PrjApp_CnstName.setEnabled(False)
        self.lEdit_PrjApp_ProjectNo.setEnabled(False)
        self.lEdit_PrjApp_Creator.setEnabled(False)
        self.lEdit_PrjApp_CreateDT.setEnabled(False)
        self.lEdit_PrjApp_TechMan.setEnabled(False)
        self.lEdit_PrjApp_Partner.setEnabled(False)
        self.lEdit_PrjApp_PM.setEnabled(False)
        self.lEdit_PrjApp_BL.setEnabled(False)
        self.lEdit_PrjApp_Bid.setEnabled(False)
        self.lEdit_PrjApp_WinDT.setEnabled(False)
        self.lEdit_PrjApp_Amount.setEnabled(False)
        self.lEdit_PrjApp_GP_Pre.setEnabled(False)
        self.lEdit_PrjApp_Const_Pre.setEnabled(False)
        self.lEdit_PrjApp_Bus_Pre.setEnabled(False)
        self.lEdit_PrjApp_Purchase_Pre.setEnabled(False)
        self.lEdit_PrjApp_Oth_Ore.setEnabled(False)
    ## 槽函数：项目采购申请单
    def click_pbtn_Project_PurchaseList_Appr_Auto(self):
        row_index = self.tbw_Project.currentIndex().row()
        if row_index >= 0:
            select_id = self.tbw_Project.item(row_index, 0).text()
            if select_id != '':
                #popup_Pickup_Purchase_Plan.popup_show(self, self.popup_pickup_purchase_plan)
                popup_Pickup_Purchase_Plan_Item.popup_show(self, self.popup_pickup_purchase_plan_item)
        else:
            QMessageBox.warning(None, '警告', '请选中项目清单记录后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_Project_PurchaseList_Appr_Pick(self):
        popup_Pickup_Purchase_Plan_Item.popup_pick(self, self.popup_pickup_purchase_plan_item)
    ## 槽函数：项目采购订单
    def click_pbtn_Project_Cost_Purchase_Payment_New(self):
        popup_Payment.popup_show(self, self.popup_payment)
    def click_pbtn_Project_Cost_Purchase_Payment_Save(self):
        popup_Payment.popup_save(self, self.popup_payment)
    def click_pbtn_Project_Cost_Purchase_Payment_Cancel(self):
        popup_Payment.popup_quit(self, self.popup_payment)
    # 槽函数：采购提醒
    def popup_pbtn_Purchase_Notice__Purchase_Change(self):
        row_index = self.tbw_Purchase_Notice.currentIndex().row()
        if row_index >= 0 :
            select_id = self.tbw_Purchase_Notice.item(row_index, 0).text()
            itm_row_index = self.tbw_Purchase_Notice_Purchase.currentIndex().row()
            if itm_row_index >= 0 :
                itm_select_id = self.tbw_Purchase_Notice_Purchase.item(row_index, 0).text()
                result = dbExec("""update S_ORDER_ITEM set Inquiry_id = %s where id = %s """,(itm_select_id,select_id))
            else:
                QMessageBox.warning(None, '警告', '请选中供应列表数据后，再执行相关操作！', QMessageBox.Ok)
        else :
            QMessageBox.warning(None, '警告', '请选中提醒表单数据后，再执行相关操作！', QMessageBox.Ok)
        self.mTabChange(5)
    # 槽函数：采购任务
    def popup_Purchase_Job_Show(self):
        popup_Purchase_Job.popup_show(self, self.popup_purchase_job)
    def popup_Purchase_Job_Save(self):
        popup_Purchase_Job.popup_save(self, self.popup_purchase_job)
    def popup_aPurchase_Job_Cancel(self):
        popup_Purchase_Job.popup_quit(self, self.popup_purchase_job)
    def popup_Purchase_Job_Order_New(self):
        popup_Purchase_Job_Order.popup_show(self, self.popup_purchase_job_order)
    def popup_Purchase_Job_Order_Save(self):
        popup_Purchase_Job_Order.popup_save(self, self.popup_purchase_job_order)
    def popup_Purchase_Job_Order_Quit(self):
        popup_Purchase_Job_Order.popup_quit(self, self.popup_purchase_job_order)
    def popup_Purchase_Job_Order_Item_New(self):
        popup_Purchase_Job_Order_Item.popup_show(self, self.popup_purchase_job_order_item)
    def popup_Purchase_Job_Order_Item_Save(self):
        popup_Purchase_Job_Order_Item.popup_save(self, self.popup_purchase_job_order_item)
    def popup_Purchase_Job_Order_Item_Quit(self):
        popup_Purchase_Job_Order_Item.popup_quit(self, self.popup_purchase_job_order_item)

    # 槽函数：采购询价订单项
    def popup_Purchase_Inquiry_Rec_Show(self):
        popup_Purchase_Inquiry.popup_show(self, self.popup_purchase_inquiry)
    def popup_Purchase_Inquiry_Rec_Save(self):
        popup_Purchase_Inquiry.popup_save(self, self.popup_purchase_inquiry)
    def popup_Purchase_Inquiry_Rec_Cancel(self):
        popup_Purchase_Inquiry.popup_quit(self, self.popup_purchase_inquiry)
    ## 槽函数：采购任务订单项
    def popup_Purchase_Job_Contract_Show(self):
        popup_Purchase_Job_Contract.popup_show(self, self.popup_purchase_job_contract)
    def popup_Purchase_Job_Contract_Save(self):
        popup_Purchase_Job_Contract.popup_save(self, self.popup_purchase_job_contract)
    def popup_Purchase_Job_Contract_Cancel(self):
        popup_Purchase_Job_Contract.popup_quit(self, self.popup_purchase_job_contract)

    # 槽函数：采购结算
    def click_pbtn_tbw_Purchase_Payment_New(self):
        popup_Invoice.popup_show(self, self.popup_invoice)
    def click_pbtn_tbw_Purchase_Payment_Save(self):
        popup_Invoice.popup_save(self, self.popup_invoice)
    def click_pbtn_tbw_Purchase_Payment_Cancel(self):
        popup_Invoice.popup_quit(self, self.popup_invoice)
    def click_pbtn_Purchase_Payment_Invoice_New(self):
        popup_M_Pay_Invc.popup_show(self, self.popup_m_pay_invc)
    def click_pbtn_Purchase_Payment_Invoice_Save(self):
        popup_M_Pay_Invc.popup_save(self, self.popup_m_pay_invc)
    def click_pbtn_Purchase_Payment_Invoice_Cancel(self):
        popup_M_Pay_Invc.popup_quit(self, self.popup_m_pay_invc)
    # 槽函数：供应商
    def click_pbtn_Supppiler_New(self):
        # 按钮变化
        self.pbtn_Supppiler_Query.setEnabled(False)
        self.pbtn_Supppiler_Cancel.setEnabled(True)
        self.pbtn_Supppiler_Save.setEnabled(True)
        self.pbtn_Supppiler_Update.setEnabled(False)
        self.pbtn_Supppiler_Delete.setEnabled(False)
        self.pbtn_Supppiler_Modify.setEnabled(False)
        self.pbtn_Supppiler_Run.setEnabled(False)
        self.pbtn_Supppiler_New.setEnabled(False)
        # 文本框内容置空
        self.lEdit_Supppiler_BusinessNo.setText("")
        self.lEdit_Supppiler_TaxNo.setText("")
        self.lEdit_Supppiler_Level.setText("")
        self.lEdit_Supppiler_Amount.setText("")
        self.lEdit_Supppiler_FstDT.setText("")
        self.lEdit_Supppiler_Pay.setText("")
        self.lEdit_Supppiler_CheckDT.setText("")
        self.lEdit_Supppiler_unPayPct.setText("")
        self.lEdit_Supppiler_Name.setText("")
        self.lEdit_Supppiler_Scale.setText("")
        self.lEdit_Supppiler_Place.setText("")
        self.lEdit_Supppiler_Type.setText("")
        self.lEdit_Supppiler_Industry.setText("")
        # 打开文本框
        self.lEdit_Supppiler_BusinessNo.setEnabled(True)
        self.lEdit_Supppiler_TaxNo.setEnabled(True)
        self.lEdit_Supppiler_Level.setEnabled(False)
        self.lEdit_Supppiler_Amount.setEnabled(False)
        self.lEdit_Supppiler_FstDT.setEnabled(False)
        self.lEdit_Supppiler_Pay.setEnabled(False)
        self.lEdit_Supppiler_CheckDT.setEnabled(False)
        self.lEdit_Supppiler_unPayPct.setEnabled(False)
        self.lEdit_Supppiler_Name.setEnabled(True)
        self.lEdit_Supppiler_Scale.setEnabled(True)
        self.lEdit_Supppiler_Place.setEnabled(True)
        self.lEdit_Supppiler_Type.setEnabled(True)
        self.lEdit_Supppiler_Industry.setEnabled(True)
    def click_pbtn_Supppiler_Save(self):
        BusinessNo = self.lEdit_Supppiler_BusinessNo.text().strip()
        TaxNo = self.lEdit_Supppiler_TaxNo.text().strip()
        Name = self.lEdit_Supppiler_Name.text().strip()
        Scale = self.lEdit_Supppiler_Scale.text().strip()
        Place = self.lEdit_Supppiler_Place.text().strip()
        Type = self.lEdit_Supppiler_Type.text().strip()
        Industry = self.lEdit_Supppiler_Industry.text().strip()
        if Name != "" and BusinessNo != "" and Industry != "" and Scale != "" and Place != "" and TaxNo != "" and Type != "":
            result = dbQuery("select id from S_ACCOUNT where Business_license_No = %s or Tax_No = %s", (BusinessNo, TaxNo))
            if len(result) > 0 :
                result = dbExec(
                    "update`S_ACCOUNT` set Supppiler_Flg = 'Y' where Business_license_No = %s or Tax_No = %s", (BusinessNo, TaxNo))
            else :
                result = dbExec(
                    "insert into `S_ACCOUNT` (`Name`,`Business_license_No`,`Industry`, Scale, Place, Tax_No, Type, Level,Supppiler_Flg) " +
                    " values(%s,%s,%s,%s,%s,%s,%s,60,'Y')",
                    (Name, BusinessNo, Industry, Scale, Place, TaxNo, Type))
            if result > 0:
                self.mTabChange(8)
            else:
                QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_Supppiler_Cancel(self):
        # 按钮变化
        self.pbtn_Supppiler_Query.setEnabled(True)
        self.pbtn_Supppiler_Cancel.setEnabled(False)
        self.pbtn_Supppiler_Save.setEnabled(False)
        self.pbtn_Supppiler_Update.setEnabled(False)
        self.pbtn_Supppiler_Delete.setEnabled(True)
        self.pbtn_Supppiler_Modify.setEnabled(True)
        self.pbtn_Supppiler_Run.setEnabled(False)
        self.pbtn_Supppiler_New.setEnabled(True)
        # 文本框内容置空
        self.lEdit_Supppiler_BusinessNo.setText("")
        self.lEdit_Supppiler_TaxNo.setText("")
        self.lEdit_Supppiler_Level.setText("")
        self.lEdit_Supppiler_Amount.setText("")
        self.lEdit_Supppiler_FstDT.setText("")
        self.lEdit_Supppiler_Pay.setText("")
        self.lEdit_Supppiler_CheckDT.setText("")
        self.lEdit_Supppiler_unPayPct.setText("")
        # 打开文本框
        self.lEdit_Supppiler_BusinessNo.setEnabled(False)
        self.lEdit_Supppiler_TaxNo.setEnabled(False)
        self.lEdit_Supppiler_Level.setEnabled(False)
        self.lEdit_Supppiler_Amount.setEnabled(False)
        self.lEdit_Supppiler_FstDT.setEnabled(False)
        self.lEdit_Supppiler_Pay.setEnabled(False)
        self.lEdit_Supppiler_CheckDT.setEnabled(False)
        self.lEdit_Supppiler_unPayPct.setEnabled(False)
        self.lEdit_Supppiler_Name.setEnabled(False)
        self.lEdit_Supppiler_Scale.setEnabled(False)
        self.lEdit_Supppiler_Place.setEnabled(False)
        self.lEdit_Supppiler_Type.setEnabled(False)
        self.lEdit_Supppiler_Industry.setEnabled(False)
        # 刷新界面
        self.dTabChange(24)
    # 槽函数：产品
    def click_pbtn_Product_New(self):
        # 按钮变化
        self.pbtn_Product_Query.setVisible(False)
        self.pbtn_Product_Cancel.setVisible(True)
        self.pbtn_Product_Save.setVisible(True)
        self.pbtn_Product_Update.setVisible(False)
        self.pbtn_Product_Delete.setVisible(False)
        self.pbtn_Product_Modify.setVisible(False)
        self.pbtn_Product_Run.setVisible(False)
        self.pbtn_Product_New.setVisible(False)
        # 文本框内容置空
        self.lEdit_Prod_No.setText("")
        self.lEdit_Prod_Name.setText("")
        self.lEdit_Prod_TypeName.setText("")
        self.lEdit_Prod_TechStandard.setText("")
        self.lEdit_Prod_Unit.setText("")
        self.cBox_Prod_TypeA.clear()
        self.cBox_Prod_TypeB.clear()
        self.cBox_Prod_Origin.clear()
        # 打开文本框
        self.lEdit_Prod_No.setEnabled(True)
        self.lEdit_Prod_Name.setEnabled(True)
        self.lEdit_Prod_TypeName.setEnabled(True)
        self.lEdit_Prod_TechStandard.setEnabled(True)
        self.lEdit_Prod_Unit.setEnabled(True)
        self.cBox_Prod_TypeA.setEnabled(True)
        self.cBox_Prod_TypeB.setEnabled(True)
        self.cBox_Prod_Origin.setEnabled(True)
        # 填充下拉框
        result = dbQueryFull("""SELECT t2.`Value`
  from S_LOV t1
 INNER JOIN S_LOV t2
    on t1.Type_code = t2.Type_code
   and t2.Type_flg = 'N'
 where t1.Type_flg = 'Y'
   and t1. Value = '产品大类'
""")
        row = len(result)
        if row > 0:
            for fi in range(row):
                self.cBox_Prod_TypeA.addItem(str(result[fi][0]))
        self.click_cBox_Prod_TypeA()
        result = dbQueryFull("""SELECT t2.`Value`
          from S_LOV t1
         INNER JOIN S_LOV t2
            on t1.Type_code = t2.Type_code
           and t2.Type_flg = 'N'
         where t1.Type_flg = 'Y'
           and t1. Value = '产品产地'
        """)
        row = len(result)
        if row > 0:
            for fi in range(row):
                self.cBox_Prod_Origin.addItem(str(result[fi][0]))
    def click_cBox_Prod_TypeA(self):
        Prod_TypeA = self.cBox_Prod_TypeA.currentText()
        self.cBox_Prod_TypeB.clear()
        if Prod_TypeA != '' :
            result = dbQuery("""SELECT t2.`Value`
  from S_LOV t1
 INNER JOIN S_LOV t2
    on t1.Type_code = t2.Type_code
   and t2.Type_flg = 'N'
 INNER JOIN S_LOV t3
    on t3.`Index` = t2.Type_par
   and t3.`Value` = %s
 where t1.Type_flg = 'Y'
   and t1.`Value` = %s
            """,(Prod_TypeA,'产品小类'))
            row = len(result)
            if row > 0:
                for fi in range(row):
                    self.cBox_Prod_TypeB.addItem(str(result[fi][0]))
    def click_pbtn_Product_Save(self):
        No = self.lEdit_Prod_No.text().strip()
        Name = self.lEdit_Prod_Name.text().strip()
        TypeName = self.lEdit_Prod_TypeName.text().strip()
        TechStandard = self.lEdit_Prod_TechStandard.text().strip()
        Unit = self.lEdit_Prod_Unit.text().strip()
        TypeA = self.cBox_Prod_TypeA.currentText()
        TypeB = self.cBox_Prod_TypeB.currentText()
        Origin = self.cBox_Prod_Origin.currentText()
        if No != "" and Name != "" and TypeName != "" and TechStandard != "" and Unit != "" and TypeA != "" and TypeB != "" and Origin != "" :
            result = dbExec("insert into S_PRODUCT (`No`,TypeA,TypeB,`Name`,Model,Origin,Standard,Unit_Name,`Comment`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (No, TypeA, TypeB, Name,TypeName,Origin,TechStandard,Unit,""))
            if result > 0:
                self.mTabChange(9)
            else:
                QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
    def click_pbtn_Product_Cancel(self):
        # 更新按钮
        self.pbtn_Product_Query.setVisible(True)
        self.pbtn_Product_Cancel.setVisible(False)
        self.pbtn_Product_Save.setVisible(False)
        self.pbtn_Product_Update.setVisible(False)
        self.pbtn_Product_Delete.setVisible(True)
        self.pbtn_Product_Modify.setVisible(True)
        self.pbtn_Product_Run.setVisible(False)
        self.pbtn_Product_New.setVisible(True)
        # 关闭文本框
        self.lEdit_Prod_No.setEnabled(False)
        self.lEdit_Prod_Name.setEnabled(False)
        self.lEdit_Prod_TypeName.setEnabled(False)
        self.lEdit_Prod_TechStandard.setEnabled(False)
        self.lEdit_Prod_Unit.setEnabled(False)
        self.cBox_Prod_TypeA.setEnabled(False)
        self.cBox_Prod_TypeB.setEnabled(False)
        self.cBox_Prod_Origin.setEnabled(False)
        # 充值文本值
        self.cBox_Prod_TypeA.clear()
        self.cBox_Prod_TypeB.clear()
        self.cBox_Prod_Origin.clear()
    # 槽函数：供应品
    def popup_Goods_Show(self):
        popup_Goods.popup_show(self, self.popup_goods)
    def popup_Goods_Save(self):
        popup_Goods.popup_save(self, self.popup_goods)
    def popup_Goods_Cancel(self):
        popup_Goods.popup_quit(self, self.popup_goods)

    # 槽函数：列表点击
    ## 槽函数：联系人列表点击
    def click_tbw_Account(self):
        row_index = self.tbw_Account.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Account.item(row_index, 0).text()
            if tab_name.strip() == '客户详情'.strip():
                result = dbQueryFull("""SELECT
	t1.type, t1.Scale,
	t1.Business_license_No,
	t1.`Name`,
	t1.Industry,
	t1.Place,
	t1.Tax_No,
	sum( IFNULL( t2.amount, 0 ) ),
	'' AS "回款金额",
	'' AS "未回款金额",
	'' AS "未回款比例" 
FROM
	S_ACCOUNT t1
	LEFT OUTER JOIN S_CONTRACT t2 ON t1.id = t2.PartyA_id 
WHERE
	t1.id =  """ + select_id + """ GROUP BY
	t1.Scale,
	t1.Business_license_No,
	t1.`Name`,
	t1.Industry,
	t1.Place,
	t1.Scale,
	t1.Tax_No""")

                self.lEdit_Acnt_Type.setText(str(result[0][0]))
                self.lEdit_Acnt_Scale.setText(str(result[0][1]))
                self.lEdit_Acnt_OrgCode.setText(str(result[0][2]))
                self.lEdit_Account_Name.setText(str(result[0][3]))
                self.lEdit_Acnt_Industry.setText(str(result[0][4]))
                self.lEdit_Acnt_Place.setText(str(result[0][5]))
                self.lEdit_Acnt_tax.setText(str(result[0][6]))
                self.lEdit_Acnt_Total.setText(str(result[0][7]))
                self.lEdit_Acnt_Return.setText(str(result[0][8]))
                self.lEdit_Acnt_unReturn.setText(str(result[0][9]))
                self.lEdit_Acnt_unReturnPst.setText(str(result[0][10]))
            elif tab_name.strip() == '客户项目'.strip():
                self.tbw_Account_Project.setRowCount(0)
                result = dbQueryFull(
                    "SELECT t1.id,t1.name, concat(tpmc.Fst_Name,tpmc.lst_name),t2.No,concat(tblc.Fst_Name,tblc.lst_name),t1.status,'项目地址'" +
                    "FROM S_PROJECT t1 left outer join S_CONTRACT t2 on t1.id = t2.project_id " +
                    "left outer join S_PROJECT_EMP t3pm on t1.id = t3pm.project_id and t3pm.status = 'Y' and t3pm.type = 'PM' " +
                    "left outer join S_PROJECT_EMP t3bl on t1.id = t3bl.project_id and t3bl.status = 'Y' and t3bl.type = 'BL' " +
                    "left outer join S_EMPLOYEE tpme on t3pm.Emp_id = tpme.id and tpme.Active_Flg = 'Y' " +
                    "left outer join S_EMPLOYEE tble on t3bl.Emp_id = tble.id and tble.Active_Flg = 'Y' " +
                    "left outer join S_CONTACT tpmc on tpme.con_id = tpmc.id " +
                    "left outer join S_CONTACT tblc on tble.con_id = tblc.id " +
                    "where t1.PartyA_id = " + select_id)
                row = len(result)
                vol = self.tbw_Account_Project.columnCount()
                self.tbw_Account_Project.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Account_Project.setItem(fi, fj, data)
                self.tbw_Account_Project.setAlternatingRowColors(True)
                self.tbw_Account_Project.resizeColumnsToContents()
                self.tbw_Account_Project.resizeRowsToContents()
            elif tab_name.strip() == '客户合同'.strip():
                self.tbw_Account_Contract.setRowCount(0)
                result = dbQueryFull(
                    "SELECT t1.id,t1.no,t1.name,t2.name,t3.name,t1.amount FROM S_CONTRACT t1 " +
                    "left outer join S_ACCOUNT t2 on t1.partyA_id = t2.id " +
                    "left outer join S_ACCOUNT t3 on t1.PartyB_id = t3.id " +
                    "where t1.PartyA_id = " + select_id)
                row = len(result)
                vol = self.tbw_Account_Contract.columnCount()
                self.tbw_Account_Contract.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Account_Contract.setItem(fi, fj, data)
                self.tbw_Account_Contract.setAlternatingRowColors(True)
                self.tbw_Account_Contract.resizeColumnsToContents()
                self.tbw_Account_Contract.resizeRowsToContents()
            elif tab_name.strip() == '客户联系人'.strip():
                self.tbw_Account_Contact.setRowCount(0)
                result = dbQueryFull(
                    "SELECT t1.id,concat(t1.Fst_Name,t1.lst_name),'销售处','销售经理', '高', '30', t1.phone, 'test@123.com' FROM operation.S_CONTACT t1 " +
                    "where t1.account_id = " + select_id)
                row = len(result)
                vol = self.tbw_Account_Contact.columnCount()
                self.tbw_Account_Contact.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Account_Contact.setItem(fi, fj, data)
                self.tbw_Account_Contact.setAlternatingRowColors(True)
                self.tbw_Account_Contact.resizeColumnsToContents()
                self.tbw_Account_Contact.resizeRowsToContents()
            else:
                pass
        else:
            if tab_name.strip() == '客户详情'.strip():
                self.lEdit_Acnt_Type.setText(" ")
                self.lEdit_Acnt_OrgCode.setText(" ")
                self.lEdit_Acnt_Total.setText(" ")
            elif tab_name.strip() == '客户项目'.strip():
                self.tbw_Account_Project.setRowCount(0)
            elif tab_name.strip() == '客户合同'.strip():
                self.tbw_Account_Contract.setRowCount(0)
            elif tab_name.strip() == '客户联系人'.strip():
                self.tbw_Account_Contact.setRowCount(0)
            else:
                pass
    ## 槽函数：联系人列表点击
    def click_tbw_Contact(self):
        row_index = self.tbw_Contact.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Contact.item(row_index, 0).text()
            if tab_name.strip() == '联系人详情'.strip():
                result = dbQueryFull("""select t1.id, t2.`Name`, t1.Fst_Name,t1.Lst_Name,  '' as "department", '' as "position"  , 
                                    '' as sup_num, '' as age , Phone , '123@123.com' as mail
                                    from S_CONTACT t1 LEFT JOIN S_ACCOUNT t2 on t1.Account_id = t2.id where t1.id = """ + select_id)
                self.lEdit_Cnt_Org.setText(str(result[0][1]))
                self.lEdit_Cnt_FstName.setText(str(result[0][2]))
                self.lEdit_Cnt_LstName.setText(str(result[0][3]))
                self.lEdit_Cnt_Phone.setText(str(result[0][8]))
            elif tab_name.strip() == '联系人项目'.strip():
                self.tbw_Contact_Project.setRowCount(0)
                result = dbQueryFull("""SELECT t1.id, t1.NAME, CONCAT(t3.Fst_Name, t3.Lst_Name), '' AS "prj_no",
       CONCAT(t5.Fst_Name, t5.Lst_Name), t1. Status, t6.Type
    FROM S_PROJECT t1
    LEFT JOIN S_PROJECT_EMP t2
    ON t1.id = t2.Project_id
    AND t2.Type = 'PM'
    LEFT JOIN S_CONTACT t3
    ON t2.Emp_id = t3.id
    LEFT JOIN S_PROJECT_EMP t4
    ON t1.id = t4.Project_id
    AND t4.Type = 'BL'
    LEFT JOIN S_CONTACT t5
    ON t4.Emp_id = t5.id
    LEFT JOIN S_PROJECT_EMP t6
    ON t1.id = t6.Project_id
    where t6.Emp_id = """ + select_id)
                row = len(result)
                vol = self.tbw_Contact_Project.columnCount()
                self.tbw_Contact_Project.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Contact_Project.setItem(fi, fj, data)
                self.tbw_Contact_Project.setAlternatingRowColors(True)
                self.tbw_Contact_Project.resizeColumnsToContents()
                self.tbw_Contact_Project.resizeRowsToContents()
            elif tab_name.strip() == '联系人通讯地址'.strip():
                self.tbw_Contact_Address.setRowCount(0)
                result = dbQueryFull("""SELECT
	t3.id,
	t2.mobile_phone,
	t2.line_phone,
	t2.email,
	CONCAT(
		ifnull( t3.country, '' ),
		ifnull( t3.province, '' ),
		ifnull( t3.city, '' ),
		ifnull( t3.street, '' ),
		ifnull( t3.address, '' ) 
	),
	t3.consignee_name,
	t2.priority,
	t2.coments 
FROM
	`S_CONTACT` t1
	INNER JOIN S_CONTACT_ADDR t2 ON t1.id = t2.con_id
	INNER JOIN S_ADDRESS t3 ON t2.adr_id = t3.id 
WHERE
	t1.id = """ + select_id)
                row = len(result)
                vol = self.tbw_Contact_Address.columnCount()
                self.tbw_Contact_Address.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Contact_Address.setItem(fi, fj, data)
                self.tbw_Contact_Address.setAlternatingRowColors(True)
                self.tbw_Contact_Address.resizeColumnsToContents()
                self.tbw_Contact_Address.resizeRowsToContents()
            elif tab_name.strip() == '联系人组织'.strip():
                self.tbw_Contact_Org.setRowCount(0)
                result = dbQueryFull("""select t1.id, t1.Industry, t1. Name, t1.Industry, t1.Scale, t1.Place,
       t1.Scale, '' as rolename
    from S_ACCOUNT t1
    LEFT JOIN S_CONTACT t2
    on t1.id = t2.Account_id
    WHERE t2.id = """ + select_id)
                row = len(result)
                vol = self.tbw_Contact_Org.columnCount()
                self.tbw_Contact_Org.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Contact_Org.setItem(fi, fj, data)
                self.tbw_Contact_Org.setAlternatingRowColors(True)
                self.tbw_Contact_Org.resizeColumnsToContents()
                self.tbw_Contact_Org.resizeRowsToContents()
            else:
                pass
        else:
            if tab_name.strip() == '客户详情'.strip():
                self.lEdit_Cnt_Org.setText(" ")
                self.lEdit_Cnt_FstName.setText(" ")
                self.lEdit_Cnt_LstName.setText(" ")
                self.lEdit_Cnt_Phone.setText(" ")
            else:
                pass
    ## 槽函数：项目列表点击
    def click_tbw_Project(self):
        row_index = self.tbw_Project.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Project.item(row_index, 0).text()
            if tab_name.strip() == '项目详单'.strip():
                result = dbQueryFull("""SELECT t1.id,  t1.ProjectNo as "No", t1. Name as "ProjectName", t2. Name as "PartyAname",
       t3. Name as "PartyBname", CONCAT(bln.Fst_Name, bln.Lst_Name) as "BL",
       CONCAT(pmn.Fst_Name, pmn.Lst_Name) as "PM", tc.Amount,
       '' as "baozheng", '' as "caigouyusuan", '' as "caigoufasheng",
       '' as "gongchengyusuan", '' as "gongchengfasheng",
       '' as "yewufeiyong", '' as "maolirun", '' as "maolilv"
  FROM S_PROJECT t1
  LEFT JOIN S_ACCOUNT t2
    on t1.PartyA_id = t2.id
  LEFT JOIN S_ACCOUNT t3
    on t1.PartyB_id = t3.id
  LEFT JOIN S_PROJECT_EMP pm
    on t1.id = pm.Project_id
   and pm.Type = 'PM'
   and pm. Status = 'Y'
  LEFT JOIN S_CONTACT pmn
    on pm.Emp_id = pmn.id
  LEFT JOIN S_PROJECT_EMP bl
    on t1.id = bl.Project_id
   and bl.Type = 'BL'
   and bl. Status = 'Y'
  LEFT JOIN S_CONTACT bln
    on bl.Emp_id = bln.id
  LEFT JOIN S_CONTRACT tc
    on t1.id = tc.Project_id where t1.id =""" + select_id)
                self.lEdit_Project_No.setText(str(result[0][1]))
                self.lEdit_Project_Name.setText(str(result[0][2]))
                self.lEdit_Project_PartyA.setText(str(result[0][3]))
                self.lEdit_Project_PartyB.setText(str(result[0][4]))
            elif tab_name.strip() == '项目采购售前单'.strip():
                self.tbw_Project_PurchaseList_Pre.setRowCount(0)
                result = dbQueryFull("""select ord.id, ord. Name, ord. Status, CONCAT(con.Fst_Name, con.Lst_Name),
       CONCAT(apr.Fst_Name, apr.Lst_Name)
  from S_ORDER ord
  LEFT JOIN S_CONTACT con
    on ord.owner_id = con.id
  LEFT JOIN S_CONTACT apr
    on ord.Approved_id = apr.id
    WHERE ord.type = '采购售前单' and ord.Project_id = """ + select_id)
                row = len(result)
                vol = self.tbw_Project_PurchaseList_Pre.columnCount()
                self.tbw_Project_PurchaseList_Pre.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Project_PurchaseList_Pre.setItem(fi, fj, data)
                self.tbw_Project_PurchaseList_Pre.setAlternatingRowColors(True)
                self.tbw_Project_PurchaseList_Pre.resizeColumnsToContents()
                self.tbw_Project_PurchaseList_Pre.resizeRowsToContents()
            elif tab_name.strip() == '项目采购计划单'.strip():
                self.tbw_Project_PurchaseList_Plan.setRowCount(0)
                result = dbQueryFull("""select ord.id, ord. Name, ord. Status, CONCAT(con.Fst_Name, con.Lst_Name),
       CONCAT(apr.Fst_Name, apr.Lst_Name)
  from S_ORDER ord
  LEFT JOIN S_CONTACT con
    on ord.owner_id = con.id
  LEFT JOIN S_CONTACT apr
    on ord.Approved_id = apr.id
    WHERE ord.type = '采购计划单' and ord.Project_id = """ + select_id)
                row = len(result)
                vol = self.tbw_Project_PurchaseList_Plan.columnCount()
                self.tbw_Project_PurchaseList_Plan.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Project_PurchaseList_Plan.setItem(fi, fj, data)
                self.tbw_Project_PurchaseList_Plan.setAlternatingRowColors(True)
                self.tbw_Project_PurchaseList_Plan.resizeColumnsToContents()
                self.tbw_Project_PurchaseList_Plan.resizeRowsToContents()
            elif tab_name.strip() == '项目立项单'.strip():
                # 文本框置空
                self.lEdit_PrjApp_Name.setText("")
                self.lEdit_PrjApp_ShortName.setText("")
                self.lEdit_PrjApp_CnstName.setText("")
                self.lEdit_PrjApp_ProjectNo.setText("")
                self.lEdit_PrjApp_Creator.setText("")
                self.lEdit_PrjApp_CreateDT.setText("")
                self.lEdit_PrjApp_TechMan.setText("")
                self.lEdit_PrjApp_Partner.setText("")
                self.lEdit_PrjApp_PM.setText("")
                self.lEdit_PrjApp_BL.setText("")
                self.lEdit_PrjApp_Bid.setText("")
                self.lEdit_PrjApp_WinDT.setText("")
                self.lEdit_PrjApp_Amount.setText("")
                self.lEdit_PrjApp_GP_Pre.setText("")
                self.lEdit_PrjApp_Const_Pre.setText("")
                self.lEdit_PrjApp_Bus_Pre.setText("")
                self.lEdit_PrjApp_Purchase_Pre.setText("")
                self.lEdit_PrjApp_Oth_Ore.setText("")
                # 查询数据
                result = dbQueryFull("""SELECT Name, ShortName, CnstName, ProjectNo, Creator, CreateDT, TechMan,
       Partner, PM, BL, Bid, WinDT, Amount, GP_Pre, Const_Pre, Bus_Pre,
       Purchase_Pre, Oth_Pre
  FROM S_PROJECT_APPROVAL
 where pjt_id = """ + select_id)
                if len(result) > 0:
                    self.lEdit_PrjApp_Name.setText(str(result[0][0]))
                    self.lEdit_PrjApp_ShortName.setText(str(result[0][1]))
                    self.lEdit_PrjApp_CnstName.setText(str(result[0][2]))
                    self.lEdit_PrjApp_ProjectNo.setText(str(result[0][3]))
                    self.lEdit_PrjApp_Creator.setText(str(result[0][4]))
                    self.lEdit_PrjApp_CreateDT.setText(str(result[0][5]))
                    self.lEdit_PrjApp_TechMan.setText(str(result[0][6]))
                    self.lEdit_PrjApp_Partner.setText(str(result[0][7]))
                    self.lEdit_PrjApp_PM.setText(str(result[0][8]))
                    self.lEdit_PrjApp_BL.setText(str(result[0][9]))
                    self.lEdit_PrjApp_Bid.setText(str(result[0][10]))
                    self.lEdit_PrjApp_WinDT.setText(str(result[0][11]))
                    self.lEdit_PrjApp_Amount.setText(str(result[0][12]))
                    self.lEdit_PrjApp_GP_Pre.setText(str(result[0][13]))
                    self.lEdit_PrjApp_Const_Pre.setText(str(result[0][14]))
                    self.lEdit_PrjApp_Bus_Pre.setText(str(result[0][15]))
                    self.lEdit_PrjApp_Purchase_Pre.setText(str(result[0][16]))
                    self.lEdit_PrjApp_Oth_Ore.setText(str(result[0][17]))
            elif tab_name.strip() == '项目采购申请单'.strip():
                self.tbw_Project_PurchaseList_Appr.setRowCount(0)
                result = dbQueryFull("""SELECT t1.id, CONCAT(t2.Fst_Name,t2.Lst_Name),'部门Pending', t1.Comments, t1.plan_dt,t1.Create_Time FROM `S_ORDER` t1 
LEFT JOIN S_CONTACT t2 on t1.Owner_id = t2.id
WHERE t1.Type = '采购申请单' and t1.Project_id = """ + select_id)
                row = len(result)
                vol = self.tbw_Project_PurchaseList_Appr.columnCount()
                self.tbw_Project_PurchaseList_Appr.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Project_PurchaseList_Appr.setItem(fi, fj, data)
                self.tbw_Project_PurchaseList_Appr.setAlternatingRowColors(True)
                self.tbw_Project_PurchaseList_Appr.resizeColumnsToContents()
                self.tbw_Project_PurchaseList_Appr.resizeRowsToContents()
            elif tab_name.strip() == '项目合同'.strip():
                self.tbw_Project_Contract.setRowCount(0)
                result = dbQueryFull("""SELECT distinct t3.id,t3.`No`,t3.Type,pa.`Name` as "PartyA",pb.`Name` as "PartyB",t3.Amount,t3.DT_Active
FROM `S_ORDER` t1
INNER JOIN S_PROJECT t2 on t1.Project_id = t2.id
INNER JOIN S_CONTRACT t3 on t1.Prchs_id = t3.Prchs_id
INNER JOIN S_ACCOUNT pa on t3.PartyA_id = pa.id
INNER JOIN S_ACCOUNT pb on t3.PartyB_id = pb.id
where t1.Type = '采购购买单' and t2.id = """ + select_id)
                row = len(result)
                vol = self.tbw_Project_Contract.columnCount()
                self.tbw_Project_Contract.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Project_Contract.setItem(fi, fj, data)
                self.tbw_Project_Contract.setAlternatingRowColors(True)
                self.tbw_Project_Contract.resizeColumnsToContents()
                self.tbw_Project_Contract.resizeRowsToContents()
            elif tab_name.strip() == '项目供应商'.strip():
                self.tbw_Project_Supppiler.setRowCount(0)
                result = dbQueryFull("""SELECT t5.id,t5.`Name`, t5.Industry,t5.Scale,t5.Place,sum(t4.Prod_Num * t4.Unit_Price) as "Total", '支付总额pending', '回票总额pending', '回票比率pending'
FROM `S_ORDER` t1
INNER JOIN S_ORDER_ITEM t4 on t1.id = t4.ord_id
INNER JOIN S_PURCHASE t3 on t1.Prchs_id = t3.id
INNER JOIN S_ACCOUNT t5 on t3.Supppiler_id = t5.id
where t1.Type = '采购购买单' and t1.Project_id = """ + select_id + """ group by t5.id,t5.`Name`, t5.Industry,t5.Scale,t5.Place""")
                row = len(result)
                vol = self.tbw_Project_Supppiler.columnCount()
                self.tbw_Project_Supppiler.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Project_Supppiler.setItem(fi, fj, data)
                self.tbw_Project_Supppiler.setAlternatingRowColors(True)
                self.tbw_Project_Supppiler.resizeColumnsToContents()
                self.tbw_Project_Supppiler.resizeRowsToContents()
            elif tab_name.strip() == '项目采购订单'.strip():
                self.tbw_Project_Cost_Purchase.setRowCount(0)
                result = dbQueryFull("""SELECT t1.id,t1.`Name` as "OrdName", t6.`No`,t5.`Name` as "PrchsName",t6.Amount,sum(t4.Prod_Num * t4.Unit_Price) as "Total", '回票总额pending'
FROM `S_ORDER` t1
INNER JOIN S_ORDER_ITEM t4 on t1.id = t4.ord_id
INNER JOIN S_PURCHASE t3 on t1.Prchs_id = t3.id
INNER JOIN S_ACCOUNT t5 on t3.Supppiler_id = t5.id
left join S_CONTRACT t6 on t3.id = t6.Prchs_id
where t1.Type = '采购购买单' and t1.Project_id = """ + select_id + """ group by t1.id,t1.`Name`, t6.`No`,t5.`Name`,t6.Amount""")
                row = len(result)
                vol = self.tbw_Project_Cost_Purchase.columnCount()
                self.tbw_Project_Cost_Purchase.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Project_Cost_Purchase.setItem(fi, fj, data)
                self.tbw_Project_Cost_Purchase.setAlternatingRowColors(True)
                self.tbw_Project_Cost_Purchase.resizeColumnsToContents()
                self.tbw_Project_Cost_Purchase.resizeRowsToContents()
                self.click_tbw_Project_Cost_Purchase()
            elif tab_name.strip() == '项目开票及回款'.strip():
                self.tbw_Contact_Org.setRowCount(0)
                result = dbQueryFull("""select t1.id, t1.Industry, t1. Name, t1.Industry, t1.Scale, t1.Place,
               t1.Scale, '' as rolename
            from S_ACCOUNT t1
            LEFT JOIN S_CONTACT t2
            on t1.id = t2.Account_id
            WHERE t2.id = """ + select_id)
                row = len(result)
                vol = self.tbw_Contact_Org.columnCount()
                self.tbw_Contact_Org.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Contact_Org.setItem(fi, fj, data)
                self.tbw_Contact_Org.setAlternatingRowColors(True)
                self.tbw_Contact_Org.resizeColumnsToContents()
                self.tbw_Contact_Org.resizeRowsToContents()
            elif tab_name.strip() == '项目干系人'.strip():
                self.tbw_Contact_Org.setRowCount(0)
                result = dbQueryFull("""select t1.id, t1.Industry, t1. Name, t1.Industry, t1.Scale, t1.Place,
               t1.Scale, '' as rolename
            from S_ACCOUNT t1
            LEFT JOIN S_CONTACT t2
            on t1.id = t2.Account_id
            WHERE t2.id = """ + select_id)
                row = len(result)
                vol = self.tbw_Contact_Org.columnCount()
                self.tbw_Contact_Org.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Contact_Org.setItem(fi, fj, data)
                self.tbw_Contact_Org.setAlternatingRowColors(True)
                self.tbw_Contact_Org.resizeColumnsToContents()
                self.tbw_Contact_Org.resizeRowsToContents()
            else:
                pass
        else:
            if tab_name.strip() == '客户详情'.strip():
                self.lEdit_Cnt_Org.setText(" ")
                self.lEdit_Cnt_FstName.setText(" ")
                self.lEdit_Cnt_LstName.setText(" ")
                self.lEdit_Cnt_Phone.setText(" ")
            else:
                pass
    def click_tbw_Project_PurchaseList_Pre(self):
        row_index = self.tbw_Project_PurchaseList_Pre.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Project_PurchaseList_Pre.item(row_index, 0).text()
            self.tbw_Project_PurchaseList_Pre_Item.setRowCount(0)
            result = dbQueryFull("""SELECT itm.id, prd.`Name`, prd.Model, prd.Standard, itm.Prod_Num, itm.Unit_Name, itm.Comments
  FROM S_ORDER ord
 INNER JOIN S_ORDER_ITEM itm
    on ord.id = itm.Ord_id
  LEFT JOIN S_PRODUCT prd
    on itm.Prod_id = prd.id where ord.id = """ + select_id)
            row = len(result)
            vol = self.tbw_Project_PurchaseList_Pre_Item.columnCount()
            self.tbw_Project_PurchaseList_Pre_Item.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Project_PurchaseList_Pre_Item.setItem(fi, fj, data)
            self.tbw_Project_PurchaseList_Pre_Item.setAlternatingRowColors(True)
            self.tbw_Project_PurchaseList_Pre_Item.resizeColumnsToContents()
            self.tbw_Project_PurchaseList_Pre_Item.resizeRowsToContents()
    def click_tbw_Project_PurchaseList_Plan(self):
        row_index = self.tbw_Project_PurchaseList_Plan.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Project_PurchaseList_Plan.item(row_index, 0).text()
            self.tbw_Project_PurchaseList_Plan_Item.setRowCount(0)
            result = dbQueryFull("""SELECT
	itm.id,
	prd.`Name`,
	prd.Model,
	prd.Standard,
	sp.`Name`,
	sp.Industry,
	sp.Scale,
	gd.Brand,
	gd.Model,
	gd.Market_DT,
	itm.Unit_Price/1000,
	gi.Cycle,
	itm.Prod_Num,
	itm.Unit_Name,
	gi.Inquiry_dt,
	itm.Comments 
FROM
	S_ORDER ord
	INNER JOIN S_ORDER_ITEM itm ON ord.id = itm.Ord_id
	LEFT JOIN S_PRODUCT prd ON itm.Prod_id = prd.id
	LEFT JOIN S_GOODS gd ON itm.Goods_id = gd.id
	LEFT JOIN S_ACCOUNT sp ON gd.Supppiler_id = sp.id
	LEFT JOIN S_GOODS_INQUIRY gi ON itm.Inquiry_id = gi.id 
WHERE
	ord.type = '采购计划单' 
	AND ord.id = """ + select_id)
            row = len(result)
            vol = self.tbw_Project_PurchaseList_Plan_Item.columnCount()
            self.tbw_Project_PurchaseList_Plan_Item.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Project_PurchaseList_Plan_Item.setItem(fi, fj, data)
            self.tbw_Project_PurchaseList_Plan_Item.setAlternatingRowColors(True)
            self.tbw_Project_PurchaseList_Plan_Item.resizeColumnsToContents()
            self.tbw_Project_PurchaseList_Plan_Item.resizeRowsToContents()
    def click_tbw_Project_PurchaseList_Appr(self):
        row_index = self.tbw_Project_PurchaseList_Appr.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Project_PurchaseList_Appr.item(row_index, 0).text()
            self.tbw_Project_PurchaseList_Appr_Item.setRowCount(0)
            result = dbQueryFull("""SELECT
        	itm.id,
        	prd.`Name`,
        	prd.Model,
        	prd.Standard,
        	sp.`Name`,
        	sp.Industry,
        	sp.Scale,
        	gd.Brand,
        	gd.Model,
        	gd.Market_DT,
        	itm.Unit_Price/1000,
        	gi.Cycle,
        	itm.Prod_Num,
        	itm.Unit_Name,
        	gi.Inquiry_dt,
        	itm.Comments 
        FROM
        	S_ORDER ord
        	INNER JOIN S_ORDER_ITEM itm ON ord.id = itm.Ord_id
        	LEFT JOIN S_PRODUCT prd ON itm.Prod_id = prd.id
        	LEFT JOIN S_GOODS gd ON itm.Goods_id = gd.id
        	LEFT JOIN S_ACCOUNT sp ON gd.Supppiler_id = sp.id
        	LEFT JOIN S_GOODS_INQUIRY gi ON itm.Inquiry_id = gi.id 
        WHERE
        	ord.type = '采购申请单' 
        	AND ord.id = """ + select_id)
            row = len(result)
            vol = self.tbw_Project_PurchaseList_Appr_Item.columnCount()
            self.tbw_Project_PurchaseList_Appr_Item.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Project_PurchaseList_Appr_Item.setItem(fi, fj, data)
            self.tbw_Project_PurchaseList_Appr_Item.setAlternatingRowColors(True)
            self.tbw_Project_PurchaseList_Appr_Item.resizeColumnsToContents()
            self.tbw_Project_PurchaseList_Appr_Item.resizeRowsToContents()
    ## 槽函数：采购询价列表点击
    def click_tbw_Purchase_Inquiry(self):
        row_index = self.tbw_Purchase_Inquiry.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Purchase_Inquiry.item(row_index, 0).text()
            self.tbw_Purchase_Inquiry_Rec.setRowCount(0)
            result = dbQueryFull(
                "select t2.id,t3.`Name`,t3.Industry,t3.Scale,t3.Place,t1.Brand,t2.nums,round(t2.Price/1000,4),round(t2.Price/t2.nums/1000,4),t2.Cycle,t2.Inquiry_dt, t2.comments " +
                "from S_GOODS t1 LEFT JOIN S_GOODS_INQUIRY t2 on t1.id = t2.Goods_id LEFT JOIN S_ACCOUNT t3 on t1.Supppiler_id = t3.id " +
                "where t1.id = " + select_id)
            row = len(result)
            vol = self.tbw_Purchase_Inquiry_Rec.columnCount()
            self.tbw_Purchase_Inquiry_Rec.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Inquiry_Rec.setItem(fi, fj, data)
            self.tbw_Purchase_Inquiry_Rec.setAlternatingRowColors(True)
            self.tbw_Purchase_Inquiry_Rec.resizeColumnsToContents()
            self.tbw_Purchase_Inquiry_Rec.resizeRowsToContents()
        else:
            if tab_name.strip() == '客户详情'.strip():
                self.lEdit_Acnt_Type.setText(" ")
                self.lEdit_Acnt_OrgCode.setText(" ")
                self.lEdit_Acnt_Total.setText(" ")
            elif tab_name.strip() == '客户项目'.strip():
                self.tbw_Account_Project.setRowCount(0)
            elif tab_name.strip() == '客户合同'.strip():
                self.tbw_Account_Contract.setRowCount(0)
            elif tab_name.strip() == '客户联系人'.strip():
                self.tbw_Account_Contact.setRowCount(0)
            else:
                pass
    def click_tbw_Purchase_Job_Order(self):
        row_index = self.tbw_Purchase_Job_Order.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Purchase_Job_Order.item(row_index, 0).text()
            self.tbw_Purchase_Job_Order_Item.setRowCount(0)
            result = dbQueryFull("SELECT t1.id,t4.`Name`, t3.Model, t1.Prod_Num,t1.Unit_Name,t1.Unit_Price, " +
            """t1.Unit_Price*t1.Prod_Num as "total", t1.Comments from S_ORDER_ITEM t1 """ +
            "LEFT JOIN S_GOODS_INQUIRY t2 on t1.Inquiry_id = t2.id " +
            "LEFT JOIN S_GOODS t3 on t2.Goods_id = t3.id " +
            "LEFT JOIN S_PRODUCT t4 on t3.Prod_id = t4.id " +
            "where t1.Ord_id = " + select_id)
            row = len(result)
            vol = self.tbw_Purchase_Job_Order_Item.columnCount()
            self.tbw_Purchase_Job_Order_Item.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Job_Order_Item.setItem(fi, fj, data)
            self.tbw_Purchase_Job_Order_Item.setAlternatingRowColors(True)
            self.tbw_Purchase_Job_Order_Item.resizeColumnsToContents()
            self.tbw_Purchase_Job_Order_Item.resizeRowsToContents()
    ## 槽函数：采购计划列表点击
    def click_tbw_Purchase_Plan(self):
        row_index = self.tbw_Purchase_Plan.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Purchase_Plan.item(row_index, 0).text()
            if tab_name.strip() == '计划内容'.strip():
                self.tbw_Purchase_Plan_Prod.setRowCount(0)
                result = dbQueryFull("""SELECT
    t1.id,
    t2.TypeA,
    t2.TypeB,
    t2.`Name`,
    t2.Model,
    t1.Prod_Num,
    t1.Comments 
FROM
    `S_ORDER_ITEM` t1
    LEFT JOIN S_PRODUCT t2 ON t1.Prod_id = t2.id
Where t1.Ord_id = """ + select_id)
                row = len(result)
                vol = self.tbw_Purchase_Plan_Prod.columnCount()
                self.tbw_Purchase_Plan_Prod.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Purchase_Plan_Prod.setItem(fi, fj, data)
                self.tbw_Purchase_Plan_Prod.setAlternatingRowColors(True)
                self.tbw_Purchase_Plan_Prod.resizeColumnsToContents()
                self.tbw_Purchase_Plan_Prod.resizeRowsToContents()
            elif tab_name.strip() == '产品供应品'.strip():
                self.tbw_Product_Goods.setRowCount(0)
                result = dbQueryFull(
                    "select t1.id,t2.`Name`, t2.Industry, t2.Scale, t1.brand, t1.model, t1.Market_DT,t1.Price , t1.Cycle,'Pending' " +
                    "from S_GOODS t1 LEFT JOIN S_ACCOUNT t2 on t1.Supppiler_id = t2.id " +
                    "where t1.Prod_id = " + select_id)
                row = len(result)
                vol = self.tbw_Product_Goods.columnCount()
                self.tbw_Product_Goods.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Product_Goods.setItem(fi, fj, data)
                self.tbw_Product_Goods.setAlternatingRowColors(True)
                self.tbw_Product_Goods.resizeColumnsToContents()
                self.tbw_Product_Goods.resizeRowsToContents()
            else:
                pass
        else:
            if tab_name.strip() == '客户详情'.strip():
                self.lEdit_Acnt_Type.setText(" ")
                self.lEdit_Acnt_OrgCode.setText(" ")
                self.lEdit_Acnt_Total.setText(" ")
            elif tab_name.strip() == '客户项目'.strip():
                self.tbw_Account_Project.setRowCount(0)
            elif tab_name.strip() == '客户合同'.strip():
                self.tbw_Account_Contract.setRowCount(0)
            elif tab_name.strip() == '客户联系人'.strip():
                self.tbw_Account_Contact.setRowCount(0)
            else:
                pass
    def click_tbw_Purchase_Plan_Prod(self):
        row_index = self.tbw_Purchase_Plan_Prod.currentIndex().row()
        if row_index >= 0:
            select_id = self.tbw_Purchase_Plan_Prod.item(row_index, 0).text()
            self.tbw_Purchase_Plan_Goods.setRowCount(0)
            result = dbQueryFull("""SELECT
    t3.id,
    act.`Name` AS "Sup_Name",
    act.Industry,
    act.Scale,
    t2.Brand,
    t2.Model,
    t2.Market_DT,
    round(t3.mprice/1000,4),
    t3.Cycle,
    t3.Inquiry_dt 
FROM
    `S_ORDER_ITEM` t1
    INNER JOIN S_GOODS t2 ON t1.Prod_id = t2.Prod_id
    LEFT JOIN S_ACCOUNT act ON t2.Supppiler_id = act.id
    LEFT JOIN (
    SELECT
        t1.id,
        t1.Goods_id,
        t2.mprice,
        t1.Cycle,
        t1.Inquiry_dt 
    FROM
        S_GOODS_INQUIRY t1
        INNER JOIN ( SELECT goods_id, min( price / Nums ) mprice FROM S_GOODS_INQUIRY GROUP BY goods_id ) t2 ON t1.Goods_id = t2.goods_id 
        AND t1.price / t1.Nums = t2.mprice 
    ) t3 ON t2.id = t3.Goods_id 
where t1.id = """ + select_id)
            row = len(result)
            vol = self.tbw_Purchase_Plan_Goods.columnCount()
            self.tbw_Purchase_Plan_Goods.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Plan_Goods.setItem(fi, fj, data)
            self.tbw_Purchase_Plan_Goods.setAlternatingRowColors(True)
            self.tbw_Purchase_Plan_Goods.resizeColumnsToContents()
            self.tbw_Purchase_Plan_Goods.resizeRowsToContents()
    ## 槽函数：采购提示列表点击
    def click_tbw_Purchase_Notice(self):
        row_index = self.tbw_Purchase_Notice.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Purchase_Notice.item(row_index, 0).text()
            self.tbw_Purchase_Notice_Purchase.setRowCount(0)
            result = dbQueryFull(
                """SELECT
	inq.id,
	sup.`Name`,
	sup.Industry,
	sup.Scale,
	sup.Place,
	gds.Brand,
	gds.Model,
	round(inq.Price/inq.Nums / 1000,4 ),
	inq.Nums,
	round(((inq.Price/inq.Nums) * inq.Nums) /1000,4) AS "Amount",
	inq.Cycle,
	inq.Inquiry_dt 
FROM
	S_ORDER ord
	INNER JOIN S_ORDER_ITEM itm ON ord.id = itm.ord_id
	INNER JOIN S_GOODS gds ON itm.Prod_id = gds.Prod_id
	INNER JOIN S_ACCOUNT sup ON gds.Supppiler_id = sup.id
	LEFT JOIN S_GOODS_INQUIRY inq ON gds.id = inq.Goods_id 
WHERE
	itm.id = """ + select_id + """ 
ORDER BY
	inq.Price, Inquiry_dt desc""")
            row = len(result)
            vol = self.tbw_Purchase_Notice_Purchase.columnCount()
            self.tbw_Purchase_Notice_Purchase.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Notice_Purchase.setItem(fi, fj, data)
            self.tbw_Purchase_Notice_Purchase.setAlternatingRowColors(True)
            self.tbw_Purchase_Notice_Purchase.resizeColumnsToContents()
            self.tbw_Purchase_Notice_Purchase.resizeRowsToContents()
    def click_tbw_Project_Cost_Purchase(self):
        row_index = self.tbw_Project_Cost_Purchase.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Project_Cost_Purchase.item(row_index, 0).text()
            self.tbw_Project_Cost_Purchase_Payment.setRowCount(0)
            result = dbQueryFull(
                """SELECT t1.id,t1.Pay_Date,t1.Reason,t1.Amount,t1.dep_id,t1.Emp_id,t1.Pay_Type,t1.Note_Code FROM `S_PAYMENT` t1 WHERE t1.Ord_id = """ + select_id + """ 
         ORDER BY
        	t1.Pay_Date""")
            row = len(result)
            vol = self.tbw_Project_Cost_Purchase_Payment.columnCount()
            self.tbw_Project_Cost_Purchase_Payment.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Project_Cost_Purchase_Payment.setItem(fi, fj, data)
            self.tbw_Project_Cost_Purchase_Payment.setAlternatingRowColors(True)
            self.tbw_Project_Cost_Purchase_Payment.resizeColumnsToContents()
            self.tbw_Project_Cost_Purchase_Payment.resizeRowsToContents()
    def click_tbw_Project_Cost_Purchase_Payment(self):
        row_index = self.tbw_Project_Cost_Purchase_Payment.currentIndex().row()
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Project_Cost_Purchase_Payment.item(row_index, 0).text()
            self.tbw_Project_Cost_Purchase_Invoice.setRowCount(0)
            result = dbQueryFull(
                """SELECT
	t1.id,
	t1.Return_Date,
	t1.Invoice_Date,
	t1.Invoice_No,
	t1.Amount,
	t1.Tax_Rate,
	t1.Exchange,
	ts.`Name`,
	tb.`Name` 
FROM
	`S_INVOICE` t1
	INNER JOIN S_M_PYMNT_INVC tm ON t1.id = tm.Invc_id
	INNER JOIN S_PAYMENT t2 ON tm.Pay_id = t2.id
	LEFT JOIN S_ACCOUNT tb ON t1.Buyer_id = tb.id
	LEFT JOIN S_ACCOUNT ts ON t1.Seller_id = ts.id 
WHERE t2.id = """ + select_id)
            row = len(result)
            vol = self.tbw_Project_Cost_Purchase_Invoice.columnCount()
            self.tbw_Project_Cost_Purchase_Invoice.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Project_Cost_Purchase_Invoice.setItem(fi, fj, data)
            self.tbw_Project_Cost_Purchase_Invoice.setAlternatingRowColors(True)
            self.tbw_Project_Cost_Purchase_Invoice.resizeColumnsToContents()
            self.tbw_Project_Cost_Purchase_Invoice.resizeRowsToContents()
    ## 槽函数:采购任务列表点击
    def click_tbw_Purchase_Job(self):
        row_index = self.tbw_Purchase_Job.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Purchase_Job.item(row_index, 0).text()
            if tab_name.strip() == '采购订单'.strip():
                self.tbw_Purchase_Job_Order.setRowCount(0)
                result = dbQueryFull("""select `id`,`Type`,`Create_Time`,'pending','pending',`Name` from S_ORDER where `Type` = '采购购买单' and Prchs_id = """ + select_id)
                row = len(result)
                vol = self.tbw_Purchase_Job_Order.columnCount()
                self.tbw_Purchase_Job_Order.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Purchase_Job_Order.setItem(fi, fj, data)
                self.tbw_Purchase_Job_Order.setAlternatingRowColors(True)
                self.tbw_Purchase_Job_Order.resizeColumnsToContents()
                self.tbw_Purchase_Job_Order.resizeRowsToContents()
                self.click_tbw_Purchase_Job_Order()
            elif tab_name.strip() == '采购合同'.strip():
                self.tbw_Purchase_Job_Contract.setRowCount(0)
                result = dbQueryFull("""SELECT t1.id, t1.`No`, t1.`Name`, pa.`Name` as "PartyA", pb.`Name`  as "PartyB", t1.Amount, t1.`Status` """ +
                                    "FROM S_CONTRACT t1 " +
                                    "LEFT JOIN S_ACCOUNT pa on t1.PartyA_id = pa.id " +
                                    "LEFT JOIN S_ACCOUNT pb on t1.PartyB_id = pb.id " +
                                    "where t1.Prchs_id = " + select_id)
                row = len(result)
                vol = self.tbw_Purchase_Job_Contract.columnCount()
                self.tbw_Purchase_Job_Contract.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Purchase_Job_Contract.setItem(fi, fj, data)
                self.tbw_Purchase_Job_Contract.setAlternatingRowColors(True)
                self.tbw_Purchase_Job_Contract.resizeColumnsToContents()
                self.tbw_Purchase_Job_Contract.resizeRowsToContents()
            elif tab_name.strip() == '采购项目'.strip():
                self.tbw_Purchase_Job_Project.setRowCount(0)
                result = dbQueryFull("""SELECT DISTINCT
	t2.id,
	t2.ProjectNo,
	t2.`Name`,
	partyA.`Name` as "AName",
	partyB.`Name` as "BName",
	CONCAT( tt5.Fst_Name, tt5.Lst_Name ) as "BL",
	CONCAT( tt3.Fst_Name, tt3.Lst_Name ) as "PM",
	tc.Amount,
	'保证金pending',
	pjta.Purchase_Pre,
	'采购发生比例pending',
	pjta.Const_Pre,
	'工程发生比例pending',
	pjta.Bus_Pre,
	pjta.GP_Pre,
	'毛利率pending' 
FROM
	S_ORDER t1
	INNER JOIN S_PROJECT t2 ON t1.Project_id = t2.id
	LEFT JOIN S_ACCOUNT partyA ON t2.PartyA_id = partyA.id
	LEFT JOIN S_ACCOUNT partyB ON t2.PartyB_id = partyB.id
	LEFT JOIN S_PROJECT_EMP tt2 ON t2.id = tt2.Project_id 
	AND tt2.Type = 'PM'
	LEFT JOIN S_CONTACT tt3 ON tt2.Emp_id = tt3.id
	LEFT JOIN S_PROJECT_EMP tt4 ON t2.id = tt4.Project_id 
	AND tt4.Type = 'BL'
	LEFT JOIN S_CONTACT tt5 ON tt4.Emp_id = tt5.id
	LEFT JOIN S_CONTRACT tc ON t2.id = tc.Project_id
	LEFT JOIN S_PROJECT_APPROVAL pjta ON t2.id = pjta.pjt_id 
WHERE
	t1.Type = '采购购买单' 
	AND t1.Prchs_id = """ + select_id)
                row = len(result)
                vol = self.tbw_Purchase_Job_Project.columnCount()
                self.tbw_Purchase_Job_Project.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Purchase_Job_Project.setItem(fi, fj, data)
                self.tbw_Purchase_Job_Project.setAlternatingRowColors(True)
                self.tbw_Purchase_Job_Project.resizeColumnsToContents()
                self.tbw_Purchase_Job_Project.resizeRowsToContents()
            else:
                pass
        else:
            if tab_name.strip() == '客户详情'.strip():
                self.lEdit_Cnt_Org.setText(" ")
                self.lEdit_Cnt_FstName.setText(" ")
                self.lEdit_Cnt_LstName.setText(" ")
                self.lEdit_Cnt_Phone.setText(" ")
            else:
                pass
    ## 槽函数：采购结算列表点击
    def click_tbw_Purchase_Payment(self):
        row_index = self.tbw_Purchase_Payment.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Purchase_Payment.item(row_index, 0).text()
            if tab_name.strip() == '支付单关联'.strip():
                self.tbw_Purchase_Payment_Invoice.setRowCount(0)
                result = dbQueryFull(
                    """SELECT
	t1.id,
	t1.Pay_Date,
	t1.Reason,
	t1.Amount,
	t1.dep_id,
	t1.Emp_id,
	t1.Pay_Type,
	t1.Note_Code 
FROM
	`S_PAYMENT` t1 
INNER JOIN S_M_PYMNT_INVC t2
on t1.id = t2.Pay_id
WHERE
	t2.Invc_id = """ + select_id + """ 
ORDER BY
	t1.Pay_Date """)
                row = len(result)
                vol = self.tbw_Purchase_Payment_Invoice.columnCount()
                self.tbw_Purchase_Payment_Invoice.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Purchase_Payment_Invoice.setItem(fi, fj, data)
                self.tbw_Purchase_Payment_Invoice.setAlternatingRowColors(True)
                self.tbw_Purchase_Payment_Invoice.resizeColumnsToContents()
                self.tbw_Purchase_Payment_Invoice.resizeRowsToContents()
            else:
                pass
        else:
            if tab_name.strip() == '客户详情'.strip():
                pass
            else:
                pass
    ## 槽函数：供应商列表点击
    def click_tbw_Supppiler(self):
        row_index = self.tbw_Supppiler.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Supppiler.item(row_index, 0).text()
            if tab_name.strip() == '供应商详情'.strip():
                result = dbQueryFull("""select a.Business_license_No, a.Tax_No, a.`Level`,
       sum(ifnull(p.Amount, 0)) as "已付金额",
       sum(ifnull(ct.Amount, 0)) as "合同总额", min(ct.DT_Active) as "初次供应日期",
       ROUND((1 - sum(ifnull(p.Amount, 0)) /
              if(sum(ifnull(ct.Amount, 0)) = 0,
                      1,
                      sum(ifnull(ct.Amount, 0)))) * 100) as "未付款比例", a.`Name`, a.type, a.Industry, a.Scale , a.Place
  from S_ACCOUNT a
  LEFT JOIN S_PAYMENT p
    on a.id = p.Pay_Target
  LEFT JOIN S_CONTRACT ct
    on a.id = ct.PartyB_id
   and ct.Type = '实施合同'
 where a.Active_Flg = 'Y'
   and a.Supppiler_Flg = 'Y' and a.id = """ + select_id +
 " group by a.Business_license_No, a.Tax_No, a.`Level`, a.`Name`, a.type, a.Industry, a.Scale , a.Place")
                if len(result) > 0:
                    self.lEdit_Supppiler_BusinessNo.setText(str(result[0][0]))
                    self.lEdit_Supppiler_TaxNo.setText(str(result[0][1]))
                    self.lEdit_Supppiler_Level.setText(str(result[0][2]))
                    self.lEdit_Supppiler_Pay.setText(str(result[0][3]))
                    self.lEdit_Supppiler_Amount.setText(str(result[0][4]))
                    self.lEdit_Supppiler_FstDT.setText(str(result[0][5]))
                    self.lEdit_Supppiler_CheckDT.setText("pending")
                    self.lEdit_Supppiler_unPayPct.setText(str(result[0][6]))
                    self.lEdit_Supppiler_Name.setText(str(result[0][7]))
                    self.lEdit_Supppiler_Type.setText(str(result[0][8]))
                    self.lEdit_Supppiler_Industry.setText(str(result[0][9]))
                    self.lEdit_Supppiler_Scale.setText(str(result[0][10]))
                    self.lEdit_Supppiler_Place.setText(str(result[0][11]))
            elif tab_name.strip() == '供应商合同'.strip():
                self.tbw_Supppiler_Contract.setRowCount(0)
                result = dbQueryFull("""select crt.`id`, crt.`No`, crt.`Name`, acta.`Name` as "PartyA_Name", act.`Name` as "PartyB_Name", crt.`Amount` , 'Pending'
  from S_ACCOUNT act
 INNER JOIN S_CONTRACT crt
    on act.id = crt.PartyB_id
   and crt.Type = '采购合同'
 inner join S_ACCOUNT acta
    on crt.PartyA_id = acta.id
 where act.Active_Flg = 'Y'
   and act.Supppiler_Flg = 'Y'
   and act.id = """ + select_id)
                row = len(result)
                vol = self.tbw_Supppiler_Contract.columnCount()
                self.tbw_Supppiler_Contract.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Supppiler_Contract.setItem(fi, fj, data)
                self.tbw_Supppiler_Contract.setAlternatingRowColors(True)
                self.tbw_Supppiler_Contract.resizeColumnsToContents()
                self.tbw_Supppiler_Contract.resizeRowsToContents()
            elif tab_name.strip() == '供应商项目'.strip():
                self.tbw_Supppiler_Project.setRowCount(0)
                result = dbQueryFull("""select distinct t1.`Name`,t4.ProjectNo,t4.`Name`,pa.`Name` as "PartyA",pb.`Name` as "PartyB",  """ +
                                    """CONCAT(cbl.Fst_Name,cbl.Lst_Name) as "BL" , CONCAT(cpm.Fst_Name,cpm.Lst_Name) as "PM"   """ +
                                    """from S_ACCOUNT t1   """ +
                                    """INNER JOIN S_PURCHASE t2 on t1.id = t2.Supppiler_id  """ +
                                    """INNER JOIN S_ORDER t3 on t2.id = t3.Prchs_id   """ +
                                    """INNER JOIN S_PROJECT t4 on t3.Project_id = t4.id  """ +
                                    """LEFT JOIN S_ACCOUNT pa on t4.PartyA_id = pa.id  """ +
                                    """LEFT JOIN S_ACCOUNT pb on t4.PartyB_id = pb.id  """ +
                                    """left join S_PROJECT_EMP pbl on t4.id = pbl.project_id and pbl.Type = 'BL'  """ +
                                    """left join S_CONTACT cbl on pbl.Emp_id = cbl.id  """ +
                                    """left join S_PROJECT_EMP ppm on t4.id = ppm.project_id and ppm.Type = 'PM'  """ +
                                    """left join S_CONTACT cpm on ppm.Emp_id = cpm.id  """ +
                                    """where t1.id = """ + select_id)
                row = len(result)
                vol = self.tbw_Supppiler_Project.columnCount()
                self.tbw_Supppiler_Project.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Supppiler_Project.setItem(fi, fj, data)
                self.tbw_Supppiler_Project.setAlternatingRowColors(True)
                self.tbw_Supppiler_Project.resizeColumnsToContents()
                self.tbw_Supppiler_Project.resizeRowsToContents()
            elif tab_name.strip() == '供应商干系人'.strip():
                self.tbw_Supppiler_Contact.setRowCount(0)
                result = dbQueryFull("""select ct.id,CONCAT(ct.Fst_Name,ct.Lst_Name),'pending','pending','pending','pending',ct.Phone from S_CONTACT ct where ct.Account_id = """ + select_id)
                row = len(result)
                vol = self.tbw_Supppiler_Contact.columnCount()
                self.tbw_Supppiler_Contact.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Supppiler_Contact.setItem(fi, fj, data)
                self.tbw_Supppiler_Contact.setAlternatingRowColors(True)
                self.tbw_Supppiler_Contact.resizeColumnsToContents()
                self.tbw_Supppiler_Contact.resizeRowsToContents()
            else:
                pass
        else:
            pass
    ## 槽函数：产品列表点击
    def click_tbw_Product(self):
        row_index = self.tbw_Product.currentIndex().row()
        tab_name = self.Tab_Detail.tabText(self.Tab_Detail.currentIndex())
        # 如果有选中记录
        if row_index >= 0:
            select_id = self.tbw_Product.item(row_index, 0).text()
            if tab_name.strip() == '产品详情'.strip():
                self.lEdit_Prod_No.setText("")
                self.lEdit_Prod_Name.setText("")
                self.lEdit_Prod_TypeName.setText("")
                self.lEdit_Prod_TechStandard.setText("")
                self.lEdit_Prod_Unit.setText("")
                self.cBox_Prod_TypeA.clear()
                self.cBox_Prod_TypeB.clear()
                # 绑定数据
                result = dbQueryFull(
                    "SELECT p.`No`, p.`Name`,p.TypeA, p.TypeB , p.Model, p.Origin,p.Standard,p.Unit_Name FROM S_PRODUCT p where p.id = " + select_id)
                self.lEdit_Prod_No.setText(str(result[0][0]))
                self.lEdit_Prod_Name.setText(str(result[0][1]))
                self.lEdit_Prod_TypeName.setText(str(result[0][4]))
                self.cBox_Prod_Origin.addItem(str(result[0][5]))
                self.lEdit_Prod_TechStandard.setText(str(result[0][6]))
                self.lEdit_Prod_Unit.setText(str(result[0][7]))
                self.cBox_Prod_TypeA.addItem(str(result[0][2]))
                self.cBox_Prod_TypeB.addItem(str(result[0][3]))
                self.tbw_Product_parameter.setRowCount(0)
                result2 = dbQueryFull("""SELECT pm.parameter,pm.`condition`, pm.`value`, pm.`comment` FROM S_PRODUCT_PARAMETER pm where pm.prd_id = """
                                      + select_id + " order by id")
                row = len(result2)
                vol = self.tbw_Product_parameter.columnCount()
                self.tbw_Product_parameter.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result2[fi][fj]))
                        self.tbw_Product_parameter.setItem(fi, fj, data)
                self.tbw_Product_parameter.setAlternatingRowColors(True)
                self.tbw_Product_parameter.resizeColumnsToContents()
                self.tbw_Product_parameter.resizeRowsToContents()
            elif tab_name.strip() == '产品供应品'.strip():
                self.tbw_Product_Goods.setRowCount(0)
                result = dbQueryFull(
                    "select t1.id,t2.`Name`, t2.Industry, t2.Scale, t1.brand, t1.model, t1.Market_DT,t1.Price , t1.Cycle,'Pending' " +
                    "from S_GOODS t1 LEFT JOIN S_ACCOUNT t2 on t1.Supppiler_id = t2.id " +
                    "where t1.Prod_id = " + select_id)
                row = len(result)
                vol = self.tbw_Product_Goods.columnCount()
                self.tbw_Product_Goods.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Product_Goods.setItem(fi, fj, data)
                self.tbw_Product_Goods.setAlternatingRowColors(True)
                self.tbw_Product_Goods.resizeColumnsToContents()
                self.tbw_Product_Goods.resizeRowsToContents()
            elif tab_name.strip() == '产品历史报价'.strip():
                self.tbw_Product_HisPrice.setRowCount(0)
                result = dbQueryFull(
                    "SELECT t2.id,t3.`Name`, t3.Industry, t3.Scale, t3.Place, t1.Brand, t2.nums,t2.Price,round(t2.Price/t2.nums) sPrice,t2.Cycle,t2.Inquiry_dt, 'Pending' "+
                    "FROM `S_GOODS` t1 LEFT JOIN `S_GOODS_INQUIRY` t2 on t1.id = t2.Goods_id " +
                    "LEFT JOIN S_ACCOUNT t3 on t1.Supppiler_id = t3.id where t1.Prod_id = " + select_id)
                row = len(result)
                vol = self.tbw_Product_HisPrice.columnCount()
                self.tbw_Product_HisPrice.setRowCount(row)
                for fi in range(row):
                    for fj in range(vol):
                        data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                        self.tbw_Product_HisPrice.setItem(fi, fj, data)
                self.tbw_Product_HisPrice.setAlternatingRowColors(True)
                self.tbw_Product_HisPrice.resizeColumnsToContents()
                self.tbw_Product_HisPrice.resizeRowsToContents()
            else:
                pass
        else:
            if tab_name.strip() == '客户详情'.strip():
                self.lEdit_Acnt_Type.setText(" ")
                self.lEdit_Acnt_OrgCode.setText(" ")
                self.lEdit_Acnt_Total.setText(" ")
            elif tab_name.strip() == '客户项目'.strip():
                self.tbw_Account_Project.setRowCount(0)
            elif tab_name.strip() == '客户合同'.strip():
                self.tbw_Account_Contract.setRowCount(0)
            elif tab_name.strip() == '客户联系人'.strip():
                self.tbw_Account_Contact.setRowCount(0)
            else:
                pass


    # 槽函数：页签切换
    ## 槽函数：主页签切换
    def mTabChange(self, currentIndex):
        tab_name = self.Tab_Main.tabText(currentIndex)
        # 删除全部选项
        i = 0
        q = self.Tab_Detail.count()
        while i <= q:
            self.Tab_Detail.removeTab(0)
            i = i + 1
        # 各主页签数据填充
        if tab_name.strip() == '客户'.strip():
            self.mTabAccount()
            # 绑定数据
            result = dbQueryFull(
                "select id,Name,Industry,Scale,Place,Business_license_No,Tax_No,Level from S_ACCOUNT where id != 0 and Active_Flg = 'Y' and Custmoer_Flg = 'Y'")
            row = len(result)
            vol = self.tbw_Account.columnCount()
            self.tbw_Account.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Account.setItem(fi, fj, data)
            self.mTabAccountFormat()
        elif tab_name.strip() == '联系人'.strip():
            self.mTabContact()
            result = dbQueryFull("""select t1.id, t2.`Name`, CONCAT(t1.Fst_Name,t1.Lst_Name) "full_name",  '' as "department", '' as "position"  , 
                                      '' as sup_num, '' as age , Phone , '123@123.com' as mail
                                      from S_CONTACT t1 LEFT JOIN S_ACCOUNT t2 on t1.Account_id = t2.id where t1.Active_Flg = 'Y'""")
            row = len(result)
            vol = self.tbw_Account.columnCount()
            self.tbw_Contact.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Contact.setItem(fi, fj, data)
            self.mTabContactFormat()
        elif tab_name.strip() == '项目'.strip():
            self.mTabProject()
            result = dbQueryFull("""SELECT t1.id,  t1.ProjectNo as "No", t1. Name, t2. Name as "PartyAname",
         t3. Name as "PartyBname", CONCAT(bln.Fst_Name, bln.Lst_Name) as "BL",
         CONCAT(pmn.Fst_Name, pmn.Lst_Name) as "PM", tc.Amount,
         '' as "baozheng", '' as "caigouyusuan", '' as "caigoufasheng",
         '' as "gongchengyusuan", '' as "gongchengfasheng",
         '' as "yewufeiyong", '' as "maolirun", '' as "maolilv"
    FROM S_PROJECT t1
    LEFT JOIN S_ACCOUNT t2
      on t1.PartyA_id = t2.id
    LEFT JOIN S_ACCOUNT t3
      on t1.PartyB_id = t3.id
    LEFT JOIN S_PROJECT_EMP pm
      on t1.id = pm.Project_id
     and pm.Type = 'PM'
     and pm. Status = 'Y'
    LEFT JOIN S_CONTACT pmn
      on pm.Emp_id = pmn.id
    LEFT JOIN S_PROJECT_EMP bl
      on t1.id = bl.Project_id
     and bl.Type = 'BL'
     and bl. Status = 'Y'
    LEFT JOIN S_CONTACT bln
      on bl.Emp_id = bln.id
    LEFT JOIN S_CONTRACT tc
      on t1.id = tc.Project_id and tc.Type = '实施合同'""")
            row = len(result)
            vol = self.tbw_Project.columnCount()
            self.tbw_Project.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Project.setItem(fi, fj, data)
            self.mTabProjectFormat()
        elif tab_name.strip() == '采购询价'.strip():
            self.mTabPurchaseInquiry()
            # 20210507 JerryShang：因某条产品询价后在当前界面就立刻不可见，所以先去除having子句，添加order by子句。
            # 未来此功能建议添加一个picklist来选择查询的范围：全部产品或者是需要询价的产品。
            #result = dbQueryFull("""select t1.id,tp.`Name`, t2.`Name`, t1.brand, t1.model, t1.Market_DT, max(t3.Inquiry_dt) Inquiry_dt
            #from S_GOODS t1 LEFT JOIN S_ACCOUNT t2 on t1.Supppiler_id = t2.id LEFT JOIN S_PRODUCT tp on t1.Prod_id = tp.id left JOIN S_GOODS_INQUIRY t3 on t1.id = t3.Goods_id
            #group by t1.id,tp.`Name`, t2.`Name`, t1.brand, t1.model, t1.Market_DT having Inquiry_dt is null or Inquiry_dt < curdate() - INTERVAL 3 MONTH""")
            result = dbQueryFull("""select t1.id,tp.`Name`, t2.`Name`, t1.brand, t1.model, t1.Market_DT, ifnull(max(t3.Inquiry_dt),DATE('0000-0-0')) Inquiry_dt 
            from S_GOODS t1 LEFT JOIN S_ACCOUNT t2 on t1.Supppiler_id = t2.id LEFT JOIN S_PRODUCT tp on t1.Prod_id = tp.id left JOIN S_GOODS_INQUIRY t3 on t1.id = t3.Goods_id 
            group by t1.id,tp.`Name`, t2.`Name`, t1.brand, t1.model, t1.Market_DT order by Inquiry_dt""")
            row = len(result)
            vol = self.tbw_Purchase_Inquiry.columnCount()
            self.tbw_Purchase_Inquiry.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Inquiry.setItem(fi, fj, data)
            self.mTabPurchaseInquiryFormat()
        elif tab_name.strip() == '采购计划'.strip():
            self.mTabPurchasePlan()
            result = dbQueryFull("""select t1.id,t2.`Name` as "Pjt_Name", t1.`Name`, t3.`Name` as "PartyA" , t4.`Name` as "PartyB", 
	CONCAT(t8.Fst_Name,t8.Lst_Name) as "BL", CONCAT(t6.Fst_Name,t6.Lst_Name) as "PM" ,
	round(sum(itm.Prod_Num * inq.price/inq.Nums)/1000,4), t1.`Status`
from S_ORDER t1 
LEFT JOIN S_PROJECT t2 on t1.Project_id = t2.id
LEFT JOIN S_ACCOUNT t3 on t2.PartyA_id = t3.id
LEFT JOIN S_ACCOUNT t4 on t2.PartyA_id = t4.id
LEFT JOIN S_PROJECT_EMP t5 on t2.id = t5.Project_id and t5.Type = 'PM'
LEFT JOIN S_CONTACT t6 on t5.Emp_id = t6.id 
LEFT JOIN S_PROJECT_EMP t7 on t2.id = t7.Project_id and t7.Type = 'BL'
LEFT JOIN S_CONTACT t8 on t7.Emp_id = t8.id 
LEFT JOIN S_ORDER_ITEM itm on t1.id = itm.Ord_id
LEFT JOIN S_GOODS_INQUIRY inq on itm.Inquiry_id = inq.id 
where t1.Type = '采购计划单'
group by t1.id,t2.`Name`, t1.`Name`, t3.`Name`  , t4.`Name` , 
	CONCAT(t8.Fst_Name,t8.Lst_Name), CONCAT(t6.Fst_Name,t6.Lst_Name) ,t1.`Status`""")
            row = len(result)
            vol = self.tbw_Purchase_Plan.columnCount()
            self.tbw_Purchase_Plan.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Plan.setItem(fi, fj, data)
            self.mTabPurchasePlanFormat()
        elif tab_name.strip() == '采购提醒'.strip():
            self.mTabPurchaseNotice()
            result = dbQueryFull("""SELECT
	itm.id,
	ord.Type,
	-- itm.`status`,
	prod.`Name` AS "Prod_Name",
	prod.Model as "Prod_Model",
	sup.`Name` AS "Sup_Name",
	gds.Brand as "gd_Brand",
	gds.Model as "gd_Model",
	itm.Prod_Num,
	itm.Unit_Name,
	round(itm.Unit_Price/1000,4),
	round(itm.Prod_Num * itm.Unit_Price / 1000,4) AS "Amount",
	ord.plan_dt,
  concat(IF(ord.Comments is null,'',concat(ord.Comments,'/')), IF(itm.Comments is null,'',itm.Comments)) ,ord.Comments
FROM
	S_ORDER ord
	INNER JOIN S_ORDER_ITEM itm ON ord.id = itm.ord_id
	INNER JOIN S_PRODUCT prod ON itm.prod_id = prod.id
	INNER JOIN S_GOODS_INQUIRY inq ON itm.Inquiry_id = inq.id
	INNER JOIN S_GOODS gds ON inq.Goods_id = gds.id
	INNER JOIN S_ACCOUNT sup ON gds.Supppiler_id = sup.id 
WHERE
	ord.Type = '采购申请单' 
	AND ord.`Status` IN ( 'Pending' )
	-- and itm.`status` IN ( 'Pending' )""")
            row = len(result)
            vol = self.tbw_Purchase_Notice.columnCount()
            self.tbw_Purchase_Notice.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Notice.setItem(fi, fj, data)
            self.mTabPurchaseNoticeFormat()
        elif tab_name.strip() == '采购任务'.strip():
            self.mTabPurchaseJob()
            result = dbQueryFull("""select t1.`id`, t1.`No`, t1.`Name`,t2.`Name`, t1.`Create_Time`, t1.`Status`, 'Pending' from S_PURCHASE t1 LEFT JOIN S_ACCOUNT t2 on t1.Supppiler_id = t2.id where t1.Type = '采购任务'""")
            row = len(result)
            vol = self.tbw_Purchase_Job.columnCount()
            self.tbw_Purchase_Job.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Job.setItem(fi, fj, data)
            self.mTabPurchaseJobFormat()
        elif tab_name.strip() == '采购结算'.strip():
            self.mTabPurchasePayment()
            self.tbw_Purchase_Payment.setRowCount(0)
            result = dbQueryFull("""SELECT
	t1.id,
	t1.Return_Date,
	t1.Invoice_Date,
	t1.Invoice_No,
	t1.Amount,
	t1.Tax_Rate,
	t1.Exchange,
	ts.`Name`,
	tb.`Name` 
FROM
	`S_INVOICE` t1
	LEFT JOIN S_ACCOUNT tb ON t1.Buyer_id = tb.id
	LEFT JOIN S_ACCOUNT ts ON t1.Seller_id = ts.id """)
            row = len(result)
            vol = self.tbw_Purchase_Payment.columnCount()
            self.tbw_Purchase_Payment.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Purchase_Payment.setItem(fi, fj, data)
            self.tbw_Purchase_Payment.setAlternatingRowColors(True)
            self.tbw_Purchase_Payment.resizeColumnsToContents()
            self.tbw_Purchase_Payment.resizeRowsToContents()
            self.mTabPurchasePaymentFormat()
        elif tab_name.strip() == '供应商'.strip():
            self.mTabSuppiler()
            # 绑定数据
            result = dbQueryFull(
                "select id,Name,Industry,Scale,Place,'pending','pending' from S_ACCOUNT where id != 0 and Active_Flg = 'Y' and Supppiler_Flg = 'Y'")
            row = len(result)
            vol = self.tbw_Supppiler.columnCount()
            self.tbw_Supppiler.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Supppiler.setItem(fi, fj, data)
            self.mTabSuppilerFormat()
        elif tab_name.strip() == '产品'.strip():
            self.mTabProduct()
            # 绑定数据
            result = dbQueryFull(
                "SELECT p.id, p.TypeA, p.TypeB, p.`Name`, p.Model, p.Origin FROM S_PRODUCT p")
            row = len(result)
            vol = self.tbw_Product.columnCount()
            self.tbw_Product.setRowCount(row)
            for fi in range(row):
                for fj in range(vol):
                    data = QtWidgets.QTableWidgetItem(str(result[fi][fj]))
                    self.tbw_Product.setItem(fi, fj, data)
            self.mTabProductFormat()
        else:
            pass
    ## 槽函数：详单页签切换
    def dTabChange(self, currentIndex):
        tab_name = self.Tab_Detail.tabText(currentIndex)
        # 各详单页签数据填充
        if tab_name.strip() == '客户详情'.strip():
            # 获取当前主页签的选定记录
            self.click_tbw_Account()
        elif tab_name.strip() == '客户项目'.strip():
            self.click_tbw_Account()
        elif tab_name.strip() == '客户合同'.strip():
            self.click_tbw_Account()
        elif tab_name.strip() == '客户联系人'.strip():
            self.click_tbw_Account()
        elif tab_name.strip() == '联系人详情'.strip():
            self.click_tbw_Contact()
        elif tab_name.strip() == '联系人通讯地址'.strip():
            self.click_tbw_Contact()
        elif tab_name.strip() == '联系人项目'.strip():
            self.click_tbw_Contact()
        elif tab_name.strip() == '联系人组织'.strip():
            self.click_tbw_Contact()
        elif tab_name.strip() == '项目详单'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目采购售前单'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目采购计划单'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目立项单'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目采购申请单'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目合同'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目供应商'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目采购订单'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目开票及回款'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '项目干系人'.strip():
            self.click_tbw_Project()
        elif tab_name.strip() == '采购订单'.strip():
            self.click_tbw_Purchase_Job()
        elif tab_name.strip() == '采购合同'.strip():
            self.click_tbw_Purchase_Job()
        elif tab_name.strip() == '采购项目'.strip():
            self.click_tbw_Purchase_Job()
        elif tab_name.strip() == '供应商详情'.strip():
            self.click_tbw_Supppiler()
        elif tab_name.strip() == '供应商合同'.strip():
            self.click_tbw_Supppiler()
        elif tab_name.strip() == '供应商项目'.strip():
            self.click_tbw_Supppiler()
        elif tab_name.strip() == '供应商干系人'.strip():
            self.click_tbw_Supppiler()
        elif tab_name.strip() == '产品详情'.strip():
            self.click_tbw_Product()
        elif tab_name.strip() == '产品供应品'.strip():
            self.click_tbw_Product()
        elif tab_name.strip() == '产品历史报价'.strip():
            self.click_tbw_Product()
        else:
            pass

# 主程序入口
if __name__ == "__main__":
    main_log.mylog()    # 根据全局变量，打开日志文件记录
    app = QApplication(sys.argv)
    main_window = main()
    main_window.setFixedSize(main_window.width(), main_window.height())
    main_window.show()
    sys.exit(app.exec_())
