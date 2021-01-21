# -*- coding: utf-8 -*-
# @File : test_Algorithm_Tool.py
# _author_=feng
# date: 2021/1/14
import json
import allure
import pytest
from TP_Api_Test.Lib.Function_Module.Algorithm_Tool import AlgorithmTool
from TP_Api_Test.tools.getExcelData import get_excelData
# from tools.getYamlData import get_yaml_data
from TP_Api_Test.tools.logBasic import logger
log = logger()

@allure.epic('TP系统')
@allure.feature('算法工具模块')
@allure.story('算法工具接口')
@allure.severity('critical')
@pytest.mark.Algorithm_Tool(order=3)
class TestAlgTool:
    # @pytest.mark.parametrize('inData,respData',get_yaml_data('../data/data.yaml'))  # param
    # def setup_class(self):
    @pytest.mark.任务队列查询
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('3算法工具模块', 2, 2))
    def test_Task_query(self, login_fixture, inData, respData):
        res = AlgorithmTool(login_fixture).Task_query(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.算法模型执行
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('3算法工具模块', 3, 3))
    def test_Alg_model(self, login_fixture, inData, respData):
        res = AlgorithmTool(login_fixture).Alg_model(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.获取算法函数
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('3算法工具模块', 4, 4))
    def test_Get_algorithm(self, login_fixture, inData, respData):
        res = AlgorithmTool(login_fixture).Get_algorithm(inData)
        log.info('------##############------------')
        try:
            assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.保存算法模型
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('3算法工具模块', 5, 5))
    def test_Save_Alg_model(self, login_fixture, inData, respData):
        res = AlgorithmTool(login_fixture).Save_Alg_model(inData)
        log.info('------##############------------')
        try:
            assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.算法超市列表
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('3算法工具模块', 6, 6))
    def test_Alg_supermarket(self, login_fixture, inData, respData):
        res = AlgorithmTool(login_fixture).Alg_supermarket(inData)
        log.info('------##############------------')
        try:
            assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err
