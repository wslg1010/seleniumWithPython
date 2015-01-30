#coding:utf-8
__author__ = 'lg'
import unittest
from testCase import logonCase
import time
import HTMLTestRunner

if __name__ =='__main__':
    #unittest.main()
    logon = logonCase.logonCase
    testsuite = unittest.TestSuite()
    #添加测试用例到测试集中
    testsuite.addTest(logon("test_login"))
    # 生成测试报告文件
    filename = 'D:\\result1.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=u'测试结果',
                description=u'测试报告.'
                )
    #runner = unittest.TextTestRunner()
    runner.run(testsuite)