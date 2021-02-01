# -*- coding: utf-8 -*-
# @File : test_Data_interface_service.py
# _author_=feng
# date: 2021/1/25
import json
import allure
import pytest
from TP_Api_Test.Lib.Function_Module.Data_interface_service import DataInterfaceService
from TP_Api_Test.tools.getExcelData import get_excelData
# from tools.getYamlData import get_yaml_data
from TP_Api_Test.tools.logBasic import logger
log = logger()

@allure.epic('TP系统')
@allure.feature('数据接口服务模块')
@allure.story('数据接口服务接口')
@allure.severity('critical')
@pytest.mark.Data_interface_service(order=6)
class TestDataInterfaceService:
    # @pytest.mark.parametrize('inData,respData',get_yaml_data('../data/data.yaml'))  # param
    # def setup_class(self):
    @pytest.mark.API接口查询
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('6数据接口服务', 2, 2))
    def test_Interface_query(self, login_fixture, inData, respData):
        res = DataInterfaceService(login_fixture).API_interface_query()  # 无需传参inData
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.接口分组查看
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('6数据接口服务', 3, 3))
    def test_Interface_group_view(self, login_fixture, inData, respData):
        res = DataInterfaceService(login_fixture).Interface_group_view(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.接口分组编辑
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('6数据接口服务', 4, 4))
    def test_Interface_group_editing(self, login_fixture, inData, respData):
        res = DataInterfaceService(login_fixture).Interface_group_editing(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.API时耗列表查询
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('6数据接口服务', 5, 5))
    def test_API_time_query(self, login_fixture, inData, respData):
        res = DataInterfaceService(login_fixture).API_time_query(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

