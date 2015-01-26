#coding:utf-8
__author__ = 'lg'
from selenium import webdriver

class loginPage:
    def __init__(self,driver):
        self._driver = driver
        #self._driver.

    def username(self,username):
        self._driver.find_element_by_name('name').send_keys(username)

    def password(self,password):
        self._driver.find_element_by_name('password').send_keys(password)

    def logon(self):
        self._driver.find_element_by_xpath(u"//input[@value='登录系统']").click()

#driver = webdriver.Chrome()
#driver.switch_to_window()