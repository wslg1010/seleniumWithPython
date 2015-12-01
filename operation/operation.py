# -*- coding:utf-8 -*-
__author__ = 'LG'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import  sleep

class Operation():
    #页面滑动
    def swipeRightToLeft(self, driver):
        windowSize = driver.get_window_size()
        width = windowSize['width']
        heigth = windowSize['height']
        driver.swipe(width * 3/4, heigth/2, width * 1/4, heigth/2, 0)

    #判断元素是否存在
    def is_element_present(self, driver, how, what):
        try: driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    #等待元素出现
    def wait_for_element(self, driver, how, what, time=30):
        count = 1
        while not self.is_element_present(driver, how, what):
            if count < time:
                print u'等待中，请稍后...'
                sleep(1)
            else:
                print u'等待超时，程序退出...'
                driver.quit()
