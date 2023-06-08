import pytest
import time



def report(style: list):
    path_allure = '/pytest_demo/report/' + time.strftime('%Y_%m_%d', time.localtime(time.time())) + '/xml'
    path_html = '/pytest_demo/report/' + time.strftime('%Y_%m_%d', time.localtime(time.time())) + '/html'
    # 生成allure报告
    pytest.main(style + ['--alluredir={path_allure}'.format(path_allure=path_allure)])
    # 生成HTML报告
    os.system('allure generate {path_allure} -o {path_html} --clean'
              .format(path_allure=path_allure, path_html=path_html))
    # 开启allure web服务
    os.system('allure open {path_html}'.format(path_html=path_html))


if __name__ == '__main__':
    style0 = ['-s', 'F:\\pytest_demo\\test_case\\test_selenium_case\\test_1.py']
    # pytest.main(['-s', 'F:\\pytest_demo\\test_case\\test_selenium_case\\test_1.py'])
    report.report(style=style0)