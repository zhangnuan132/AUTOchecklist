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


@allure.epic('花椒自动化测试-封面测评')
# 查找消息按钮
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-封面测评test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/',name='点击可进入用例链接')
    @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Mine   # 增加用例标识，执行指定用例用
    def test_cover(self, init_driver):
        with allure.step('step 1、点击我的tab,我的，进入任务页面'):
            driver = init_driver
            time.sleep(5)
            # 点击 我的   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine']['Mine_ids'])[0])
            # 点击 我的-用户   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver,is_element_exist_test(driver, josn_test['Modle_mine']['Mine_anchor']['Mine_ids'])[0])
            time.sleep(5)
        with allure.step('step 2、点击我的任务tab，进入页面'):
            click_methods_id_text(driver, list_str(josn_test['Modle_mine']['Mine_task']['task_id_text']),'消息')
        with allure.step('step 3、已经点击任务，判断点击后的页面是否正确'):
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_task']['Mine_subtext_daily']),'日常')
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_task']['Mine_subtext_anchor']),'主播')
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_task']['Mine_subtext_activity']),'活动')
            driver.quit()