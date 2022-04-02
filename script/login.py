import logging
import unittest
import random

import requests
from bs4 import BeautifulSoup
from parameterized import  parameterized
from api.loginApi import loginApi
from util import assertUtils, get_sms_code_success_Utils


class login_test(unittest.TestCase):
    phone1 = '18616298989'
    phone2='18616161616'  #未注册
    pwd="test123"
    imgVerifyCode = '8888'

    def setUp(self):
        # 实例化api
        self.loginApi = loginApi()
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    # 参数为随机整数时，获取图片验证码成功
    def test01_img_code_random_float(self):
        # 定义参数(随机小数)
        r = random.random()
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, str(r))
        # 接收接口的返回结果，获取断言
        self.assertEqual(200, response.status_code)

    # 获取（随机整数）注册图片验证码
    def test02_img_code_random_int(self):
        # 定义参数（随机整数)
        r = random.randint(1, 100000000)
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, str(r))
        # 接收接口的返回结果，获取断言
        self.assertEqual(200, response.status_code)

    # （随机数为空）注册图片验证码失败
    def test03_img_code_param_is_null(self):
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, '')
        # 接收接口的返回结果，获取断言
        self.assertEqual(404, response.status_code)

    # 获取（随机字母）注册图片验证码失败
    def test04_img_code_param_is_null(self):
        # 定义参数（随机整数)
        r = random.sample('abcdefghijklmnopqrstuvwxyz', 9)
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, str(r))
        # 接收接口的返回结果，获取断言
        self.assertEqual(404, response.status_code)

    # 随机数为字符串）·获取注册图片验证码失败
    def test04_img_code_param_is_null(self):
        # 定义参数（随机整数)
        r = random.sample('abcdefghijklmnopqrstuvwxyz', 9)
        rand = ''.join(r)  # 通过拼接方式
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, rand)
        # 接收接口的返回结果，获取断言
        self.assertEqual(400, response.status_code)

    # 获取短信验证码成功-参数正确
    def test05_get_sms_code_success(self):
        # 1、获取图片验证码
        r = random.randint(1, 100000000)
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, str(r))
        # 接收接口的返回结果，获取断言
        self.assertEqual(200, response.status_code)

        # 2、获取短信验证码（需要先获取图片）
        # 定义参数（正确的手机号和验证码)
        # 调用接口类中的发送短信验证码的接口
        response = self.loginApi.getSmsCode(self.session, self.phone1, self.imgVerifyCode)
        # 接收接口的返回结果，获取断言
        logging.info(response.json())
        assertUtils(self, response, 200, 200, "短信发送成功")

    # 获取短信验证码失败-图片验证码错误
    def test06_get_sms_code_failed(self):
        # 1、获取图片验证码
        r = random.randint(1, 100000000)
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, str(r))
        # 接收接口的返回结果，获取断言
        self.assertEqual(200, response.status_code)
        # 1、获取错误的图片验证码
        # 2.获取验证码失败，-图片错误
        error_imgcode = '1212'
        # 定义参数（正确的手机号和验证码)
        response = self.loginApi.getSmsCode(self.session, self.phone1, error_imgcode)
        # 接收接口的返回结果，获取断言
        assertUtils(self, response, 200, 100, "图片验证码错误")

    # 获取短信验证码失败-图片验证码为空
    def test07_get_sms_code_imgcode_isnull(self):
        # 1、获取图片验证码
        r = random.randint(1, 100000000)
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, str(r))
        # 接收接口的返回结果，获取断言
        self.assertEqual(200, response.status_code)
        # 2.获取验证码失败，图片验证码为空

        # 定义参数（正确的手机号和验证码  )
        response = self.loginApi.getSmsCode(self.session, self.phone1, '')
        # 接收接口的返回结果，获取断言
        assertUtils(self, response, 200, 100, "图片验证码错误")

    # 失败·获取注册短信验证码（手机号为空）
    def test08_get_sms_code_number_isnull(self):
        # 1、获取图片验证码
        r = random.randint(1, 100000000)
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, str(r))
        # 接收接口的返回结果，获取断言
        self.assertEqual(200, response.status_code)

        # 定义参数（正确的手机号和验证码  )
        response = self.loginApi.getSmsCode(self.session, '', self.imgVerifyCode)
        # 接收接口的返回结果，获取断言
        assertUtils(self, response, 200, 100, "图片验证码错误")

    # 失败·获取注册短信验证码（不获取图片验证码）
    def test08_get_sms_code_number_isnull(self):

        # 定义参数（正确的手机号和验证码  )
        response = self.loginApi.getSmsCode(self.session, self.phone1, self.imgVerifyCode)
        # 接收接口的返回结果，获取断言
        assertUtils(self, response, 200, 100, "图片验证码错误")


    #输入必填项，注册成功
    def test09_register_params_mustin(self):

        #2.成功获取短信验证码
        get_sms_code_success_Utils(self.session,self.phone2,self.imgVerifyCode)
        #3.前提手机号未注册
        response=self.loginApi.register(self.session,self.phone2,self.pwd)
        logging.info("register code response = {}".format(response.json()))
        assertUtils(self,response,200,200,'注册成功')




