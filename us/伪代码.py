# coding=utf-8

import os
import time

from appium import webdriver

PATH = lambda p: os.path.abspath(p)

# 过滤H5控件 by class name
H5list = ["android.webkit.WebView"]

# 获取页面中所有可点击的元素，返回List
def getelement():
    return True

#根据id查询测试记录表，是否是新的一次测试
def isnewtest(times):
    return True

def istestover(times):
     over =False
     iss =True #根据times查询sql是否存在
     if iss :
         print('不是一次新的测试')
         aa =False  # 根据times查询此次测试所有页面已经遍历完毕
         if aa:
            print('所有页面测试已经结束')
            over=True
         else:
             print('所有页面测试未结束')
             over=False
     else:
         print('全新的测试')
         print('测试未结束')
         over=False
     return over


#根据page id 查询当前activity是否测试结束
# 返回一个未点击元素的列表
# 未点击的含义：该元素未点击， 该元素生成的子节点页面未完成。

def ispageover(s):
    return True
    pass

# 判断当前是否是H5
def isH5page():
        h5page = True
        # n = 0
        # for x in H5list:
        #     if driver.find_elements_by_class_name(x).__len__() != 0:
        #         n = n + 1
        # if n != 0:
        #     noth5page = False
        return h5page
# 判断是否仍在被测应用中,需传入当前包名
def isTheTestedApp(theapp):
    isappswich = False
    # if driver.current_package.__eq__(theapp):
    #     isappswich = True
    return isappswich



#新页面
def newpage():
    return  False
    pass


def jump(act):
    pass

#数据库操作
def  sql():
    pass



if __name__ == "__main__":

    testSign = "Android_"+int(time.time())  # 开始测试时的时间戳 作为本次测试的唯一标识

    notover=True
    while notover:
            isover=istestover(testSign)
            if isover:
                print('测试全部结束')
                notover=False
            else:
               if isH5page:
                   # driver.back
                   break
               else:
                   if not isTheTestedApp(""):
                       # driver.start
                        break
                   else:
                       print('测试尚未结束，解析当前页面')
                       getelement()
                       pagesid = 1
                       if newpage():
                           print('当前页面是新页面')
                           sql()
                           print('点击当前页面未点击过的元素')
                           # click()
                       else:
                           print('当前页面是旧的页面')
                           if ispageover(1):
                               print('当前页面元素已经点完了')
                               # driver.back()
                               # print('跳转到未完成的页面')
                               # print('重启应用，  driver.start_activity(theTestedApp, current_activity')
                               # print('点击该页面的父按钮')
                               # # jump(1)

                           else:
                               print('当前页面元素还没点完')
                               print('点击当前页面未点击过的元素')
                               # sql()
                               # click()


    print('test over')
