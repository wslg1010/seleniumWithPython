#coding:utf-8
__author__ = 'lg'
import unittest
from selenium import webdriver
from pageObject import loginPage
from testCase import logonCase
import time
import HTMLTestRunner

class CMCCCloud(unittest.TestCase):
    def setUp(self):
        #pass
        driver = webdriver.Chrome()
        driver.get('http://192.168.0.236')
        #窗口最大化
        driver.maximize_window()
        self._driver = driver

    def tearDown(self):
        time.sleep(5)
        self._driver.quit()

    def test_login(self):
        login = loginPage.loginPage(self._driver)
        login.username('admin')
        login.password('asdf123')
        login.logon()
        keyword = self._driver.find_element_by_class_name('li_login_wrap').text
        self.assertEqual(keyword,u'admin，您好！  [退出]')
    #driver.switch_to.window(driver.window_handles[-1])
    # main = mainPage.mainPage(driver)
    #
    # main.importDeviceManual()
if __name__ =='__main__':
    #unittest.main()
    #print CMCCCloud('test_login')
    logon = logonCase.logonCase
    #print logon("test_login")
    testsuite = unittest.TestSuite()
    #添加测试用例到测试集中
    testsuite.addTest(logon("test_login"))
    # 生成测试报告文件
    print CMCCCloud('test_login')
    filename = 'D:\\result1.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=u'测试结果',
                description=u'测试报告.'
                )
    #runner = unittest.TextTestRunner()
    runner.run(testsuite)