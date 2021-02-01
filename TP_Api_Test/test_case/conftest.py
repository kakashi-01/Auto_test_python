# -*- coding: utf-8 -*-
# @File : conftest.py
# _author_=feng
# date: 2021/1/13
import requests
import json
import pytest
from TP_Api_Test.tools.Data_preparation_and_cleaning import Loginclass, Query_list
from TP_Api_Test.configs.config import HOST

# 鉴权把头部带上token值
@pytest.fixture(scope="session")
def login_fixture():
    s = requests.Session()
    info = Loginclass(s)
    info.login()
    yield s # 返回的token需要使用，所以需要返回值
    s.close()

# test_Data_element_management.py文件中需要数据清除
@pytest.fixture(scope='session')
def Delete_new_group():
    s = requests.Session()
    info = Loginclass(s)
    info.login()
    yield s
    s.close()
    n = json.loads(Query_list())["data"][0]["children"][-1]["id"]
    url = f"{HOST}api/v1/data/element/group/delete"
    payload = {"id": f"{n}"}
    r = requests.post(url, json=payload)
    # r.encoding = 'unicode_escape'
    # return r.json()


# @pytest.fixture(scope='session',autouse=True) # 整一个包都会执行，scope只作用域
# def start_demo(request):# 这个一个运行该包下，任何一个test文件，都会一开始就执行的操作
#     print('---开始执行自动化测试---') # 数据准备
#
#     # 数据清除操作:删除测试生成的垃圾数据
#     def fin(): # 数据清除，相当于teardown。
#         print('---自动化测试---结束') # 数据清除
#     request.addfinalizer(fin)


