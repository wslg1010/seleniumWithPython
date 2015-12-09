# -*- coding:utf-8 -*-
__author__ = 'LG'

import os
import sys
import unittest
import HTMLTestRunner
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.logonPage import LogonPage
from pages.questionList import QuestionList
from pages.newQuestion import NewQuestion
from pages.questionPay import QuestionPay
from pages.questionDetail import QuestionDetail
from pages.evaluatePage import EvaluatePage
from operation.operation import Operation
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class quesFlow(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_quesFlow(self):
        pass

if __name__ == "__main__":
    testunit=unittest.TestSuite()        #定义一个单元测试容器
    testunit.addTest(quesFlow("test_sendQues"))  #将测试用例加入到测试容器中
    filename="myAppiumLog.html"        #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)                 #自动进行测试