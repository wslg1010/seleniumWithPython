#coding:utf-8
__author__ = 'lg'
from selenium import webdriver
from pageObject import loginPage
from pageObject import mainPage
import time
driver = webdriver.Chrome()

driver.get('http://192.168.0.236')
driver.maximize_window()
login = loginPage.loginPage(driver)

login.username('admin')
login.password('asdf123')
login.logon()

#driver.switch_to.window(driver.window_handles[-1])
mPage = mainPage.mainPage(driver)

mPage.importDeviceManual()
time.sleep(5)

driver.quit()