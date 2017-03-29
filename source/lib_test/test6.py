# -*- coding: utf-8 -*-

# 尝试 递归调用 level 并打印

import sys
import time
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')


def get_element_name(level):
    """
    未知 level の 获取 text
    """
    len_stepright = len(driver.find_elements_by_class_name('stepright' + str(level)))
    if not len_stepright:
        return 0
    else:
        for _ in range(0, len_stepright):
            stepright_list = driver.find_elements_by_class_name('stepright' + str(level))
            _ele = stepright_list[_]
            print _ele.text
            _node_id = _ele.get_attribute('id')
            # 这里在 最后 level 会不存在 img_ 's id
            driver.find_element_by_id('img_' + _node_id).click()
            time.sleep(2)
    return get_element_name(level + 1)

if __name__ == '__main__':
    url = 'http://202.200.151.19/browse/cls_browsing.php'
    # driver = webdriver.PhantomJS()
    driver = webdriver.PhantomJS('C:\\Users\\mzc\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    driver.get(url)
    # 切换到 tree frame 中
    driver.switch_to_frame('tree')
    #  http://www.51testing.com/html/21/n-862721-2.html
    get_element_name(1)
    driver.quit()
