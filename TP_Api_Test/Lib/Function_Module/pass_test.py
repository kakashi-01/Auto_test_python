# -*- coding: utf-8 -*-
# @File : pass_test.py
# _author_=feng
# date: 2021/1/13
import requests
from TP_Api_Test.configs.config import HOST
from TP_Api_Test.Lib.Login_Module.login_token import g_token


def Export_metadata():
    url = f"{HOST}api/v1/q/export/e528a75b-8178-4c2a-9066-66986988652c?name=行人特征表_2021年1月13日16时8分57秒&ext=csv"
    # payload = {"order":1,"page":0,"size":12}  # inData是字符串，转字典传入
    header = {"Authorization": f"bearer {g_token()}"}
    reps = requests.get(url,  headers=header)
    reps.encoding = 'unicode_escape'
    return reps

if __name__ == '__main__':
    a=Export_metadata()
    print(a)
    print(type(a))
#     print(Export_metadata())
#     print(type(Export_metadata()))
