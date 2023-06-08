"""
{
    "Modle_mine": {
        "Mine_task": {
            "Mine_ids": [
                "com.huajiao:id/qu",
            ],
            "Mine_text": [
                "我的任务"
            ]
        },
        "Mine_message": {
            "Mine_ids": [
                "com.huajiao:id/pe_message",
                "com.huajiao:id/caa_message"
            ],
            "Mine_text": [
                "我的消息"
            ]
        }
    },
    "Modle_LiveRoom": {
        "LiveRoom1": {
            "Live_ids": [
                "com.huajiao:id/pe_11",
                "com.huajiao:id/caa_11"
            ],
            "Livew_text": [
                "直播间1"
            ]
        },
        "LiveRoom2": {
            "Mine_ids": [
                "com.huajiao:id/pe_22",
                "com.huajiao:id/caa_22"
            ],
            "Mine_text": [
                "直播间2"
            ]
        }
    }
}
"""
import time
from os.path import join
from selenium.webdriver.common.by import By

# import pairs

josn_test = {
    'Modle_mine': {
        'Mine': {  # 底部我的tab,com.huajiao:id/pa 容易点到直播按钮，所以放list后面判断
            'Mine_ids': ['com.huajiao:id/bottom_tab_user', 'com.huajiao:id/p2', 'com.huajiao:id/pc',
                         'com.huajiao:id/c8r', 'com.huajiao:id/pa', 'com.huajiao:id/c9a', 'com.huajiao:id/of',
                         'com.huajiao:id/c98'],
            'Mine_text': ['我的']
        },
        'Mine_user': {  # 我的-我的用户
            'Mine_ids': ['com.huajiao:id/tv_user_pager', 'com.huajiao:id/ejy'],
            'Mine_text': ['用户']
        },
        'Mine_anchor': {  # 我的-我的主播
            'Mine_ids': ['com.huajiao:id/tv_anchor_pager', 'com.huajiao:id/dsy', 'com.huajiao:id/e3l'],
            'Mine_text': ['主播']
        },
        'Mine_account': {  # 我的-我的账户
            'Mine_uid_id': ['com.huajiao:id/huajiao_id_text'],
            'uid_id_text': ["//*[@resource-id='com.huajiao:id/tv_copy'][@text='复制']"],

            'Mine_uid_text': ['账户'],
            'Mine_image_id': ['com.huajiao:id/avatar'],
            'Mine_sub_id_text_editdata': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='个人资料']"],

            'Mine_setting_id': ['com.huajiao:id/tv_setting'],
            'Mine_sub_id_text_setting': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='设置']"],

            'Mine_manage_id': ['com.huajiao:id/tag_manager_text'],
            'Mine_sub_id_text_labelsquare': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='标签广场']"],

        },
        'Mine_privilege': {  # 我的-我的特权
            'userlevel_id_text': ["//*[@resource-id='com.huajiao:id/tv_name'][@text='用户等级']"],
            'Mine_sub_id_text_userlevel': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='用户等级']"],

            'memberlevel_id_text': ["//*[@resource-id='com.huajiao:id/tv_name'][@text='会员等级']"],
            'Mine_memberlevel_subtext': ['会员特权'],

            'knights_id_text': ["//*[@resource-id='com.huajiao:id/tv_name'][@text='骑士团']"],
            'Mine_sub_id_text_knights': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='骑士团']"],

            'loveclub_id_text': ["//*[@resource-id='com.huajiao:id/tv_name'][@text='真爱团']"],
            'Mine_sub_id_text_loveclub': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='加入的团']"],
        },
        'Mine_message': {  # 我的-我的私信
            'Mine_ids': ['com.huajiao:id/btn_icon', 'com.huajiao:id/pe_message', 'com.huajiao:id/caa_message'],
            'Mine_text': ['消息'],
            'message_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='消息']"],
            'Mine_subid_sixintitle': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subid_peopleicon': ['com.huajiao:id/top_bar_right_btn2'],
            'Mine_subid_kefuicon': ['com.huajiao:id/header_civ'],
            'Mine_sub_id_text_message': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='私信']"],
            'Mine_sub_id_text_kefu': ["//*[@resource-id='com.huajiao:id/tv_title'][@text='花椒客服']"],
            'Mine_sub_id_text_call': ["//*[@resource-id='com.huajiao:id/tv_title'][@text='打招呼']"],

        },
        'Mine_task': {  # 我的-我的任务
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['我的任务'],
            'task_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='任务']"],
            'Mine_subid_richang': [
                "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout["
                "1]/android.widget.LinearLayout/android.widget.TextView"],
            'Mine_subid_zhubo': [
                "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout["
                "2]/android.widget.LinearLayout/android.widget.TextView"],
            'Mine_subtext_daily': ['日常'],
            'Mine_subtext_anchor': ['主播'],
            'Mine_subtext_activity': ['活动'],
        },
        'Mine_dynamic': {  # 我的-我的动态
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['我的动态'],
            'dynamic_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='我的动态']"],
            'Mine_xpath': [
                "//android.widget.RelativeLayout/android.widget.FrameLayout[1]//android.widget.LinearLayout[4]/android.widget.TextView"],
            'Mine_subxpath_zuopin': [
                "//android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[1]"],
            'Mine_subxpath_dynamic': [
                "//android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[2]"],
            'Mine_subxpath_data': [
                "//android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[3]"],
            'Mine_subtext_zuopin': ['作品'],
            'Mine_subtext_dynamic': ['动态'],
            'Mine_subtext_data': ['资料']
        },
        'Mine_cover': {  # 我的-我的封面测评
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['封面测评'],
            'cover_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='封面测评']"],
            'Mine_subid_cover': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subxpath_cover': [
                "//android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[2]"],
            'Mine_subtext_cover': ['封面测评'],
            'Mine_sub_id_text_cover': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='封面测评']"],

        },
        'Mine_equipment': {  # 我的-外显装备
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['外显装备'],
            'equipment_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='外显装备']"],
            'Mine_subid_equipment': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subxpath_equipment': [
                "//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView"],
            'Mine_subtext_equipment': ['我的装备'],
            'Mine_sub_id_text_equipment': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='我的装备']"],

        },
        'Mine_image': {  # 我的-我的形象
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['我的形象'],
            'image_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='我的形象']"],
            'Mine_subtext_zhuangban': ['装扮'],
            'Mine_subtext_mine': ['我的'],
            'Mine_subtext_zhanshenchuanshuo': ['战神传说']
        },
        'Mine_flow': {  # 我的-流量中心
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['流量中心'],
            'flow_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='流量中心']"],
            'Mine_subid_flow': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subtext_flow': ['流量中心'],
            'Mine_subtext_availableflow': ['可使用流量']
        },
        'Mine_package': {  # 我的-我的背包
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['我的背包'],
            'package_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='我的背包']"],
            'Mine_subid_package': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subtext_package': ['我的背包'],
            'Mine_subtext_liwuka': ['礼物卡'],
            'Mine_subtext_daoju': ['道具'],
            'Mine_subtext_suipian': ['碎片'],
        },
        'Mine_family': {  # 我的-我的家族
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['我的家族'],
            'family_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='我的家族']"],
            'Mine_subid_family': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subtext_family': ['我的家族'],
            'Mine_sub_id_text_family': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='我的家族']"],

        },
        'Mine_agreement': {  # 我的-我的协议
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['我的协议'],
            'agreement_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='我的协议']"],
            'Mine_subid_agreement': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_sub_id_text_agreement': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='主播相关']"],
            'Mine_subtext_agreement': ['主播相关']
        },
        'Mine_signature': {  # 我的-语音签名
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['语音签名'],
            'signature_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='语音签名']"],
            'Mine_subid_signature': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subtext_signature': ['录制语音签名']
        },
        'Mine_looked': {  # 我的-用户-我看过的
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['我看过的'],
            'looked_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='我看过的']"],
            'Mine_subid_looked': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subtext_looked': ['我看过的'],
            'Mine_sub_id_text_looked': ["//*[@resource-id='com.huajiao:id/top_bar_center_top_tv'][@text='我看过的']"],
            'Mine_sub_id_text_live': ["//*[@resource-id='com.huajiao:id/eid'][@text='直播']"],
            'Mine_sub_id_text_dynamic': ["//*[@resource-id='com.huajiao:id/eid'][@text='动态']"]

        },
        'Mine_shop': {  # 我的-用户-商城
            'Mine_ids': ['com.huajiao:id/btn_icon'],
            'Mine_text': ['商城'],
            'shop_id_text': ["//*[@resource-id='com.huajiao:id/btn_text'][@text='商城']"],
            'Mine_subid_shop': ['com.huajiao:id/top_bar_center_top_tv'],
            'Mine_subtext_record': ['记录'],
            'Mine_subtext_rule': ['规则']
        }
    },
    'Modle_LiveRoom': {
        'LiveRoom1': {
            'Live_ids': ['com.huajiao:id/pe_11', 'com.huajiao:id/caa_11'],
            'Livew_text': ['直播间1']
        },
        'LiveRoom2': {
            'Mine_ids': ['com.huajiao:id/pe_22', 'com.huajiao:id/caa_22'],
            'Mine_text': ['直播间2']
        }
    }
}


