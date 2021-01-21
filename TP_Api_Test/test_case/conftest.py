# -*- coding: utf-8 -*-
# @File : conftest.py
# _author_=feng
# date: 2021/1/13
import requests
import pytest
import xlrd
from xlutils.copy import copy
from TP_Api_Test.configs.config import HOST
from TP_Api_Test.Lib.Login_Module.login_token import Loginclass


@pytest.fixture(scope="session")
def login_fixture():
    s = requests.Session()
    info = Loginclass(s)
    info.login()
    yield s
    s.close()

@pytest.fixture(scope="session")
def set_excelData():
    # 1-excel表路径
    excelDir = '../data/TP_接口自动化测试用例V1.1.xls'
    # 2- 打开excel对象--formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)
    workBookNew = copy(workBook)  # 复制一个新excel文件对象
    # workSheetNew = workBookNew.get_sheet(n)
    # 取复制出来的新excel文件对象的第一个子表
    workBookNew.save(r'../report/res.xls')
    return workBookNew

# @pytest.fixture(scope='session', autouse=True)  # 整一个包都会执行，scope只作用域
# def get_token():
#     login_url = f'{HOST}api/v1/sys/oauth/token'
#     # 1.构造请求消息体
#     header = {'Content-Type': 'application/x-www-form-urlencoded',
#               'Authorization': 'Basic emhhbmppYW5nLXNzby10ZXN0OmFhYTQ0ZjI3LTc0MmYtNDMzMS05ZTA0LTllMDFmMGE1MmVjNg=='}
#     # 2.构造请求消息体：口诀2
#     payload = {"grant_type":"password", "username":"17688701458", "password":"Sutpc@2020",
#              "cid":"dd7e5924-b5b4-4a0b-b269-66f11ef92b16", "scope":"all", "imageCode":"9527"}
#     # # 3.发送Post请求
#     r = requests.post(login_url, headers=header, data=payload)
#     # print(r.json()['access_token'])
#
#     return r

# @pytest.fixture(scope='session',autouse=True) # 整一个包都会执行，scope只作用域
# def start_demo(request):# 这个一个运行该包下，任何一个test文件，都会一开始就执行的操作
#     print('---开始执行自动化测试---') # 数据准备
#
#     # 数据清除操作:删除测试生成的垃圾数据
#     def fin(): # 数据清除，相当于teardown。
#         print('---自动化测试---结束') # 数据清除
#     request.addfinalizer(fin)

# 那么环境初始化，是否可以测试人员手动调用？---可以的
# @pytest.fixture(scope='function')
# def update_shop_init():#更新商铺的环境初始化
#     #1- 登录---setup_class---已经在类初始化做了--这边不需要做
#     print('---我的作用是商铺更新的初始化操作---')
#     #1- 登录成功
#     token = Login().login({"username":"sq0777","password":"xintian"},getToken=True)
#     #2- 列出商铺--id
#     shopId=MyShop(token).shop_list({'page':1,'limit':20})['data']['records'][0]['id']
#     #3-文件上传
#     imageInfo = MyShop(token).file_upload('123.png','../data/123.png')
#     return shopId,imageInfo#元组类型
