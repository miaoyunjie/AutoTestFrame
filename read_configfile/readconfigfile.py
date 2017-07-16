# -*- coding:utf-8 -*-
#读取配置文件

import configparser
import os

class ReadConfigFile(object):
    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))
        config = configparser.ConfigParser()
        file_path = root_dir + '/config/config.ini'
        file_open = open(file_path)
        config.readfp(file_open)

        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")
        return (browser, url)