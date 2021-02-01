# -*- coding: utf-8 -*-
# @File : test_Data_element_management.py
# _author_=feng
# date: 2021/1/26
import json, requests
import allure
import pytest
from TP_Api_Test.Lib.Function_Module.Data_element_management import DataElementManagement
from TP_Api_Test.tools.getExcelData import get_excelData
# from tools.getYamlData import get_yaml_data
from TP_Api_Test.tools.logBasic import logger
log = logger()


@allure.epic('TP系统')
@allure.feature('数据元管理模块')
@allure.story('数据元管理接口')
@allure.severity('critical')
@pytest.mark.Data_interface_service(order=7)
class TestDataElementManagement:
    # @pytest.mark.parametrize('inData,respData',get_yaml_data('../data/data.yaml'))  # param
    # def setup_class(self):
    @pytest.mark.查询目录树
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('7数据元管理', 2, 2))
    def test_Query_directory_tree(self, login_fixture, inData, respData):
        res = DataElementManagement(login_fixture).Query_directory_tree()  # 无需传参
        r = json.loads(res)
        log.info('------##############------------')
        try:
            assert r["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.新增分组
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('7数据元管理', 3, 3))
    def test_New_group(self, Delete_new_group , inData, respData):
        res = DataElementManagement(Delete_new_group).New_group(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    # @pytest.mark.删除新增分组
    # @allure.title("测试输入：{inData}")
    # @pytest.mark.parametrize('inData,respData', get_excelData('7数据元管理', 4, 4))
    # def test_Delete_new_group(self, login_fixture, inData, respData):
    #     res = DataElementManagement(login_fixture).Delete_new_group(inData)
    #     log.info('------##############------------')
    #     try:
    #         assert res["code"] == json.loads(respData)["code"]
    #     except Exception as err:
    #         log.error(err)
    #         raise err

    @pytest.mark.批量导入
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('7数据元管理', 5, 5))
    def test_Batch_import(self, login_fixture, inData, respData):
        res = DataElementManagement(login_fixture).Batch_import()  # 无需传参inData
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err