def list_str(list):
    for k in range(len(list)):
        str_list = str(list[k])
        print("???????")
        print("str_list zuizhong?", str_list)
    return str_list


def str_list(s):
    list = s.split(', ')
    print("--------")
    print("list...", list)
    return list



def is_element_exist_text(driver, list, excepted_element):
    # 将多个id分别判断是否在 页面里
    # 'Mine_ids': ['com.huajiao:id/of', 'com.huajiao:id/pa', 'com.huajiao:id/c9a', 'com.huajiao:id/c98'],
    time.sleep(10)  # 获取页面元素时，一定要停留几秒
    page_source = driver.page_source  # 获取私信列表页面资源   把这个写在判断的方法里
    time.sleep(5)  # 获取页面元素时，一定要停留几秒
    print("list", list)
    print("excepted_element", excepted_element)
    global flag
    flag = 0
    if excepted_element in page_source:
        flag = 1
        return list, flag
    if flag == 0:
        return list, flag

# 不同包，不一样的id   需要判断有效的id在此页面里
def is_element_exist(element, page_source):
    global flag
    flag = 0
    for i in range(len(element)):
        print("i", i)
        print("len(element)", len(element))
        print("element[i]", element[i])
        if element[i] in page_source:
            flag = 1
            print("flag == 1", element[i], flag, i)
            return element[i], flag
        else:
            continue
    if flag == 0:
        print("flag == 0", element[i], flag)
        return element[i], flag


