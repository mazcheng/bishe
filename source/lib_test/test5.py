# -*- coding: utf-8 -*-

# 尝试 利用 selenium 来 A-Z 保存 至 dict
# 2017年3月29日17:09:57 实现 对 类别 1 2 级 的 打印 --> level263-22

import sys
import time
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://202.200.151.19/browse/cls_browsing.php'
# driver = webdriver.PhantomJS()
driver = webdriver.PhantomJS('C:\\Users\\mzc\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get(url)

# 切换到 tree frame 中
# 发现 切换到 level 2 下 即可 点击
#  http://202.200.151.19/browse/cls_browsing_book.php
#  ?s_doctype=all&
#  cls=T-01
#  &clsname=%26%23x65b9%3B%26%23x9488%3B%26%23x3001%3B%26%23x653f%3B%26%23x7b56%3B%26%23x53ca%3B%26%23x5176%3B%26%23x9610%3B%26%23x8ff0%3B
#  import HTMLParser to 转换 至 中文 现在需要将 中文 转换成 以上 Unicode
#  1. urllib.unicode() 将 url decode 成 html entity
#  2. HTMLParser.unescape() 将 html entity 成 unicode
#  3. 2 可 利用 BeautifulSoup 直接 转换

#  出现 问题 在 tree 中 level 2 url 正常
#  但当 出现 在 main 中 level 2 url 相比于上面 出现 很多  %26(&) %3b(;) 以 误导 我 但有规律
#  %26amp%3b == &amp; 指得是 &
#  规律:
#      %26 -> %26amp
#      %3B 两倍出现
#  tree 中 %26 与 %3b 同时出现 并中间 夹杂 一个 unicode 字符 三者 数量相同
#  main 中 %26amp 与 %3b 亦同时出现 但中间 先 夹杂一个 %3b 再 夹杂一个 unicode 字符 %3b 两倍于 其他两者

# 模拟归模拟 神他妈 还是 requests 好用 明知 GET 却不用

driver.switch_to_frame('tree')
len_stepright_list1 = len(driver.find_elements_by_class_name('stepright1'))
for _ in range(0, len_stepright_list1):
    stepright_list1 = driver.find_elements_by_class_name('stepright1')
    _ele = stepright_list1[_]
    print _ele.text
    _node_id = _ele.get_attribute('id')
    driver.find_element_by_id('img_' + _node_id).click()
    time.sleep(2)
    len_stepright_list2 = len(driver.find_elements_by_class_name('stepright2'))
    for _ in range(0, len_stepright_list2):
        stepright_list2 = driver.find_elements_by_class_name('stepright2')
        _ele = stepright_list2[_]
        # _ele.click()
        #  准确来说不是点击 _ele 而是 点击 其 第二 子节点 来触发
        print _ele.text
        # time.sleep(2)
        # driver.switch_to_default_content()
        # driver.switch_to_frame('main')
        # print driver.find_element_by_id('titlenav').text
        #  print driver.find_element_by_xpath('/html/body/form/div[1]/font[3]').text
driver.quit()

