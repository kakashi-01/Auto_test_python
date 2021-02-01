# -*- coding: utf-8 -*-
# @File : Data_interface_service.py
# _author_=feng
# date: 2021/1/25
import json
from TP_Api_Test.configs.config import HOST

class DataInterfaceService:
    def __init__(self, s):
        self.s = s

    def API_interface_query(self):  # 无需传参inData
        url = f"{HOST}api/v1/api/develop/tree/list"
        r = self.s.get(url)
        r.encoding = 'unicode_escape'
        return r.json()

    def Interface_group_view(self, inData):
        url = f"{HOST}api/v1/api/develop/tree/group/add"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(url, json=payload)
        r.encoding = 'unicode_escape'
        return r.json()

    def Interface_group_editing(self, inData):
        url = f"{HOST}api/v1/api/develop/tree/group/update"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(url, json=payload)
        r.encoding = 'unicode_escape'
        return r.json()

    def API_time_query(self, inData):
        url = f"{HOST}api/v1/api/develop/apiInfo/timeConsumingList"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.get(url, params=payload)
        r.encoding = 'unicode_escape'
        return r.json()