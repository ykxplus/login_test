import time
import unittest


import app
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from script.login import login_test

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login_test))

report_file = app.Base_Dir + "/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(report_file, "wb") as f:
    runnner = HTMLTestRunner(f, title='p2p测试项目测试报告')
    runnner.run(suite)