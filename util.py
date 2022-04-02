import json
import logging
from random import random

import app


def assertUtils(self, response, status_code, status, desc):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(status, response.json().get("status"))
    self.assertEqual(desc, response.json().get("description"))

    # 获取短信验证码成功-参数正确


def get_sms_code_success_Utils(self, response, session, phone, imgVerifyCode):
    # 1、获取图片验证码
    r = random.randint(1, 100000000)
    # 调用接口类中的接口
    response = self.loginApi.getImgCode(session, str(r))
    # 2、获取短信验证码（需要先获取图片）
    # 调用接口类中的发送短信验证码的接口
    response = self.loginApi.getSmsCode(session, phone, imgVerifyCode)
    # 接收接口的返回结果，获取断言
    logging.info(response.json())
    return response


# 读取注册测试用例的接口数据
def get_register_data_Utils(filename):
    # 生成的data的register.json文件，
    file = app.Base_Dir + '/data/' + filename
    test_case_data = []
    with open(file, encoding='utf-8')as f:
        # 将json的数据格式转换为字典
        register_data = json.load(f)
        # 获取所有测试数据的列表
        test_data_list = register_data.get("test_register")
        # 依次读取测试数据列表中的每一条数据
        for test_data in test_data_list:
            test_case_data.append((test_data.get("phone"), test_data.get("pwd"), test_data.get("imgVerifyCode"),
                                   test_data.get("phoneCode"), test_data.get("dyServer"), test_data.get("invite_phone"),
                                   test_data.get("status_code"), test_data.get("status"),
                                   test_data.get("description")))
        print("test_case_data{}".format(test_data_list))
    return test_data


# 定义统一的读取所有参数数据文件的方法
def get_All_data_Utils(filename, method_name, param_name):
    # filename： 参数数据文件的文件名
    #    method_name: 参数数据文件中定义的测试数据列表的名称，如：test_get_img_verify_code
    #    param_names: 参数数据文件一组测试数据中所有的参数组成的字符串，如："type,status_code"
    file = app.Base_Dir + '/data/' + filename
    test_case_data = []
    with open(file, encoding="utf-8")as f:
        # 将json数据转换成列表
        file_list = json.load(f)
        # 获取所有测试数据的列表
        test_data_list = file_list.get(method_name)
        for test_data in test_data_list:
            test_params = []
            for param in param_name.split(","):
                # 依次获取同一组测试数中每个参数的值，添加到test_params中，形成一个列表

                test_params.append(test_data.get(param))
                # 依次获取同一组测试数中每个参数的值，添加到test_params中，形成一个列表
            test_case_data.append(test_params)
    print("test_case_data={}".format(test_case_data))
    return test_case_data
