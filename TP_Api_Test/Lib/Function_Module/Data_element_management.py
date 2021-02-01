# -*- coding: utf-8 -*-
# @File : Data_element_management.py
# _author_=feng
# date: 2021/1/26
import json
from TP_Api_Test.configs.config import HOST
from TP_Api_Test.tools.Data_preparation_and_cleaning import Query_list


class DataElementManagement:
    def __init__(self, s):
        self.s = s
    def Query_directory_tree(self):   # 无需传参inData
        url = f"{HOST}api/v1/data/element/tree/list"
        r = self.s.get(url)
        r.encoding = 'utf-8'
        return r.text

    def New_group(self, inData):
        url = f"{HOST}api/v1/data/element/group/add"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(url , json=payload)
        r.encoding = 'unicode_escape'
        return r.json()

    # def Delete_new_group(self, inData):
    #     n = json.loads(Query_list())["data"][0]["children"][-1]["id"]
    #     url = f"{HOST}api/v1/data/element/group/delete"
    #     payload = {"id": f"{n}"}
    #     r = self.s.post(url , json=payload)
    #     r.encoding = 'unicode_escape'
    #     return r.json()

    def Batch_import(self): # 无需传参inData
        url = f"{HOST}api/v1/data/element/file/upload"
        files = {
            "file": (
                "模板.xlsx",
                open(
                    "../data/模板.xlsx",
                    "rb"),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        # ’..’ 表示py文件当前所处的文件夹上一级文件夹的绝对路径,执行文件在testcase，先到上一级文件夹TP_Api_Test+/data目录
        r = self.s.post(url, files=files)
        r.encoding = 'unicode_escape'
        return r.json()

