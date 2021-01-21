# -*- coding: utf-8 -*-
# @File : testLogin.py
# _author_=feng
# date: 2021/1/14
import xlrd
from TP_Api_Test.Lib.Login_Module.login import Login_TP
from TP_Api_Test.test_case.test_Data_Index import TestDataIndex
from TP_Api_Test.Lib.Function_Module.Algorithm_Tool import AlgorithmTool
from TP_Api_Test.tools.getExcelData import get_excelData, set_excelData
from TP_Api_Test.test_case.conftest import login_fixture

workBookNew = set_excelData()
# 拿到复制的文件对象

workSheetNew = workBookNew.get_sheet(0)
dataList = get_excelData('1登录模块', 2, 7)  # [(请求body，响应数据),(),()]
for one in range(0, len(dataList)):  # one---元组--(请求body，响应数据)
    res = Login_TP().api_login(dataList[one][0])  # 实际响应结果
            # 预期与实际的响应数据进行比较
    if res == "bearer"or "unauthorized" or "invalid_grant" :
                            # 列表.index(元素)---求出该元素的下标
        workSheetNew.write(one + 1, 12, 'pass')  # (行号，列号，字符串内容)
    else:
        workSheetNew.write(one + 1, 12, 'fail')


# workSheetNew = workBookNew.get_sheet(1)
# dataList = get_excelData('2指数模块', 2, 2)  # [(请求body，响应数据),(),()]
# for one in range(0, len(dataList)):  # one---元组--(请求body，响应数据)
#     res = TestDataIndex().test_DataList(login_fixture , inData=dataList[one][0], respData=dataList[one][1])
#         # 预期与实际的响应数据进行比较
#     if res is True:
#         print('---pass---')
#         workSheetNew.write(one + 1, 12, 'pass')  # (行号，列号，字符串内容)
#     else:
#         print('---fail---')
#         workSheetNew.write(one + 1, 12, 'fail')


workBookNew.save('../report/res.xls')

# 3- 写结果
