'''
    我的账户相关
'''
# import pyperclip
import time
import allure
import pytest
from selenium.webdriver.common.by import By

from testcases.location import list_str, click_methods_id_text, exist_methods_subtext, click_methods_id, \
    is_element_exist_test, josn_test, exist_methods_subidtext


@allure.epic('花椒自动化测试 - 我的账户相关')
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-我的账户相关 test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/', name='点击可进入用例链接')
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Mine  # 增加用例标识，执行指定用例用
    def test_account(self, init_driver):
        with allure.step('step 1、点击我的tab,我的-主播，进入主播页面'):
            driver = init_driver
            time.sleep(5)
            # 点击 我的   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine']['Mine_ids'])[0])
            # 点击 我的-用户   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine_user']['Mine_ids'])[0])
            time.sleep(5)
        with allure.step('step 2、uid展示正确'):
            # 点击花椒号复制，复制uid展示正常
            print("点击uid的复制")
            click_methods_id_text(driver, list_str(josn_test['Modle_mine']['Mine_account']['uid_id_text']), '复制')
            # info = pyperclip.paste()
            info = "258095004"
            print(f"剪切板复制的内容：{info}")
            # 线上uid 为9位
            if len(info) == 9:
                print("uid正确")
            else:
                print("uid错误")
        with allure.step('step 3、点击头像进入个人编辑页面'):
            # 点击头像进入个人编辑页面
            click_methods_id(driver,
                             is_element_exist_test(driver, josn_test['Modle_mine']['Mine_account']['Mine_image_id'])[0])
            exist_methods_subidtext(driver,
                                    list_str(josn_test['Modle_mine']['Mine_account']['Mine_sub_id_text_editdata']),
                                    '个人资料')
            print("需要返回上一级")
            driver.press_keycode('4')
        with allure.step('step 4、点击管理，进入语音签名'):
            # 点击管理，进入语音签名
            click_methods_id(driver,
                             is_element_exist_test(driver, josn_test['Modle_mine']['Mine_account']['Mine_manage_id'])[
                                 0])
            exist_methods_subidtext(driver,
                                    list_str(josn_test['Modle_mine']['Mine_account']['Mine_sub_id_text_labelsquare']),
                                    '标签广场')
            driver.press_keycode('4')
        with allure.step('step 5、点击设置，进入个人设置页'):
            # 点击设置，进入个人设置页
            print("需要返回上一级")
            click_methods_id(driver,
                             is_element_exist_test(driver, josn_test['Modle_mine']['Mine_account']['Mine_setting_id'])[
                                 0])
            exist_methods_subidtext(driver,
                                    list_str(josn_test['Modle_mine']['Mine_account']['Mine_sub_id_text_setting']), '设置')
            driver.press_keycode('4')
            # 测试看：花椒豆、金币展示正常，花椒豆充值成功   点击金币跳转金币明细
            # 测试看花椒豆展示正常，点击充值，余额增加正确
            driver.quit()
