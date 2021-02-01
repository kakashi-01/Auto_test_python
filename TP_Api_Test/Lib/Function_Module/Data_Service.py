# -*- coding: utf-8 -*-
# @File : Data_Service.py
# _author_=feng
# date: 2021/1/22
import json
from TP_Api_Test.configs.config import HOST


class DataService:
    def __init__(self, s):
        self.s = s

    def Interface_query(self, inData):
        url = f"{HOST}api/v1/sys/openman/v2/records"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.get(url, params=payload)
        r.encoding = 'unicode_escape'
        return r.status_code

    def Interface_management(self, inData):
        url = f"{HOST}api/v1/sys/openman/apis"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.get(url, params=payload)
        r.encoding = 'unicode_escape'
        return r.status_code

    # def Interface_disabled(self, inData):
    #     url = f"{HOST}api/v1/sys/openman/apis/updateIsEnableByIds"
    #     payload = json.loads(inData)  # inData是字符串，转字典传入
    #     r = self.s.get(url, params=payload)
    #     r.encoding = 'unicode_escape'
    #     return r.status_code

    def Interface_authorization(self, inData):
        url = f"{HOST}api/v1/sys/openman/authorizations"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.get(url, params=payload)
        r.encoding = 'unicode_escape'
        return r.status_code
