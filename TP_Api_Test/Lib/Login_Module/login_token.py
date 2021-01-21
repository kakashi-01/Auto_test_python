# -*- coding: utf-8 -*-
# @File : login_token.py
# _author_=feng
# date: 2021/1/13
import requests
import json
import allure
from TP_Api_Test.configs.config import HOST


class Loginclass():
    def __init__(self, s):
        self.s = s

    @allure.step("登录")
    def login(self,):
        login_url = f'{HOST}api/v1/sys/oauth/token'
        # 1.构造请求消息体
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic emhhbmppYW5nLXNzby10ZXN0OmFhYTQ0ZjI3LTc0MmYtNDMzMS05ZTA0LTllMDFmMGE1MmVjNg=='}
        # 2.构造请求消息体：口诀2
        payload = {
            "grant_type": "password",
            "username": "17688701458",
            "password": "Sutpc@2020",
            "imageCode": "9527"}
        # # 3.发送Post请求
        r = self.s.post(login_url, headers=header, data=payload)
        token = r.json()['access_token']
        h = {"Authorization": "bearer" + token}
        self.s.headers.update(h)
        return r

# if __name__ == '__main__':
#       a = get_token()
#       print(a)
