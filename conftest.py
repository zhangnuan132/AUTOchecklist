import os

from appium.common.logger import logger

import allure
import pytest
from appium import webdriver
# from appium.common.logger import logger
# from selenium.webdriver.common.service import logger
import time

driver = None  # 定义一个全局driver对象


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item: 测试用例
    :param call: 测试步骤
    :return:
    """
    # 获取钩子方法的调用结果
    print("调用勾子函数了吗")
    out_come = yield
    rep = out_come.get_result()  # 从钩子方法的调用结果中获取测试报告
    # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write((rep.nodeid + extra + "\n"))
        # 添加allure报告截图
        # 实现失败截图并添加到allure附件。截图方法需要使用driver对象，想办法把driver传过来
        print("勾子函数里的 driver :", driver)
        if hasattr(driver, "get_screenshot_as_png"):  # global定义的
            with allure.step('用例执行失败时，添加失败截图...'):
                logger.error("用例执行失败，捕获当前页面......")
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
                # 加了这两句，添加日志
                # log = logger.error("报错信息:%s", "无法找到或点击元素", exc_info=1)  # 记录报错日志
                # # 获取报错日志，并将日志展示在Allure报告上
                # allure.attach.file(driver.get_log(log), "失败日志", allure.attachment_type.TEXT)


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def attachAndroidList():
    dict1 = {}
    dict2 = {
        # 'platformVersion': '9',  # 手机安卓版本
        # 'deviceName': 'z5fqhqaitwuolbs8',  # android设备名，安卓手机可以随意填写
        'appPackage': 'com.huajiao',  # 启动APP Package名称
        'platformName': 'Android',  # 被测手机是安卓
        'appActivity': '.cover.CoverActivity',  # 启动Activity名称     com.huajiao.main.MainActivity
        'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App
        # 'newCommandTimeout': 6000,
        # 'automationName': 'UiAutomator2'
        # 'app': r'd:\apk\bili.apk',
    }

    serial_output = os.popen("adb devices", "r").read().split()[
                    4:]  # 用空格作为分隔符，从输出的列表中第5个开始为设备序列号，将后面所有内容全部输出,['List', 'of', 'devices', 'attached', '序列号',
    # 'device']
    # print(serial_output, len(serial_output))
    for i in range(len(serial_output)):
        if i % 2 == 0:
            # print("i是", i)
            dict1['deviceName'] = serial_output[i]
            version_output = os.popen("adb -s " + serial_output[i] + " shell  getprop ro.build.version.release",
                                      "r").read()
            dict1['platformVersion'] = str(version_output).strip("\n")
            des = Merge(dict1, dict2)
            # print(dict3) # 想下如何兼容多个设备，return
            return des
        else:
            pass


@pytest.fixture()
def init_driver():
    # 前置
    global driver  # global变量，相当于给上面driver = None赋值了
    print("attachAndroidList()::", attachAndroidList())
    driver = webdriver.Remote('http://localhost:4723/wd/hub', attachAndroidList())
    print("start_app :::", driver)
    return driver

#
# 关闭app
@pytest.fixture()
def close_driver():
    yield driver
    time.sleep(2)
    driver.quit()



