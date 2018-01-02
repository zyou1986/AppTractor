# coding=utf-8

import os
import time
import _md5
import types
import hashlib
from appium import webdriver
from common import clientdriver
from common import log

import os
import time
import logging
PATH = lambda p: os.path.abspath(p)

# 过滤H5控件 by class name
H5list = ["android.webkit.WebView"]


#MD5
def strmd5(str):
    m2 = hashlib.md5()
    m2.update(str.encode("gb2312"))
    return   m2.hexdigest()

#根据id查询测试记录表，是否是新的一次测试
def isnewtest(times):
    return True

def istestover(times):
     over =False
     iss =True #根据times查询sql是否存在
     if iss :
         logging.info('不是一次新的测试')

         aa =False  # 根据times查询此次测试所有页面已经遍历完毕
         if aa:
            logging.info('所有页面测试已经结束')

            over=True
         else:
             logging.info('所有页面测试未结束')

             over=False
     else:
         logging.info('全新的测试')

         over=False
     return over


#根据page id 查询当前activity是否测试结束
# 返回一个未点击元素的列表
# 未点击的含义：该元素未点击， 该元素生成的子节点页面未完成。

def ispageover(pagesname):
    return False
    pass



#新页面
def newpage(pagesname):
    return  True
    pass

def takename(getelement):
    strlist =""
    pagesname=""
    for x in getelement:
        strlist=strlist+x.text+x.tag_name+str(x.location.get("x"))+str(x.location.get("y"))
    logging.info(strlist)
    md5 =strmd5(strlist)
    logging.info(md5)
    return str(thedriver.current_activity) +'_'+ md5

def jump(act):
    pass

#数据库操作
def  sql():
    pass

def refresh(driver):
    notover = True
    while notover:
        isover = istestover(testSign)
        if isover:
            logging.info('测试全部结束')
            notover = False
        else:
            if driver.isH5page():
                driver.back
                break
            else:
                if not driver.isTheTestedApp(theTestedApp):
                    driver.start
                    break
                else:
                    logging.info('测试尚未结束，解析当前页面')
                    driver.getelement()
                    # strlist =str(driver.getelement())
                    pagesname = takename(driver.getelement())
                    logging.debug("当前页面名称： "+pagesname)
                    if newpage(pagesname):
                        logging.info('当前页面是新页面：'+ pagesname)
                        sql()
                        driver.tap([(550, 550)])
                        logging.info('点击按钮：')
                        time.sleep(0.5)
                        driver.screenshot()  # 点击后截屏                    else:
                    else:
                        logging.info('当前页面是旧的页面')

                        if ispageover(pagesname):
                            logging.info('当前页面元素已经点完了')
                            logging.debug("当前 " + pagesname +"遍历完毕，寻找未完成页面")

                            # driver.back()
                            # print('跳转到未完成的页面')
                            # print('重启应用，  driver.start_activity(theTestedApp, current_activity')
                            # print('点击该页面的父按钮')
                            # # jump(1)

                        else:
                            # sql()
                            # click()
                            driver.tap([(550, 550)])
                            logging.info('点击按钮：')
                            time.sleep(0.5)
                            driver.screenshot()  # 点击后截屏

    logging.info('遍历结束')


if __name__ == "__main__":
    log
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = '/Users/mileszhou/Downloads/aaaa/xdj-3.1.0-test.apk'
    thedriver =clientdriver.ClientDriver('http://localhost:4723/wd/hub', desired_caps)
    thedriver.splashcreen()
    theTestedApp=thedriver.current_package
    testSign = "Android_" + str(int(time.time()))  # 开始测试时的时间戳 作为本次测试的唯一标识
    refresh(thedriver)