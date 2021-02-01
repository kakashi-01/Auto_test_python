# -*- coding: utf-8 -*-
# @File : test_Data_Service.py
# _author_=feng
# date: 2021/1/22
import json
import allure
import pytest
from TP_Api_Test.Lib.Function_Module.Data_Service import DataService
from TP_Api_Test.tools.getExcelData import get_excelData
# from tools.getYamlData import get_yaml_data
from TP_Api_Test.tools.logBasic import logger
log = logger()

@allure.epic('TP系统')
@allure.feature('数据服务模块')
@allure.story('数据服务接口')
@allure.severity('critical')
@pytest.mark.Data_Service(order=4)
class TestDataService:
    # @pytest.mark.parametrize('inData,respData',get_yaml_data('../data/data.yaml'))  # param
    # def setup_class(self):
    @pytest.mark.接口调用查询
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('4数据服务模块', 2, 2))
    def test_Interface_query(self, login_fixture, inData, respData):
        res = DataService(login_fixture).Interface_query(inData)
        log.info('------##############------------')
        try:
            assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.接口管理列表
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('4数据服务模块', 3, 3))
    def test_Interface_management(self, login_fixture, inData, respData):
        res = DataService(login_fixture).Interface_management(inData)
        log.info('------##############------------')
        try:
            assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    # @pytest.mark.接口停用
    # @allure.title("测试输入：{inData}")
    # @pytest.mark.parametrize('inData,respData', get_excelData('4数据服务模块', 4, 4))
    # def test_Interface_disabled(self, login_fixture, inData, respData):
    #     res = DataService(login_fixture).Interface_disabled(inData)
    #     log.info('------##############------------')
    #     try:
    #         assert str(res) == json.loads(respData)["code"]
    #     except Exception as err:
    #         log.error(err)
    #         raise err

    @pytest.mark.接口授权查看
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('4数据服务模块', 5, 5))
    def test_Interface_authorization(self, login_fixture, inData, respData):
        res = DataService(login_fixture).Interface_authorization(inData)
        log.info('------##############------------')
        try:
            assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err
