# -*- coding: utf-8 -*-
# @File : System_Management.py
# _author_=feng
# date: 2021/1/22
import json
from TP_Api_Test.configs.config import HOST


class SystemManagement:
    def __init__(self, s):
        self.s = s

    def Add_user(self, inData):
        url = f"{HOST}api/v1/sys/user/saveObject"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(url, data=payload)
        r.encoding = 'unicode_escape'
        return r.status_code

    def Assign_user_roles(self):  # 无需传参inData
        url = f"{HOST}api/v1/sys/role/findObjects"
        r = self.s.post(url)
        r.encoding = 'unicode_escape'
        return r.json()

    def Add_role(self, inData):
        url = f"{HOST}api/v1/sys/role/saveObject"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(url, data=payload)
        r.encoding = 'unicode_escape'
        return r.status_code

    def Get_all_buttons(self):  # 无需传参inData
        url = f"{HOST}api/v1/sys/menu/getAllMenus"
        # payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(url)
        r.encoding = 'unicode_escape'
        return r.json()
