# -*- coding: utf-8 -*-
# @File : test_Data_Index.py
# _author_=feng
# date: 2021/1/13
import json
import allure
import pytest
from TP_Api_Test.Lib.Function_Module.Data_Index import DataIndex
from TP_Api_Test.tools.getExcelData import get_excelData
# from tools.getYamlData import get_yaml_data
from TP_Api_Test.tools.logBasic import logger
log = logger()  # 调用自定义封装的log函数


@allure.epic('TP系统')
@allure.feature('数据指数模块')
@allure.story('数据指数接口')
@allure.severity('critical')
@pytest.mark.Data_Index(order=2)
class TestDataIndex:  # 测试用例类
    # @pytest.mark.parametrize('inData,respData',get_yaml_data('../data/data.yaml'))  # param
    # def setup_class(self):
    @pytest.mark.指数数据查询  # 加标签
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('2指数模块', 2, 2))
    def test_DataList(self, login_fixture, inData, respData):
        ''' case description:查看指标数据库中的数据 '''
        res = DataIndex(login_fixture).Data_list(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err  # 抛出异常

    @pytest.mark.数据保存  # 加标签
    @allure.title("测试输入：{inData}")
    @pytest.mark.skip(reason="需要先删除已有数据才可保存成功")
    @pytest.mark.parametrize('inData,respData', get_excelData('2指数模块', 3, 3))
    def test_saveData(self, login_fixture, inData, respData):
        # s = login_fixture
        res = DataIndex(login_fixture).Save_Data(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
            return True
        except Exception as err:
            log.error(err)
            raise err  # 抛出异常

    @pytest.mark.数据导出  # 加标签
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('2指数模块', 4, 4))
    def test_Exportdata(self, login_fixture, inData, respData):
        # s = login_fixture
        res = DataIndex(login_fixture).Export_data(inData)
        log.info('------##############------------')
        try:
            assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err  # 抛出异常

    @pytest.mark.元数据导出  # 加标签
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('2指数模块', 5, 5))
    def test_Export_metadata(self, inData, respData):
        # 此接口不需要鉴权，所以可不传login_fixture.功能函数需要加上requests请求（Data_Index.py中）
        res = DataIndex(self).Export_metadata(inData)
        log.info('------##############------------')
        try:
            assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err  # 抛出异常

    # @pytest.mark.筛选元数据表  # 加标签
    # @allure.title("测试输入：{inData}")
    # @pytest.mark.parametrize('inData,respData', get_excelData('2指数模块', 6, 6))
    # def test_Filter_metadata(self, login_fixture, inData, respData):
    #     s = login_fixture
    #     res = DataIndex(s).Filter_metadata(inData)
    #     log.info('------##############------------')
    #     try:
    #         assert res["code"] == json.loads(respData)["code"]
    #     except Exception as err:
    #         log.error(err)
    #         raise err  # 抛出异常

    @pytest.mark.编辑元数据  # 加标签
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('2指数模块', 7, 7))
    def test_Edit_metadata(self, login_fixture, inData, respData):
        # s = login_fixture
        res = DataIndex(login_fixture).Edit_metadata(inData)
        log.info('------##############------------')
        try:
            assert res["code"] == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err  # 抛出异常

# if __name__=="__main__":
#     pytest.main(['-s'])
