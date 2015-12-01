# -*- coding:utf-8 -*-
__author__ = 'LG'
import os
import unittest
import HTMLTestRunner
from test.test_logon import Logon
from selenium.webdriver.common.by import By
from time import sleep

from appium import webdriver
from pages.logonPage import LogonPage
from operation.operation import Operation

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# suite = unittest.TestLoader().loadTestsFromTestCase(AskAndroidTest)
# unittest.TextTestRunner(verbosity=2).run(suite)
testunit=unittest.TestSuite()        #定义一个单元测试容器
testunit.addTest(Logon("test_login"))  #将测试用例加入到测试容器中
filename="myAppiumLog.html"        #定义个报告存放路径，支持相对路径。
fp=file(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
runner.run(testunit)