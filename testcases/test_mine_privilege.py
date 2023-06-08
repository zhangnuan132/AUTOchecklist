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

from testcases.location import list_str, str_list, element_text_compared, click_methods_id_text, exist_methods_subtext, \
    click_methods_id, exist_methods_subid, is_element_exist_text, click_methods_id, is_element_exist_test, josn_test, \
    exist_methods_subidtext


@allure.epic('花椒自动化测试 - 我的特权')
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-我的特权 test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/',name='点击可进入用例链接')
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Mine # 增加用例标识，执行指定用例用
    def test_privilege(self, init_driver):
        with allure.step('step 1、点击我的tab,我的-主播，进入主播页面'):
            driver = init_driver
            # 点击 我的  ,   找到'com.huajiao:id/pa'
            click_methods_id(driver,is_element_exist_test(driver, josn_test['Modle_mine']['Mine']['Mine_ids'])[0])
            # 点击 我的-用户
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine_user']['Mine_ids'])[0])
            time.sleep(5)
        with allure.step('step 2、点击 用户等级'):
            click_methods_id_text(driver,list_str(josn_test['Modle_mine']['Mine_privilege']['userlevel_id_text']), '用户等级')
            time.sleep(5)
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_privilege']['Mine_sub_id_text_userlevel']),'用户等级')
            driver.press_keycode('4')
        with allure.step('step 3、点击 会员等级'):
            click_methods_id_text(driver,list_str(josn_test['Modle_mine']['Mine_privilege']['memberlevel_id_text']), '会员等级')
            time.sleep(15)
            exist_methods_subtext(driver, list_str(josn_test['Modle_mine']['Mine_privilege']['Mine_memberlevel_subtext']),'会员特权')
            driver.press_keycode('4')
        with allure.step('step 4、点击 骑士团'):
            click_methods_id_text(driver,list_str(josn_test['Modle_mine']['Mine_privilege']['knights_id_text']), '骑士团')
            time.sleep(5)
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_privilege']['Mine_sub_id_text_knights']),'骑士团')
            driver.press_keycode('4')
        with allure.step('step 5、点击 真爱团'):
            click_methods_id_text(driver,list_str(josn_test['Modle_mine']['Mine_privilege']['loveclub_id_text']), '真爱团')
            time.sleep(5)
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_privilege']['Mine_sub_id_text_loveclub']),'加入的团')
            driver.quit()

