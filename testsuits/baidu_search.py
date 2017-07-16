# coding = utf-8
#unittest测试框架,执行测试

import time
import unittest
import logging
from logs.logger import Logger
from browser_engine.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import Homepage

class BaiduSearch(unittest.TestCase):

    Logger().logger()

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.get_browser()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search(self):
        for element in ("selenium","python"):
            homepage = Homepage(self.driver)
            homepage.type_search(element)
            homepage.send_submit_btn()
            time.sleep(2)
            try:
                assert element in homepage.get_page_title()
                logging.info('Test Pass.')
            except Exception as e:
                logging.error('Test Fail. %s' % e)

    def test_baidu_search2(self):
        homepage = Homepage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        try:
            assert 'python' in homepage.get_page_title()
            logging.info('Test Pass.')
        except Exception as e:
            logging.error('Test Fail. %s' % e)
