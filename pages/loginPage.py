#coding:utf-8
__author__ = 'LG'

from operation.operation import Operation
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage():
    usernameEdit = lambda self,driver: driver.find_element_by_id('idInput')
    passworfEdit = lambda self,driver: driver.find_element_by_id('pwdInput')
    loginButton = lambda self,driver: driver.find_element_by_id('loginBtn')

    def logon(self,driver,username,password):
        self.waiting_for_logon_page(driver)
        print u'输入用户名！'
        self.usernameEdit(driver).send_keys(username)
        print u'输入密码！'
        self.passworfEdit(driver).send_keys(password)
        print u'点击登录按钮！'
        self.loginButton(driver).click()

    def waiting_for_logon_page(self,driver, time=30):
        Operation().wait_for_element(driver, By.ID, 'idInput', time)


