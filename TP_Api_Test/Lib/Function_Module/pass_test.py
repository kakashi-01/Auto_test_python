# -*- coding: utf-8 -*-
# @File : pass_test.py
# _author_=feng
# date: 2021/1/13
import requests ,json , re
from TP_Api_Test.configs.config import HOST
from TP_Api_Test.Lib.Login_Module.get_token import login

# def Export_metadata():
#     url = f"{HOST}api/v1/data/element/group/delete"
#     header = {"Authorization": f"bearer {login()}"}
#     payload ={"id": 940}
#     reps = requests.post(url , headers=header , json=payload)
#     reps.encoding = 'utf-8'
#     return reps.json()
#
# if __name__ == '__main__':
#     a = Export_metadata()
#     print(a)
#     print(type(a))

# def Query_list():
#     url = f"{HOST}api/v1/data/element/tree/list"
#     header = {"Authorization": f"bearer {login()}"}
#     reps = requests.get(url , headers=header )
#     reps.encoding = 'utf-8'
#     return reps.text
#
# if __name__ == '__main__':
#     r=json.loads(Query_list())["data"][0]["children"][-1]["id"]
#     print(r)
#     print(type(r))
