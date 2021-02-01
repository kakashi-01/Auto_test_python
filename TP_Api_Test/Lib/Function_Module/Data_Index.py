# -*- coding: utf-8 -*-
# @File : Data_Index.py
# _author_=feng
# date: 2021/1/13
import requests
import json
from TP_Api_Test.configs.config import HOST


class DataIndex:
    def __init__(self, s):
        self.s = s

    def Data_list(self, inData):
        index_url = f"{HOST}api/v1/q/sql/task"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(index_url, json=payload)
        r.encoding = 'unicode_escape'
        return r.json()

    def Save_Data(self, inData):
        login_url = f"{HOST}api/v1/tree/saveData"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.post(login_url, json=payload)
        r.encoding = 'unicode_escape'
        return r.json()

    def Export_data(self, inData):
        login_url = f"{HOST}api/v1/q/export/e528a75b-8178-4c2a-9066-66986988652c?"
        # header = {"Authorization": f"bearer {r.json()['access_token']}"}
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = self.s.get(login_url, params=payload)
        # reps.encoding = 'unicode_escape'
        return r.status_code

    def Export_metadata(self, inData):
        login_url = f"{HOST}api/v1/admin/exportIndexMetaData?"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = requests.get(login_url, params=payload)
        # reps.encoding = 'unicode_escape'
        return r.status_code

    # def Filter_metadata(self, inData):
    #     login_url = f"{HOST}api/v1/index /OnlinefilterQuery"
    #     payload = json.loads(inData)  # inData是字符串，转字典传入
    #     r = requests.post(login_url, json=payload)
    #     # reps.encoding = 'unicode_escape'
    #     return r

    def Edit_metadata(self, inData):
        login_url = f"{HOST}api/v1/index/onlineEditMetadataTable"
        payload = json.loads(inData)  # inData是字符串，转字典传入
        r = requests.get(login_url, params=payload)
        # reps.encoding = 'unicode_escape'
        return r.json()

# if __name__ == '__main__':
#
#       print(DataIndex().Export_data())
#       print(type(DataIndex().Export_data()))
