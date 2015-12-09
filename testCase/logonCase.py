#coding:utf-8
__author__ = 'LG'
import unittest
from selenium import webdriver
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from drivers.driverFactory import DriverFactory
import time

class LogonCase(unittest.TestCase):
    def setUp(self):
        #pass
        self._driver = DriverFactory().get_driver('Firefox')
        self._driver.get('http://mail.163.com')
        #窗口最大化
        self._driver.maximize_window()
    def tearDown(self):
        time.sleep(5)
        self._driver.quit()

    def test_login(self):
        login = LoginPage().logon(self._driver,'testswp','A111111')
        HomePage().waiting_for_home_page(self._driver)
        self.assertTrue(HomePage().make_sure_is_home_page(self._driver))
    #driver.switch_to.window(driver.window_handles[-1])
