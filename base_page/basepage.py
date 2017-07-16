# -*- coding:utf-8 -*-
#封装页面操作类

import os
import time
import logging
from selenium.common.exceptions import NoSuchElementException
from browser_engine.browser_engine import BrowserEngine

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def back(self):
        self.driver.back()
        logging.info("浏览器后退操作")

    def forward(self):
        self.driver.forward()
        logging.info("浏览器前进操作")

    def open_url(self,url):
        self.driver.get(url)
        logging.info("打开网址")

    def quit_browser(self):
        self.driver.quit()
        logging.info("关闭浏览器")

    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logging.info("隐式等待")

    def close(self):
        try:
            self.driver.close()
            logging.info("点击关闭当前窗口")
        except NameError as e:
            logging.error("关闭当前窗口失败 %s"% e)

    def take_screenshot(self):
        #截图
        #os.mkdir(os.path.abspath('..')+ '/Screenshots/')
        rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screen_name = rq + '.png'
        try:
            self.driver.get_screenshot_as_file(os.path.abspath('..')+'/Screenshots/'+screen_name)
            logging.info("开始截图并保存")
        except Exception as e:
            logging.error("出现异常",format(e))

    def find_element(self,selector):
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == "id":
            try:
                element = self.driver.find_element_by_id(selector_value)
                logging.info("成功发现元素 \' %s \'"
                             "by %s via value: %s" % (element.text,selector_by,selector_value))
            except NoSuchElementException as e:
                logging.error("NoSuchElementException: %s" % e)
        elif selector_by == "n" or selector_by == "name":
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == "class_name":
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == "tag_name":
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == "xpath":
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logging.info("成功发现元素\' %s \'"
                             "by %s via value: %s" %(element.text,selector_by,selector_value))
            except NoSuchElementException as e:
                logging.error("NosuchElementException: %s" % e)
                self.take_screenshot()
        elif selector_by == "s" or selector_by == "selector_seletor":
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def type(self,selector,text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logging.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logging.error("Failed to type in input box with %s" %e)
            self.take_screenshot()

    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logging.info("Clear text in input box before tying.")
        except NameError as e:
            logging.error("Failed to clear input box with %s" % e)
            self.take_screenshot()

    def click_c(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            logging.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logging.error("Failed to click the element with %s" % e)

    def submit_s(self,selector):
        el = self.find_element(selector)
        try:
            el.submit()
            logging.info("The element \' %s \' was submited." % el.text)
        except NameError as e:
            logging.error("Failed to click the element with %s" % e)

    def get_page_title(self):
        logging.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logging.info("Sleep for %d seconds" % seconds)

if __name__ == "__main__":
    asd = BrowserEngine('')
    driver = asd.get_browser()
    a = BasePage(driver)
    a.quit_browser()
    a.sleep(3)