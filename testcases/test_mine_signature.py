'''
    消息
    任务
    我看过的
    我的动态
    外显装备
    我的形象
    流量中心：
    商城
    语音签名（协议页，直播间道具不可点击， 非直播间道具可点击使用）
    以上点击能进入正确页面
'''
import time
import allure
import pytest
from testcases.location import list_str, click_methods_id_text, exist_methods_subtext, click_methods_id, \
    is_element_exist_test, josn_test, exist_methods_subidtext


@allure.epic('花椒自动化测试 - 语音签名')
# 查找消息按钮
class TestAddSub():
    @allure.story('[story] 我的模块')
    @allure.title('[Title][case01] 验证我的-语音签名test')
    @allure.description('登录测试用例 执行人：xx')
    @allure.link(url='https://www.baidu.com/',name='点击可进入用例链接')
    @pytest.mark.flaky(reruns=2, reruns_delay=2)  # 只有失败的用例才重跑
    @pytest.mark.Mine   # 增加用例标识，执行指定用例用
    def test_signature(self, init_driver):
        with allure.step('step 1、点击我的tab,我的-主播，进入主播页面'):
            driver = init_driver
            time.sleep(5)
            # 点击 我的   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver, is_element_exist_test(driver, josn_test['Modle_mine']['Mine']['Mine_ids'])[0])
            # 点击 我的-用户   点击通用方法 ,通过is_element_exist_test找到可点击的id, 再通过click_methods_id_test点击
            click_methods_id(driver,
                             is_element_exist_test(driver, josn_test['Modle_mine']['Mine_anchor']['Mine_ids'])[0])
            time.sleep(5)
        with allure.step('step 2、点击语音签名，进入页面'):
            click_methods_id_text(driver, list_str(josn_test['Modle_mine']['Mine_signature']['signature_id_text']), '语音签名')

            #  方法2：适用于用于 不同模块相同id   根据id text 同时查询
            # signature_id_text = list_str(josn_test['Modle_mine']['Mine_signature']['signature_id_text'])  # 我的-语音签名
            # print("signature_id_text::::是str ", signature_id_text)
            # signature_id_text1 = driver.find_element(By.XPATH, signature_id_text).get_attribute('text') # 通过xpath得到可识别的text
            # print("flow_id_text1::::是str", type(signature_id_text1), signature_id_text1 )
            # if is_element_exist(str_list(signature_id_text1), page_source_flow):
            #     print("str_list(dynamic_id_text1)...是list", type(signature_id_text1), signature_id_text1)
            #     driver.find_element(By.XPATH, signature_id_text).click()  # 点击语音签名按钮
            #     assert "点击语音签名正常"
            # else:
            #     assert "点击语音签名失败"
        with allure.step('step 3、已经点击语音签名，判断点击后的页面是否正确'):
            exist_methods_subtext(driver, list_str(josn_test['Modle_mine']['Mine_signature']['Mine_subid_signature']),'录制语音签名')
            driver.quit()
            #
            # # 判断点击后展示的内容是否正确, 原来基础上增加json_all将list转为str
            # # 通过text判断是否存在文本
            # # 通过id判断是否存在文本
            # time.sleep(5)  # 获取页面元素时，一定要停留几秒
            # page_source_signature = driver.page_source  # 获取协议列表页面资源   把这个写在判断的方法里
            # print("page_source_signature..", page_source_signature)
            # text_found_signature = []
            # text_expected_signature = []
            # time.sleep(2)
            # #语音签名
            # flow_loc = list_str(josn_test['Modle_mine']['Mine_signature']['Mine_subid_signature'])
            # text_found_signature.append(driver.find_element(By.ID, flow_loc).get_attribute('text'))
            # text_expected_signature.append('录制语音签名')
            # element_text_compared(text_found_signature, text_expected_signature)  # 判断所有资源都在此页面