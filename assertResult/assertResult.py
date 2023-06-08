import time

import conftest
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
josn_test = {
	'Modle_mine': {
		'Mine': { # 底部我的tab
			'Mine_ids': ['com.huajiao:id/of'],
			'Mine_text': ['我的']
		},
		'Mine_zhubo': { # 我的-我的主播
			'Mine_ids': ['com.huajiao:id/dsy'],
			'Mine_text': ['主播']
		},
		'Mine_task': {  # 我的-我的任务
			'Mine_ids': ['com.huajiao:id/qu'],
			'Mine_text': ['我的任务']
		},
		'Mine_message': {  # 我的-我的私信
			'Mine_ids': ['com.huajiao:id/pe_message', 'com.huajiao:id/caa_message'],
			'Mine_text': ['我的消息'],
			'message_id_text': ["//*[@resource-id='com.huajiao:id/tz'][@text='消息']"],
			'Mine_subid_sixintitle': ['com.huajiao:id/dqb'],
			'Mine_subid_peopleicon': ['com.huajiao:id/dqj'],
			'Mine_subid_kefuicon': ['com.huajiao:id/e72']
		},
		'Mine_dynamic': { # 我的-我的动态
			'Mine_ids': ['com.huajiao:id/tz','com.huajiao:id/qu' ],
			'Mine_text': ['我的动态'] ,
			'dynamic_id_text': ["//*[@resource-id='com.huajiao:id/tz'][@text='我的动态']"],
			'Mine_xpath': ["//android.widget.RelativeLayout/android.widget.FrameLayout[1]//android.widget.LinearLayout[4]/android.widget.TextView"],
			'Mine_subxpath_zuopin': ["//android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[1]"],
			'Mine_subxpath_dynamic': ["//android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[2]"],
			'Mine_subxpath_data': ["//android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[3]"],
			'Mine_subtext_zuopin': ['作品'],
			'Mine_subtext_dynamic': ['动态'] ,
			'Mine_subtext_data': ['资料']
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

# 1. 此方法是为了 分成两个  2. list转化为str
def json_all(list):
	# print(list)
	for k in range(len(list)):
		str_list = "".join(list[k])
	return str_list


def is_element_exist2(element, page_source):
    time.sleep(5)
    # dirver = Initialization_parameters.initialization_parameters('Android', 'ELZ_AN00')
    element_key = list(element.keys())
    # print(element_key)
    element_name = list(element.values())
    # print(element_name)
    # print('page_source = ', page_source)
    pretime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
    for i in range(len(element)):
        # assert element_key[i] in page_source,'%s 没有找到%s元素' %(pretime,element_name[i])
        if element_key[i] in page_source:
            print('is_element_exist%s 已找到%s元素' % (pretime, element_name[i]))
        else:
            print("方法：is_element_exist%s  元素：element_name[i]) : ", element_name[i])
            print('is_element_exist 没有找到%s元素' % (pretime, element_name[i]))


def element_text_compared(element_text, expected_text):
	time.sleep(5)
	pretime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
	for i in range(len(element_text)):
		print("expected_text[i] ::是", expected_text[i], type(expected_text[i]))
		print("element_text[i] ::是", element_text[i],type(element_text[i]))
		if expected_text[i] in element_text[i]:
			print('element_text_compared%s 已找到%s元素' % (pretime, expected_text[i]))
		else:
			print("方法：element_text_compared  元素：element_name[i]) : ", expected_text[i])
			print('element_text_compared 没有找到%s元素' % (pretime, expected_text[i]))
		print('============================================================================================')