def element_text_compared(element, text_expected):
    """

	:param element:
	:param text_expected:
	:return:
	"""
    print("element ///", element)
    global flag
    flag = 0
    for i in range(len(element)):
        # print("i", i)
        # print("len(element)" , len(element))
        # print("element[i]" , element[i])
        if element[i] in text_expected:
            flag = 1
            # print("element_text_compared", element[i], flag,i)
            return element[i], flag
        else:
            continue
    if flag == 0:
        print("flag == 0", element[i], flag)
        return element[i], flag


#  通过id_text 得到text,判断 text在此页面
def click_methods_id_text(driver, x_id_text, text_expected):
    """
	点击时用此方法
	:param driver:
	:param x_id_text: 通过id_text联合判断元素，为了获取对应text并点击此元素
	:param text_expected: 提前获取整页面元素
	:return:
	"""
    time.sleep(10)  # 获取页面元素时，一定要停留几秒
    page_source = driver.page_source  # 获取私信列表页面资源   把这个写在判断的方法里
    print("click_methods_id_text错误？")
    x_id_text_found = driver.find_element(By.XPATH, x_id_text).get_attribute('text')  # 通过xpath得到可识别的text
    print("x_id_text_found:::", x_id_text_found)
    # assert 判断id_text 对应的text是否等于期待的值
    assert element_text_compared(str_list(x_id_text_found), text_expected)[1] == 1, "未找到点击的元素: " + text_expected
    driver.find_element(By.XPATH, x_id_text).click()  # 仍使用xpath对应点击x_id_text



def click_methods_id(driver, x_id):
    driver.find_element(By.ID, x_id).click()  # 点击对应按钮


