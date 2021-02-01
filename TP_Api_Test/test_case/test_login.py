# -*- coding: utf-8 -*-
# @File : test_login.py
# _author_=feng
# date: 2021/1/13
import pytest
import allure
import json
from TP_Api_Test.Lib.Login_Module.login import Login_TP
from TP_Api_Test.tools.getExcelData import get_excelData
# from tools.getYamlData import get_yaml_data
from TP_Api_Test.tools.logBasic import logger
log = logger()  # 调用自定义封装的log函数

@allure.epic('TP系统')
@allure.feature('登录模块')
@allure.story('登录接口')
@allure.severity('critical')
@pytest.mark.Login(order=1)
class TestLogin:
    # @pytest.mark.parametrize('inData,respData',get_yaml_data('../data/data.yaml'))  # param
    # parametrize('变量'，值)
    @pytest.mark.正常账户密码登陆
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('1登录模块', 2, 2))
    def test_login_a(self, inData, respData):
        # 1- 调用--封装模块
        res = Login_TP().api_login(inData)
        log.info('------##############------------')
        # 2- 断言  实际结果与预期的结果进行比较
        # try:
        #     assert res == json.loads(respData)['token_type']
        # except Exception as err:
        #     log.error(err)  #
        #     raise err  # 抛出异常
        if "access_token" in res:
            assert res["token_type"] == json.loads(respData)["token_type"]
        else:
            assert res["error"] == json.loads(respData)["error"]

    @pytest.mark.异常密码登陆
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('1登录模块', 3, 4))
    def test_login_s1(self, inData, respData):
        # 1- 调用--封装模块
        res = Login_TP().api_login_p(inData)
        log.info('------##############------------')
        # 2- 断言  实际结果与预期的结果进行比较
        try:
            assert res == json.loads(respData)['error']
        except Exception as err:
            log.error(err)  #
            raise err  # 抛出异常

    @pytest.mark.异常账户登陆
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData', get_excelData('1登录模块', 5, 7))
    def test_login_s2(self, inData, respData):
        # 1- 调用--封装模块
        res = Login_TP().api_login_u(inData)
        log.info('------##############------------')
        # 2- 断言  实际结果与预期的结果进行比较
        try:
            assert res == json.loads(respData)['error']
        except Exception as err:
            log.error(err)  #
            raise err  # 抛出异常


    # @allure.story('登录界面')
    # @allure.severity('critical')
    # @allure.description('自动截图')
    # def test_login_image(self):
    #     allure.attach.file(r'../report/test.jpg','我是附件截图的名字',
    #     attachment_type=allure.attachment_type.JPG)

# if __name__ == '__main__':
#     for one in os.listdir('../report/tmp'):  # 列出对应文件夹的数据
#         if 'json' in one:
#             os.remove(f'../report/tmp/{one}')
#     #-s:输出打印信息； -q  简化输出
#     #--alluredir =../report/tmp---生成allure报告需要的源数据
#     pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
#     #allure generate---生成报告
#     #方案二：allure serve---起服务----自动打开浏览器---一般设置默认浏览器
#     os.system('allure serve ../report/tmp')
#     #生成报告
