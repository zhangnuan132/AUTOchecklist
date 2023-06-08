'''
    消息
    任务
    我看过的
    我的动态
    外显装备
    我的形象
    流量中心：
    商城
    我的家族（家族页，直播间道具不可点击， 非直播间道具可点击使用）
    以上点击能进入正确页面
'''
import time
import allure
import pytest

import time
import allure
import pytest
from testcases.location import list_str, click_methods_id_text, exist_methods_subtext, click_methods_id, \
    is_element_exist_test, josn_test, exist_methods_subidtext


@allure.epic('花椒自动化测试 - 我的家族')
# 查找消息按钮
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-我的家族test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/',name='点击可进入用例链接')
    @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Mine   # 增加用例标识，执行指定用例用
    def test_family(self, init_driver):
        with allure.step('step 1、点击我的tab,我的-主播，进入主播页面'):
            driver = init_driver
            time.sleep(5)
            # 点击 我的   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine']['Mine_ids'])[0])
            # 点击 我的-用户   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver,
                             is_element_exist_test(driver, josn_test['Modle_mine']['Mine_anchor']['Mine_ids'])[0])
            time.sleep(5)
        with allure.step('step 2、点击我的家族，进入页面'):
        #  方法2：适用于用于 不同模块相同id   根据id text 同时查询
            click_methods_id_text(driver, list_str(josn_test['Modle_mine']['Mine_family']['family_id_text']), '我的家族')
        with allure.step('step 3、已经点击我的家族，判断点击后的页面是否正确'):
            # 判断点击后展示的内容是否正确, 原来基础上增加json_all将list转为str
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_family']['Mine_sub_id_text_family']),'我的家族')
            driver.quit()
            # # 通过text判断是否存在文本
            # # 通过id判断是否存在文本
            # time.sleep(5)  # 获取页面元素时，一定要停留几秒
            # page_source_family = driver.page_source  # 获取私信列表页面资源   把这个写在判断的方法里
            # print("page_source_family..", page_source_family)
            # text_found_family = []
            # text_expected_family = []
            # time.sleep(2)
            # #我的家族
            # flow_loc = list_str(josn_test['Modle_mine']['Mine_family']['Mine_subid_family'])
            # text_found_family.append(driver.find_element(By.ID, flow_loc).get_attribute('text'))
            # text_expected_family.append('我的家族')
            # element_text_compared(text_found_family, text_expected_family)  # 判断所有资源都在此页面