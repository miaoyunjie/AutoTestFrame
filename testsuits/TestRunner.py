#生成测试报告,集成测试用例并执行

import HTMLTestRunner
import os
import unittest
import time
from testsuits.baidu_search import BaiduSearch

report_path = os.path.dirname(os.path.abspath(".")) + '/test_report/'
now = time.strftime("%Y-%m-%d-%H_%M_%S_",time.localtime(time.time()))
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile,"wb")
suite = unittest.TestLoader().discover("testsuits")

if __name__ == "__main__":
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = u"某某项目测试报告",description = u"用例测试情况")
    runner.run(suite)