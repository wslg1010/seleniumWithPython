__author__ = 'lg'
class mainPage():
    def __init__(self,driver):
        self.driver = driver

    def exportDevice(self):
        self._driver.find_element_by_xpath('/html/body/div[5]/div/p/a/i').click()