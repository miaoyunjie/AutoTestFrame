#生成日志类
import logging
import os
import datetime

class Logger(object):
    def logger(self):
        logname = datetime.datetime.now().strftime("%Y-%m-%d")
        logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=os.path.abspath('..')+"/Loggs/"+logname+".log",
                        filemode='a')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
