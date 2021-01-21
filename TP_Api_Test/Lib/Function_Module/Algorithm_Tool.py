# -*- coding: utf-8 -*-
# @File : Algorithm_Tool.py
# _author_=feng
# date: 2021/1/14
import requests
import json
from TP_Api_Test.configs.config import HOST


class AlgorithmTool:
    def __init__(self, s):
        self.s = s

    def Task_query(self, inData):
        url = f"{HOST}api/v1/nc/message-center/api/messages"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.get(url, params=payload)
        r.encoding = 'unicode_escape'
        return r.json()

    def Alg_model(self, inData):
        url = f"{HOST}api/v1/job/script/task"
        # 1- 操作查询--需要token(fixture前置操作用r拿token)
        # header = {"content-type": "application/json",
        #           "Authorization": f"bearer {r.json()['access_token']}"}  # 请求头
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(url, json=payload)
        r.encoding = 'unicode_escape'
        return r.json()

    def Get_algorithm(self, inData):
        url = f"{HOST}api/v1/tree/func/7929dabb24cbfff42b58231111a75ce4"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.get(url, params=payload)
        r.encoding = 'unicode_escape'
        return r.status_code

    def Save_Alg_model(self, inData):
        url = f"{HOST}api/v1/query/model"
        # 1- 操作查询--需要token(fixture前置操作用r拿token)
        # header = {"content-type": "application/json",
        #           "Authorization": f"bearer {r.json()['access_token']}"}  # 请求头
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(url, json=payload)
        r.encoding = 'unicode_escape'
        return r.status_code

    def Alg_supermarket(self, inData):
        url = f"{HOST}api/v1/algo/page"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.get(url, params=payload)
        r.encoding = 'unicode_escape'
        return r.status_code
