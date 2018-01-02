# coding=utf-8


import time
import os
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from appium import webdriver

PATH = lambda p: os.path.abspath(p)

# 过滤H5控件 by class name
H5list = ["android.webkit.WebView"]

#不测试的控件，例如系统控件
ignoreEl =["android.widget.NumberPicker"]

class ClientDriver(webdriver.Remote):
    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
                 desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False):

        super(ClientDriver, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive)

        if self.command_executor is not None:
            self._addCommands()
        # self.error_handler = MobileErrorHandler()
        # self._switch_to = MobileSwitchTo(self)

        # add new method to the `find_by_*` pantheon
        By.IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
        By.IOS_PREDICATE = MobileBy.IOS_PREDICATE
        By.IOS_CLASS_CHAIN = MobileBy.IOS_CLASS_CHAIN
        By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
        By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID

    # 信贷家测试个性化操作

    # 向左滑动屏幕
    def swipeToLeft(self):
        size = self.get_window_size()
        xstart = size.get("width") / 4 * 3
        ystart = size.get("height") / 2
        xend = size.get("width") / 4
        yend = size.get("height") / 2
        self.swipe(xstart, ystart, xend, yend)
        time.sleep(1)

    # 向右滑动屏幕
    def swipeToRight(self):
        size = self.get_window_size()
        xstart = size.get("width") / 4
        ystart = size.get("height") / 2
        xend = size.get("width") / 4 * 3
        yend = size.get("height") / 2
        self.swipe(xstart, ystart, xend, yend)
        time.sleep(1)

    # 向下滑动屏幕
    def swipeToDown(self):
        size = self.get_window_size()
        xstart = size.get("width") / 2
        ystart = size.get("height") / 4
        xend = size.get("width") / 2
        yend = size.get("height") / 4 * 3
        self.swipe(xstart, ystart, xend, yend)
        time.sleep(1)

    # 向上滑动屏幕
    def swipeToUp(self):
        size = self.get_window_size()
        xstart = size.get("width") / 2
        ystart = size.get("height") / 4 * 3
        xend = size.get("width") / 2
        yend = size.get("height") / 4
        self.swipe(xstart, ystart, xend, yend)
        time.sleep(1)

    # 处理应用闪屏页 todo 如果不是首次启动?
    def splashcreen(self):
        while self.find_elements_by_xpath("//*[contains(@clickable,'true')]").__len__() == 0:
            for x in range(0, 4):
                self.swipeToLeft()
        while self.find_elements_by_xpath("//*[contains(@clickable,'true')]").__len__() == 0:
            for x in range(0, 4):
                self.swipeToUp()
        while self.find_elements_by_xpath("//*[contains(@clickable,'true')]").__len__() == 0:
            for x in range(0, 4):
                self.swipeToDown()
        for x in self.find_elements_by_xpath("//*[contains(@clickable,'true')]"):
            x.click()

    # 截屏
    def screenshot(self):
        path = PATH(os.getcwd() + "/screenshot")
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        # os.popen("adb wait-for-device")
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
            os.makedirs(path)
        time.sleep(1.5)
        os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png"))
        # os.popen("adb shell rm /data/local/tmp/tmp.png")
        print("success")

    # 获取页面中所有可点击的元素，返回List
    def getelement(self):

        #这里的list直接去重、过滤，按照activity-text-class不行，取得前5个吧 ， todo
        return self.find_elements_by_xpath("//*[contains(@clickable,'true')]")

    # 判断当前是否是H5,通过上传过滤H5控件List
    def isH5page(self):
        ish5page = True
        n = 0
        for x in H5list:
            if self.find_elements_by_class_name(x).__len__() != 0:
                n = n + 1
        if n == 0:
            ish5page = False
        return ish5page

    # 判断当前是否是H5
    def isnotH5page2(self):
        noth5page = True
        for x in self.contexts:
            if str(x).upper().__contains__('WEB'):
                noth5page = False
                break
        return noth5page

    # 判断是否仍在被测应用中,需传入当前包名
    def isTheTestedApp(self,theapp):
        isappswich = False
        if self.current_package.__eq__(theapp):
            isappswich = True
        return isappswich

