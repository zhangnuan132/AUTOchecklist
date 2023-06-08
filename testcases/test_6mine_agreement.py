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
from selenium.webdriver.common.by import By

from testcases.location import list_str, click_methods_id_text, exist_methods_subtext, click_methods_id, \
    is_element_exist_test, josn_test, exist_methods_subidtext


@allure.epic('花椒自动化测试 - 我的协议')
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-我的协议 test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/', name='点击可进入用例链接')
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Live  # 增加用例标识，执行指定用例用
    def test_agreement(self, init_driver):
        with allure.step('step 1、点击我的tab,我的-主播，进入主播页面'):
            driver = init_driver
            time.sleep(3)
            # driver.find_element(By.ID, 'com.huajiao:id/childmode_dialog_ok').click()  # 点击青少年弹窗
            time.sleep(3)
            # 点击 我的   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine']['Mine_ids'])[0])
            # 点击 我的-用户   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver,is_element_exist_test(driver, josn_test['Modle_mine']['Mine_anchor']['Mine_ids'])[0])
            time.sleep(5)
        with allure.step('step 2、点击 我的协议'):
            # 我的-> 用户 -> 我的协议icon -> 找到 主播相关 文本
            # 1、 通过click_methods_id_text方法判断，id_text对应的''中的文本是正确的   2、点击id_text
            click_methods_id_text(driver,list_str(josn_test['Modle_mine']['Mine_agreement']['agreement_id_text']), '我的协议')
            print("agreement的协议4", driver)
        with allure.step('step 3、已经点击 我的协议 ，判断点击后的页面是否正确'):
            # 我的-> 用户 -> 我的协议icon -> 找到 主播相关 文本，去掉了 list_str
            # 1、 通过exist_methods_subtext方法判断，id_text对应的''中的文本是正确的，不用点击
            exist_methods_subidtext(driver, list_str(josn_test['Modle_mine']['Mine_agreement']['Mine_sub_id_text_agreement']),'主播相关')
            driver.quit()