def exist_methods_subid(driver, x_subid, text_expected):
    """
	点击后用此方法，判断某些元素是否存在
	:param driver:
	:param x_subid:  通过子页面的id判断元素，如果该id匹配的text存在，则此元素也存在
	:param text_expected:
	:return:
	"""
    # 通过子页面的id判断是否存在文本
    time.sleep(10)  # 获取页面元素时，一定要停留几秒
    page_source = driver.page_source  # 获取私信列表页面资源   把这个写在判断的方法里
    time.sleep(5)  # 获取页面元素时，一定要停留几秒
    # 不同包id不同，assert 选择当前页有效的id
    # assert is_element_exist(str_list(x_subid), page_source)[1] == 1, "此页面，没找到, " + text_expected + "对应的id"
    # x_id_found = driver.find_element(By.ID, x_subid).get_attribute('text')
    # assert element_text_compared(str_list(x_id_found), text_expected)[1] == 1, "进入对应页面后,未找到寻找的元素: " + text_expected
    if is_element_exist(str_list(x_subid), page_source)[1] == 1:
        final_x_subid = is_element_exist(str_list(x_subid), page_source)[0]
        print("final_x_subid::", final_x_subid)
        assert element_text_compared(str_list(final_x_subid), text_expected)[1] == 1, "进入对应页面后,未找到元素: " + text_expected
    # assert element_text_compared(str_list(x_id), text_expected)[1] == 1, "进入对应页面后,未找到点击的元素: " + text_expected
    # driver.find_element(By.ID, final_x_subid).click()  # 点击对应按钮
    else:
        print("进入对应页面后,未找到元素: " + x_subid)


# 通过id_text 找到此text,等于期待的值
def exist_methods_subidtext(driver, x_subidtext, text_expected):
    """

	:param driver:
	:param x_subtext: 先判断此页面是否存在，再判断是否是此元素
	:param text_expected:
	:return:
	"""
    time.sleep(5)  # 获取页面元素时，一定要停留几秒
    page_source = driver.page_source  # 获取私信列表页面资源   把这个写在判断的方法里
    print("click_methods_subtext错误？", x_subidtext)
    x_subtext_found = driver.find_element(By.XPATH, x_subidtext).get_attribute('text')  # 通过xpath得到可识别的text
    print("x_subtext_found:::", x_subtext_found)
    # assert 判断id_text 对应的text是否等于期待的值
    print("x_subtext", x_subidtext, type(x_subidtext))
    assert element_text_compared(str_list(x_subtext_found), text_expected)[1] == 1, "未找到元素: " + text_expected


def exist_methods_subtext(driver, x_subtext, text_expected):
    """

	:param driver:
	:param x_subidtext: 根据id text 联合查询是否存在
	:param text_expected:
	:return:
	"""
    # 通过id text判断是否存在文本
    time.sleep(10)  # 获取页面元素时，一定要停留几秒
    page_source = driver.page_source  # 获取私信列表页面资源   把这个写在判断的方法里
    time.sleep(5)
    # 方法：适用于用于 不同模块相同id   根据id text 同时查询
    # def is_element_exist_test(driver, list):
    assert is_element_exist_test(driver, str_list(x_subtext))[1] == 1, "进入对应页面后,未找到元素: " + text_expected


# 多个id,挑选一个有效的，返回
def is_element_exist_test(driver, list):
    global flag
    flag = 0
    # 将多个id分别判断是否在 页面里
    time.sleep(6)  # 获取页面元素时，一定要停留几秒
    page_source = driver.page_source  # 获取私信列表页面资源   把这个写在判断的方法里
    time.sleep(10)  # 获取页面元素时，一定要停留几秒
    for k in range(len(list)):
        str_x = str(list[k])
        # 判断是否在页面里
        if str_x in page_source:
            flag = 1
            time.sleep(5)
            return str_x, flag
        else:
            continue
    if flag == 0:
        print("flag == 0", list, flag)
        return list, flag


def is_element_exist(element, page_source):
    print("element ///", element)
    global flag
    flag = 0
    for i in range(len(element)):
        print("i", i)
        print("len(element)", len(element))
        print("element[i]", element[i])
        if element[i] in page_source:
            flag = 1
            print("flag == 1", element[i], flag, i)
            return element[i], flag
        else:
            continue
    if flag == 0:
        print("flag == 0", element[i], flag)
        return element[i], flag
