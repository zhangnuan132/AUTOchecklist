import os
import time
import pytest


def report(style: list):
    # 文件的命名不能有空格，要不会将 空格后识别成文件名
    if get_platform() == "windows":
        path_allure = os.getcwd() + r'\pytest_demo\report\xml'
        path_html = os.getcwd() + r'\pytest_demo\report\html'
        pass
    else:
        path_allure = os.getcwd() + '/pytest_demo/report/' + '/xml'
        path_html = os.getcwd() + '/pytest_demo/report/' + '/html'
    # 生成allure报告,/report/xml
    pytest.main(style + ['--alluredir={path_allure}'.format(path_allure=path_allure)])
    # # 方法1：allure serve  指定端口可以个指定本机ip同时使用
    # os.system('allure serve {path_allure} -o {path_html}'.format(path_allure=path_allure,
    #                                                              path_html=path_html) + ' -h 192.168.5.20 -p 14212')
    # 方法2：生成HTML报告,/report/html
    os.system(
        'allure generate {path_allure} -o {path_html} --clean'.format(path_allure=path_allure, path_html=path_html))
    # 开启allure web服务
    os.system('allure open {path_html}'.format(path_html=path_html))


def input_data():
    print("------------------***------------------\n"
          "输入数字和中文即可，其中 1: 我的,  2: 直播间,  3: 其他\n"
          "输入方法如下: \n"
          "方法1. 我的 \n"
          "方法2. 我的,直播间 \n"
          "方法3. 1,2\n"
          "------------------***------------------")
    arg = input("请输入想要执行的用例,用英文逗号分割: ")
    # 将逗号分割的关键字，用 or 输出，如 我的,直播间 ---> Mine or Live or Account
    # a = arg.split(',')
    arg = arg.replace('我的', 'Mine').replace('1', 'Mine') \
        .replace('直播间', 'Live').replace('2', 'Live') \
        .replace('账户', 'Account').replace('3', 'Account') \
        .replace('，', ' or ').replace(',', ' or ')
    print(arg, type(arg))
    return arg


# 如果发现其他系统需要区别，可以在这里加
def get_platform():
    import platform
    sys_platform = platform.platform().lower()
    if "windows" in sys_platform:
        return "windows"
        # print("Windows")
    elif "macos" in sys_platform:
        return "linux"
        # print("Mac os")
    elif "linux" in sys_platform:
        return "linux"
        # print("Linux")
    elif "darwin" in sys_platform:
        return "linux"
        # print("Mac os的子系统")
    else:
        print("其他系统先默认windows")
        return "Windows"


if __name__ == '__main__':
    # 判断的目的：区别路径写的方式
    if get_platform() == "windows":
        # testcases下的用例均可执行
        run_path = os.getcwd()
        # pytest执行时增加 参数，再下面语句中增加单引号即可 ，如批量执行 '-m','xxx'
        style0 = ['-s', '-m ' + input_data()] + [run_path + r'\testcases']
        print("style0", style0)
        report(style=style0)
    else:
        # testcases下的用例均可执行
        run_path = os.getcwd()
        # pytest执行时增加 参数，再下面语句中增加单引号即可 ，如批量执行 '-m','xxx'
        style0 = ['-s', '-m ' + input_data()] + [run_path + '/testcases']
        print("style0", style0)
        report(style=style0)
