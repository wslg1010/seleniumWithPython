# -*- coding:utf-8 -*-
__author__ = 'LG'

from appium import  webdriver
from configs.getConfigs import GetConfigs

class DriverFactory():
    def get_driver(self,deviceName,port=4723):
        desired_caps = {}
        for item in GetConfigs().get_configs_by_sec('driver1'):
            desired_caps[item[0]] = item[1]
        print desired_caps
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4.2'
        # desired_caps['deviceName'] = 'H60-L12'
        # desired_caps['appPackage'] = 'com.tj.yy'
        # desired_caps['appActivity'] = '.activity.A001_WelcomeActivity'
        # #输入中文的设置
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        driver = webdriver.Remote('http://localhost:' + port + '/wd/hub', desired_caps)
        return driver
