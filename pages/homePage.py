#coding:utf-8
__author__ = 'LG'

from operation.operation import Operation
from selenium.webdriver.common.by import By
from time import sleep

class HomePage():
    receiveBtn = lambda self,driver: driver.find_element_by_id('_mail_component_59_59')

    def receive_letter(self,driver):
        print u'收信'
        self.receiveBtn(driver).click()

    def waiting_for_home_page(self,driver, time=30):
        Operation().wait_for_element(driver, By.ID, 'spnUid', time)


    def make_sure_is_home_page(self,driver):
        return driver.find_element_by_id('spnUid').text == 'testswp@163.com'