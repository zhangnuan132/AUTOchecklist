import time

import conftest


def is_element_exist(element, page_source):
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
        if expected_text[i] in element_text[i]:
            print('element_text_compared%s 已找到%s元素' % (pretime, expected_text[i]))
        else:
            print("方法：element_text_compared  元素：element_name[i]) : ", expected_text[i])
            print('element_text_compared 没有找到%s元素' % (pretime, expected_text[i]))
    print('============================================================================================')
