'''
    消息
    任务
    我看过的
    我的动态
    外显装备
    我的形象
    商城
    我的背包（背包页，直播间道具不可点击， 非直播间道具可点击使用）
    以上点击能进入正确页面
'''
import time
import allure
import pytest
from testcases.location import list_str, click_methods_id_text, exist_methods_subtext, click_methods_id, \
    is_element_exist_test, josn_test, exist_methods_subidtext

@allure.epic('花椒自动化测试 -装备')
# 查找消息按钮
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-我的装备test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/',name='点击可进入用例链接')
    @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Mine   # 增加用例标识，执行指定用例用
    def test_equipment(self, init_driver):
        with allure.step('step 1、点击我的tab,我的-主播，进入主播页面'):
            driver = init_driver
            # 点击 我的  ,   找到'com.huajiao:id/pa'
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine']['Mine_ids'])[0])
            # 点击 我的-用户
            # driver.find_element(By.ID, 'com.huajiao:id/ejy').click()
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine_user']['Mine_ids'])[0])
            time.sleep(5)
        with allure.step('step 2、点击外显装备，进入页面'):
            click_methods_id_text(driver, list_str(josn_test['Modle_mine']['Mine_equipment']['equipment_id_text']),'外显装备')
        with allure.step('step 3、已经点击我的装备，判断点击后的页面是否正确'):
            # 判断点击后展示的内容是否正确, 原来基础上增加json_all将list转为str
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_equipment']['Mine_sub_id_text_equipment']),'我的装备')
            driver.quit()
