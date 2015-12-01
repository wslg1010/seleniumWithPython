# -*- coding:utf-8 -*-
__author__ = 'LG'
import os
import unittest
import HTMLTestRunner

from test.test_sendQues import sendQuen

# print "****************"
# testsuite=unittest.TestSuite()        #将测试用例加入到测试容器中
# # testsuite.addTest(sendQuen("test_send"))
# suite = unittest.TestLoader().loadTestsFromTestCase(sendQuen)
# fp = file('testResult.html','wb')
# runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='WenA',description='WenA Description')
# runner.run(suite)

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
#单个功能点测试
test_path = PATH('test')

#流程测试
#test_path = PATH('workFlows')

result_path = PATH('result\log.txt')
html_result_path = PATH('result\lResult.html')
#--with-xunit --xunit-file={result_path}
cmd = "nosetests-2.7 {test_path} --cover-html --cover-html-dir={html_result_path}" .format(result_path=result_path, test_path=test_path, html_result_path=html_result_path)
print cmd
os.system(cmd)
