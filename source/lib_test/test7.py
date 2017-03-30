# -*- coding: utf-8 -*-

# 尝试 利用 树(不是 binary)遍历 の 方法实现 对 node の 遍历

#  nodeA
#  + nodeA1
#  ++ nodeA11
#  +++ nodeA112

# webdriver 先 点击 level1 再 点击 level2 以此类推 X
# 好像 不能同时 展开 不同级别的 即 展开 A 就不能展开 B
#  配合 bs4 一起处理
#  TODO(mzc) 大力 出 杯具 -> 二级下 即可点击 div main 出现
import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
            try:
                driver.find_element_by_id('img_' + _node_id).click()
                time.sleep(2)
            except NoSuchElementException:
                print 'No ...'
            return get_element_name(level + 1)


if __name__ == '__main__':
    url = 'http://202.200.151.19/browse/cls_browsing.php'
    driver = webdriver.PhantomJS('C:\\Users\\mzc\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    driver.get(url)
    # 切换到 tree frame 中
    driver.switch_to_frame('tree')
    #  http://www.51testing.com/html/21/n-862721-2.html
    get_element_name(1)
    driver.quit()

#  <div style="display: block;" class="stepright3" id="nodeP96" name="nodeP96" onclick="test(this)">
#      <a href="javascript:expandTree('P96',3)">
#          <img src="../tpl/images/open.png" title="展开" id="img_nodeP96" name="img_nodeP96" border="0">
#      </a>
#      <a title="自然资源学" style="cursor:hand;" target="main" onclick="searchF('P96','%26%23x81ea%3B%26%23x7136%3B%26%23x8d44%3B%26%23x6e90%3B%26%23x5b66%3B')">
#      P96 自然资源学
#      </a>
#      <span id="P96">
#      </span>
#  </div>
#  <div style="display: block;" id="nodeP97" name="nodeP97" class="stepright3 ">
#      <img src="../tpl/images/blank.png">
#      <span title="地理探险与发现" style="cursor:hand;" onclick="searchF('P97','%26%23x5730%3B%26%23x7406%3B%26%23x63a2%3B%26%23x9669%3B%26%23x4e0e%3B%26%23x53d1%3B%26%23x73b0%3B')">
#      P97 地理探险与发现
#      </span>
#  </div>
