#coding:utf-8
__author__ = 'LG'
import unittest
from selenium import webdriver
from pageObject import loginPage
from pageObject import mainPage
import time

class logonCase(unittest.TestCase):
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

    def runTest(self):
        print 'aaaaaaaaa'

    def test_login(self):
        login = loginPage.loginPage(self._driver)
        login.username('admin')
        login.password('asdf123')
        login.logon()
        keyword = self._driver.find_element_by_class_name('li_login_wrap').text
        self.assertEqual(keyword,u'admin，您好！  [退出]')
    #driver.switch_to.window(driver.window_handles[-1])

    def test_login1(self):
        login = loginPage.loginPage(self._driver)
        login.username('admin')
        login.password('asdf123')
        login.logon()
        keyword = self._driver.find_element_by_class_name('li_login_wrap').text
        self.assertEqual(keyword,u'admin，您好！  [退出]11')

class loginCase1(logonCase):
    def test_login1(self):
        login = loginPage.loginPage(self._driver)
        login.username('admin')
        login.password('asdf123')
        login.logon()
        keyword = self._driver.find_element_by_class_name('li_login_wrap').text
        self.assertEqual(keyword,u'admin，您好！  [退出]')
