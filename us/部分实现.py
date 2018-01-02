# # coding=utf-8
#
# import os
# import time
# import HybridAndroidDriver
# from appium import webdriver
#
# PATH = lambda p: os.path.abspath(p)
#
# # 过滤H5控件 by class name
# H5list = ["android.webkit.WebView"]
#
# #不测试的控件，例如系统控件
# ignoreEl =["android.widget.NumberPicker"]
#
# # 向左滑动屏幕
# def swipeToLeft():
#     size = driver.get_window_size()
#     xstart = size.get("width") / 4 * 3
#     ystart = size.get("height") / 2
#     xend = size.get("width") / 4
#     yend = size.get("height") / 2
#     driver.swipe(xstart, ystart, xend, yend)
#     time.sleep(1)
#
#
# # 向右滑动屏幕
# def swipeToRight():
#     size = driver.get_window_size()
#     xstart = size.get("width") / 4
#     ystart = size.get("height") / 2
#     xend = size.get("width") / 4 * 3
#     yend = size.get("height") / 2
#     driver.swipe(xstart, ystart, xend, yend)
#     time.sleep(1)
#
#
# # 向下滑动屏幕
# def swipeToDown():
#     size = driver.get_window_size()
#     xstart = size.get("width") / 2
#     ystart = size.get("height") / 4
#     xend = size.get("width") / 2
#     yend = size.get("height") / 4 * 3
#     driver.swipe(xstart, ystart, xend, yend)
#     time.sleep(1)
#
#
# # 向上滑动屏幕
# def swipeToUp():
#     size = driver.get_window_size()
#     xstart = size.get("width") / 2
#     ystart = size.get("height") / 4 * 3
#     xend = size.get("width") / 2
#     yend = size.get("height") / 4
#     driver.swipe(xstart, ystart, xend, yend)
#     time.sleep(1)
#
#
# # 判断activity是否变化
# def isactivityswich(lastactivity):
#     isactivityswich = True
#     if driver.current_activity == lastactivity:
#         isactivityswich = False
#     return isactivityswich
#
#
# # 判断元素是否变化
# def iselementswich(lastelement):
#     iselementswich = True
#     if getelement().__eq__(lastelement):
#         iselementswich = False
#     return iselementswich
#
#
# # 获取页面中所有可点击的元素，返回List
# def getelement():
#
#     #    这里的list直接去重、过滤，按照activity-text-class不行，取得前5个吧 ， todo
#     return driver.find_elements_by_xpath("//*[contains(@clickable,'true')]")
#
#
#
# # 判断当前是否是H5
# def isnotH5page():
#     noth5page = True
#     n = 0
#     for x in H5list:
#         if driver.find_elements_by_class_name(x).__len__() != 0:
#             n = n + 1
#     if n != 0:
#         noth5page = False
#     return noth5page
#
# # 判断当前是否是H5
# def isnotH5page2():
#     noth5page = True
#     for x  in driver.contexts:
#         if str(x).upper().__contains__('WEB'):
#             noth5page=False
#             break
#     return noth5page
#
#
#
# # 元素入库
# def elemenCollection():
#     return True
#
#
# # 元素入库
# def pageCollection():
#     return True
#
#
# # 判断是否仍在被测应用中,需传入当前包名
# def isTheTestedApp(theapp):
#     isappswich = False
#     if driver.current_package.__eq__(theapp):
#         isappswich = True
#     return isappswich
#
#
# # 处理应用闪屏页 todo 如果不是首次启动?
# def splashcreen():
#     while driver.find_elements_by_xpath("//*[contains(@clickable,'true')]").__len__() == 0:
#         for x in range(0, 4):
#             swipeToLeft()
#     while driver.find_elements_by_xpath("//*[contains(@clickable,'true')]").__len__() == 0:
#         for x in range(0, 4):
#             swipeToUp()
#     while driver.find_elements_by_xpath("//*[contains(@clickable,'true')]").__len__() == 0:
#         for x in range(0, 4):
#             swipeToDown()
#     for x in driver.find_elements_by_xpath("//*[contains(@clickable,'true')]"):
#         x.click()
#
#
# # 截屏
# def screenshot():
#     path = PATH(os.getcwd() + "/screenshot")
#     timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
#     # os.popen("adb wait-for-device")
#     os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
#     if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
#         os.makedirs(path)
#     time.sleep(1.5)
#     os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png"))
#     # os.popen("adb shell rm /data/local/tmp/tmp.png")
#     print("success")
#
#
# # 递归、核心逻辑
# def refresh():
#     notover = True
#     while notover:
#         current_activity = driver.current_activity  # 当前activity
#         current_getelement = getelement()  # 当前页面可点元素
#
#         if (isnotH5page2()):  # 如果当前页面不是H5页面
#             for x in current_getelement:
#                 # x.tag_name
#                 # HybridAndroidDriver.Device.click(1,2)
#                 x.click()
#                 time.sleep(0.5)
#                 screenshot()  # 点击后截屏
#                 if not isnotH5page():
#                     driver.back()
#                     break
#                     # 如果当前页面不是H5页面
#
#                 if isactivityswich(current_activity):
#                     pass
#                     # activity元素变了
#
#                 if iselementswich(current_getelement):
#                     pass
#                     # 页面元素变了
#
#                     if (not isTheTestedApp(theTestedApp, )):
#                         # 不在被测应用了,启动上一个activity,todo
#                         driver.start_activity(theTestedApp, current_activity)
#                 current_getelement = getelement()  # 当前页面元素
#                 current_activity = driver.current_activity  # 当前activity
#         else:
#             driver.back()
#
#             # todo 使用递归
#
#
# if __name__ == "__main__":
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     desired_caps['deviceName'] = 'Android Emulator'
#     desired_caps['app'] = '/Users/mileszhou/Downloads/aaaa/xdj-3.1.0-test.apk'
#     # webdriver.Remote.get('http://localhost:4723/wd/hub')
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
#     # driver =webdriver.webdriver('http://localhost:4723/wd/hub', desired_caps)
#     theTestedApp = driver.current_package  # 被测app的包名
#
#     times =time.time() #开始测试时的时间戳 作为本次测试的唯一标识
#     #
#     # while notover :
#     #     if isnewtest(times):
#     #         sql
#     #     elif  testover(times):
#     #         break
#     #     elif:
#     #         pass
#     #
#     #     getelement()
#     #     if  newpage():
#     #         sql
#     #         click()
#     #     elif pageover():
#     #         click()
#     #     else:
#     #         startavtivity
#     #         toanotoverpage
#     #         click
#     #
#
#
#     # times  #开始测试时的时间戳 作为本次测试的唯一标识
#     # while 循环， 变量 notover = True
#
#         # check(times) # 通过id查询数据库。1.是否有？  无则新建。  2.有，是否测试完成，完成则直接结束， 未完成则继续测试
#
#          # getelement（） # 新页面 则插数据库，
#     splashcreen()  # 处理闪屏页
#
#     refresh()
#
#     # driver.quit()
