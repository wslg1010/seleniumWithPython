#coding:utf-8
__author__ = 'LG'

from operation.operation import Operation
from selenium.webdriver.common.by import By
from time import sleep

class LogonPage():
    usernameEdit = lambda self,driver: driver.find_element_by_id('com.tj.yy:id/telEdit')
    passworfEdit = lambda self,driver: driver.find_element_by_id('com.tj.yy:id/passEdit')
    logonButton = lambda self,driver: driver.find_element_by_id('com.tj.yy:id/loginBtn')

    def logon(self,driver,username,password):
        self.waiting_for_logon_page(driver)
        print u'输入用户名！'
        self.usernameEdit(driver).send_keys(username)
        print u'输入密码！'
        self.passworfEdit(driver).send_keys(password)
        print u'点击登录按钮！'
        self.logonButton(driver).click()
        sleep(5)
        if Operation().is_element_present(driver,By.NAME,u'版本更新'):
            print u'取消更新'
            driver.find_element_by_id('com.tj.yy:id/cancelBtn').click()

    def waiting_for_logon_page(self,driver, time=30):
        Operation().wait_for_element(driver, By.ID, 'com.tj.yy:id/loginBtn', time)


