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


@allure.epic('花椒自动化测试 - 我看过的')
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-我看过的 test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/',name='点击可进入用例链接')
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Mine   # 增加用例标识，执行指定用例用
    def test_looked(self, init_driver):
        with allure.step('step 1、点击我的tab,我的-主播，进入主播页面'):
            driver = init_driver
            # 点击 我的  ,   找到'com.huajiao:id/pa'
            click_methods_id(driver,is_element_exist_test(driver, josn_test['Modle_mine']['Mine']['Mine_ids'])[0])
            # 点击 我的-用户
            # driver.find_element(By.ID, 'com.huajiao:id/ejy').click()
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine_user']['Mine_ids'])[0])
            time.sleep(5)
        with allure.step('step 2、点击 我看过的'):
            # 我的-> 用户 -> 商城icon -> 找到 我看过的 文本
            print("开始执行")
            # driver.find_element(By.XPATH, "//*[@resource-id='com.huajiao:id/ui'][@text='我看过的']").click()  # 通过xpath得到可识别的text
            print("点击我看过的")
            click_methods_id_text(driver,list_str(josn_test['Modle_mine']['Mine_looked']['looked_id_text']), '我看过的')
            print("look的look4", driver)
        with allure.step('step 3、已经点击 我看过的 ，判断点击后的页面是否正确'):
            # 我的-> 用户 -> 我看过的 icon -> 找到 我看过的、直播、动态 文本
            exist_methods_subidtext(driver,list_str(josn_test['Modle_mine']['Mine_looked']['Mine_sub_id_text_looked']),'我看过的')
            exist_methods_subidtext(driver,list_str(josn_test['Modle_mine']['Mine_looked']['Mine_sub_id_text_live']),'直播')
            exist_methods_subidtext(driver,list_str(josn_test['Modle_mine']['Mine_looked']['Mine_sub_id_text_dynamic']),'动态')
            print("look的look4", driver)
            driver.quit()

