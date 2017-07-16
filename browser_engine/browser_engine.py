#coding=utf-8

#封装一个浏览器类

import logging
from selenium import webdriver
from read_configfile.readconfigfile import ReadConfigFile

class BrowserEngine(object):

    browser_type = ReadConfigFile().get_value()[0]  # 获取浏览器类型
    browser_url = ReadConfigFile().get_value()[1]  # 获取测试地址

    def __init__(self,driver):
        self.driver = driver

    def get_browser(self):
        if self.browser_type == "Firefox":
            driver = webdriver.Firefox()
            logging.info("初始化火狐浏览器")
        elif self.browser_type == "Chrome":
            driver = webdriver.Chrome()
            logging.info("初始化谷歌浏览器")
        elif self.browser_type == "IE":
            driver = webdriver.Ie()
            logging.info("初始化IE浏览器")
        else:
            driver = webdriver.Ie()
            logging.info("初始化IE浏览器")
        driver.maximize_window()
        logging.info("最大化浏览器窗口")
        driver.implicitly_wait(0)
        logging.info("隐式等待10s")
        driver.get(self.browser_url)
        return driver

if __name__ == "__main__":
    abc = BrowserEngine('')
    abc.get_browser()