# -*- coding: utf-8 -*-
# @File : test_System_Management.py
# _author_=feng
# date: 2021/1/22
import json
import allure
import pytest
from TP_Api_Test.Lib.Function_Module.System_Management import SystemManagement
from TP_Api_Test.tools.getExcelData import get_excelData
# from tools.getYamlData import get_yaml_data
from TP_Api_Test.tools.logBasic import logger
log = logger()

@allure.epic('TP系统')
@allure.feature('系统管理模块')
@allure.story('系统管理接口')
@allure.severity('critical')
@pytest.mark.System_Management(order=5)
class TestSystemManagement:
    # @pytest.mark.parametrize('inData,respData',get_yaml_data('../data/data.yaml'))  # param
    # def setup_class(self):
    @pytest.mark.添加用户
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('5系统管理模块', 2, 2))
    def test_Add_user(self, login_fixture, inData, respData):
        res = SystemManagement(login_fixture).Add_user(inData)
        log.info('------##############------------')
        try:
            assert res == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.分配用户角色
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('5系统管理模块', 3, 3))
    def test_Assign_user_roles(self, login_fixture, inData, respData):
        res = SystemManagement(login_fixture).Assign_user_roles()  # 无需传参inData
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.添加角色
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('5系统管理模块', 4, 4))
    def test_Add_role(self, login_fixture, inData, respData):
        res = SystemManagement(login_fixture).Add_role(inData)
        log.info('------##############------------')
        try:
            assert res == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.获取所有按钮
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('5系统管理模块', 5, 5))
    def test_Get_all_buttons(self, login_fixture, inData, respData):
        res = SystemManagement(login_fixture).Get_all_buttons()  # 无需传参inData
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err
