__author__ = 'lg'
class mainPage():
    def __init__(self,driver):
        self._driver = driver
        #self.

    def importDeviceAuto(self):
        self._driver.find_element_by_xpath('/html/body/div[5]/div/p/a/i').click()

    def importDeviceManual(self):
        self._driver.find_element_by_xpath('/html/body/div[5]/div/p/a[2]/i').click()