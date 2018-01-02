import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='app1.log',
                    filemode='w')

#################################################################################################
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

logging.debug('《--欢迎使用测试一针灵，一针灵---有病治病没病强身，用了一针灵，bug亩产一千八--》')
logging.debug('《--感谢周游、张文俊的工作--》')
logging.debug('《--感谢领导，公司的支持--》')
logging.debug('《--感谢所有人给我这次测试的机会--》')
logging.debug('《--联系www.huijie.com ，领取精致新年大礼，开启梦幻面基旅程--》')
logging.debug('《--惠借---掌握核心科技，阿迈瑞肯，上帝压狗--》')
logging.debug('《--开始测试啦，黑喂狗，汪涵--》')










