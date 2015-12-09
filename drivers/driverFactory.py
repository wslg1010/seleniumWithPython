# -*- coding:utf-8 -*-
__author__ = 'LG'

from selenium import  webdriver
from configs.getConfigs import GetConfigs

class DriverFactory():
    def get_driver(self,browerType):
        driver = webdriver.Firefox()
        return driver
