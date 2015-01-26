#coding:utf-8
__author__ = 'lg'
from selenium import webdriver
from pageObject import loginPage
import time
driver = webdriver.Chrome()

driver.get('http://192.168.0.236')
driver.maximize_window()
login = loginPage.loginPage(driver)

login.username('admin')
login.password('asdf123')
login.logon()

#driver.switch_to.window(driver.window_handles[-1])

#"//a[@herf='/accept_weeks/new']")
#driver.find_element_by_xpath(u"//input[@value='登录系统']").click()
time.sleep(5)

driver.quit()