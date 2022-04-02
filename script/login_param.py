import logging
import unittest
import random

import requests
from parameterized import parameterized

from api.loginApi import loginApi
from util import get_register_data_Utils, assertUtils, get_All_data_Utils


class login_test(unittest.TestCase):

    def setUp(self):
        self.loginApi = loginApi()
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    # @parameterized.expand(get_register_data_Utils("register.json"))
    @parameterized.expand(get_All_data_Utils("register.json", "test_register",
                                             "phone,pwd,imgVerifyCode,phoneCode,dyServer,invite_phone,status_code,status,description"))
    def test01_register(self, phone, pwd, imgVerifyCode, phoneCode, dyServer, invite_phone, status_code, status,
                        description):
        # 1.获取图片验证码成功
        r = random.random()
        # 调用接口类中的接口
        response = self.loginApi.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        # 2.获取短信验证码成功
        response = self.loginApi.getSmsCode(self.session, phone, imgVerifyCode)
        logging.info("获取短信验证码响应{}".format(response.json()))
        assertUtils(self, response, 200, 200, "短信发送成功")
        # 3.注册
        response = self.loginApi.register(self.session,phone, pwd, imgVerifyCode, phoneCode, dyServer, invite_phone)
        # logging.info("查看相应数据 = {}".format(response.url))
        logging.info("注册的响应response = {}".format(response.json()))
        # 对收到的响应进行断言
        assertUtils(self, response, status_code, status, description)
