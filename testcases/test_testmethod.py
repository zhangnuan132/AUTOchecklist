'''
    消息
    任务
    商城
    我的动态
    外显装备
    我的形象
    流量中心：
    商城
    商城（家族页，直播间道具不可点击， 非直播间道具可点击使用）
    商城：我的-用户-商城
    以上点击能进入正确页面
'''
import time
import allure
import pytest


@allure.epic('花椒自动化测试 - 我看过的')
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-我看过的 test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/',name='点击可进入用例链接')
    @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Success   # 增加用例标识，执行指定用例用
    def test_success(self):
        with allure.step('step 1、点击我的tab,我的-主播，进入主播页面'):
            print("date and time: 啥都没加")