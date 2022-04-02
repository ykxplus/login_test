import app
import requests


class loginApi():
    def __init__(self):
        self.getImgCode_url = app.Base_url + '/common/public/verifycode1/'
        self.getSmsCode_url = app.Base_url + '/member/public/sendSms'
        self.register_url = app.Base_url + "/member/public/reg"

    # 获取图片验证码接口   /common/public/verifycode1/{r}    r=参数，通过参数化的形式可以传递进来
    def getImgCode(self, session, r):
        # 定义它的请求url
        url = self.getImgCode_url + r
        response = session.get(url)  # session为了之后用
        print(url)
        return response

    # 获取注册手机验证码接口 Sms
    def getSmsCode(self, session, phone, imgVerifyCode):
        # 准备参数
        '''
        phone="13800002222"
        imgVerifyCode="8888"
        type="reg"
        '''
        data = {'phone': phone, 'imgVerifyCode': imgVerifyCode, 'type': 'reg'}
        # 发送请求
        response = session.post(self.getSmsCode_url, data=data)
        # 返回响应
        return response
        #  七个参数  session   呢
        # def register(self, session, phone, pwd, verifycode="8888", phone_code="666666", dy_server="on",
        #              invite_phone='')

    # def register(self, session, phone,pwd,imgVerifyCode,phoneCode,dyServer,invite_phone,status_code,status,description):
    #     data = {"phone": phone,
    #             " pwd": pwd,
    #             "verifycode": imgVerifyCode,
    #             " phoneCode": phoneCode,
    #             "dy_server": dyServer,
    #             "invite_phone": invite_phone,
    #             "status_code": status_code,
    #             "status": status,
    #             "description": description
    #             }
    #     response = session.post(self.register_url, data)
    #     return response

    def register(self, session, phone, pwd, imgVerifyCode='8888', phoneCode='666666', dyServer='on', invite_phone=''):
        data = {"phone": phone,
                "password": pwd,
                "verifycode": imgVerifyCode,
                "phone_code": phoneCode,
                "dy_server": dyServer,
                'invite_phone': invite_phone}
        response = session.post(self.register_url, data=data)
        return response
