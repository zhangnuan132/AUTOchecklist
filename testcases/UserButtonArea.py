# '''
#     消息
#     任务
#     我看过的
#     我的动态
#     外显装备
#     我的形象
#     商城
#     我的背包（背包页，直播间道具不可点击， 非直播间道具可点击使用）
#     以上点击能进入正确页面
# '''
# import time
#
# from selenium.webdriver.common.by import By
#
# import conftest
# import assertResult
#
#
# # 进入我的-用户页面
# def mine_user():
#     driver = conftest.initialization_parameters('Android', 'SM_N950N')
#     # wait = WebDriverWait(driver, 10)  # 等到10s，开屏结束，进入热门频道
#     driver.implicitly_wait(10)  # 等待10s 全局等待
#     # driver.find_element(By.ID,'com.huajiao:id/pe').click()
#     # driver.find_element(By.ID,'com.huajiao:id/enm').click()
#     driver.find_element(By.ID, 'com.huajiao:id/of').click()
#     driver.find_element(By.ID, 'com.huajiao:id/dsy').click()
#
#     return driver
#
#
# #
# # 用户：com.huajiao:id/e7q
# # 主播: com.huajiao:id/dsy
# # 我的：com.huajiao:id/of
#
#
# # 查找消息按钮
# def test_message():
#     driver = mine_user()
#     driver.implicitly_wait(5)
#     driver.find_element(By.ID, 'com.huajiao:id/c4k').click()
#     # message_id_text = "//*[@resource-id='com.huajiao:id/um'][@text='消息']"  # 通过id和text联合查询
#     # driver.find_element(By.XPATH, message_id_text).click()  # 点击消息按钮
#     time.sleep(5)
#     # message_element = {'com.huajiao:id/e37': '私信标题', 'com.huajiao:id/e3e': '联系人icon', 'com.huajiao:id/b3r': '花椒客服'}
#     message_element = {'com.huajiao:id/dqb': '私信', 'com.huajiao:id/e72': '花椒客服'}
#     page_source_message = driver.page_source  # 获取私信列表页面资源
#     assert "我的消息点击完成"
#     # assertResult.is_element_exist(message_element, str(page_source_message))
#     # print('page_source = ',driver.page_source)
#     # assert (driver.find_element(By.ID,'com.huajiao:id/e37').text in '私信','测试未通过，没有找到私信tittle')
#
#
# # 查找任务按钮
# def test_task():
#     driver = mine_user()
#     driver.implicitly_wait(5)
#     task_id_text = "//*[@resource-id='com.huajiao:id/um'][@text='任务']"
#     # print(task_id_text)
#     # driver.find_element(By.XPATH, task_xpath).click()
#     driver.find_element(By.XPATH, task_id_text).click()  # 点击任务按钮
#     time.sleep(5)
#     text_found = []
#     text_expected = []
#     richang_tab_loc = "//android.widget.TabWidget/android.view.View[1]/android.view.View[1]"  # 任务页面日常tab的相对位置
#     text_found.append(driver.find_element(By.XPATH, richang_tab_loc).get_attribute('text'))
#     # print(driver.find_element(By.XPATH,richang_tab_loc))
#     text_expected.append('日常')
#     zhubo_tab_loc = "//android.widget.TabWidget/android.view.View[2]/android.view.View[1]"
#     time.sleep(2)
#     text_found.append(driver.find_element(By.XPATH, zhubo_tab_loc).get_attribute('text'))
#     text_expected.append('主播')
#     assertResult.element_text_compared(text_found, text_expected)
#
#
# # 查找我看过的按钮
# def test_mylooked():
#     driver = mine_user()
#     driver.implicitly_wait(5)
#     mylooked_id_text = "//*[@resource-id='com.huajiao:id/um'][@text='我看过的']"
#     driver.find_element(By.XPATH, mylooked_id_text).click()  # 点击我看过的按钮
#     text_found = []
#     text_expected = []
#     zhibo_loc = "//*[@resource-id='com.huajiao:id/drw']/android.widget.LinearLayout" \
#                 "/android.widget.RelativeLayout[1]/android.widget.TextView"
#     time.sleep(5)
#     text_found.append(driver.find_element(By.XPATH, zhibo_loc).get_attribute('text'))
#     text_expected.append('直播')
#     dongtai_loc = "//*[@resource-id='com.huajiao:id/drw']/android.widget.LinearLayout" \
#                   "/android.widget.RelativeLayout[2]/android.widget.TextView"
#     time.sleep(2)
#
#     text_found.append(driver.find_element(By.XPATH, dongtai_loc).get_attribute('text'))
#     text_expected.append('动态')
#     text_found.append(driver.find_element(By.ID, 'com.huajiao:id/e3d').get_attribute('text'))
#     text_expected.append('清空')
#     assertResult.element_text_compared(text_found, text_expected)
#
#     # #我看过的-动态
#     # driver.find_element(By.XPATH,dongtai_loc).click()
#     # dynamic_liked = "//*[@resource-id='com.huajiao:id/afl']/android.widget.TextView"
#
#
# # 查找我的动态按钮
# def test_mydynamic():
#     driver = mine_user()
#     driver.implicitly_wait(5)
#     mydynamic_id_text = "//*[@resource-id='com.huajiao:id/um'][@text='我的动态']"
#     driver.find_element(By.XPATH, mydynamic_id_text).click()  # 点击我的动态按钮
#     time.sleep(5)
#     page_source_dynamaic = driver.page_source
#     # print(page_source_dynamaic)
#     dynamaic_element = {'com.huajiao:id/e45': '编辑按钮', 'com.huajiao:id/e49': '分享按钮', 'com.huajiao:id/b61': '花椒号'}
#     assertResult.is_element_exist(dynamaic_element, str(page_source_dynamaic))
#     text_found = []
#     text_expected = []
#     time.sleep(2)
#     zuopin_loc = "//*[@resource-id='com.huajiao:id/b71']/android.widget.LinearLayout/android.widget.TextView[1]"
#     text_found.append(driver.find_element(By.XPATH, zuopin_loc).get_attribute('text'))
#     text_expected.append('作品')
#     dongtai_loc = "//*[@resource-id='com.huajiao:id/b71']/android.widget.LinearLayout/android.widget.TextView[2]"
#     text_found.append(driver.find_element(By.XPATH, dongtai_loc).get_attribute('text'))
#     text_expected.append('动态')
#     ziliao_loc = "//*[@resource-id='com.huajiao:id/b71']/android.widget.LinearLayout/android.widget.TextView[3]"
#     text_found.append(driver.find_element(By.XPATH, ziliao_loc).get_attribute('text'))
#     text_expected.append('资料')
#     assertResult.element_text_compared(text_found, text_expected)
#
#
# # 查找外显装备按钮
# def test_equipment():
#     driver = mine_user()
#     driver.implicitly_wait(5)
#     mydynamic_id_text = "//*[@resource-id='com.huajiao:id/um'][@text='外显装备']"
#     driver.find_element(By.XPATH, mydynamic_id_text).click()  # 点击外显装备按钮
#     time.sleep(5)
#     # page_source_equipment = driver.page_source
#     # print(page_source_equipment)
#     zhibochangjing_loc = "//#[@resource-id='app']/android.view.View/android.view.View[1]/android.view.View[1]"
#
#     jiaoyouchangjing_loc = "//#[@resource-id='app']/android.view.View/android.view.View[1]/android.view.View[2]"
#     driver.find_element(By.XPATH, jiaoyouchangjing_loc).click()
