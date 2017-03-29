#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://202.200.151.19/browse/cls_browsing_tree.php
# GET: ?s_doctype=all&cls=A&lvl=1
# mean: 展开 A 类下 所有子类 当前 展开 第 1 级
# GET: ?s_doctype=all&cls=A1&lvl=2
# mean: 展开 A1类下 所有子类 当前 展开 第 2 级
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
# requests.get(url, payload_dict)
# bs 来 检测当前 还有那些 id 下 a 对应 src 是否 还是 ../tpl/images/open.png
# 判断是否还可以展开
# 是 则 还可以展开
# 否 则 已经到 最低级
# 以上过程 用一个 id: searchF(url) dict 对 来记录当前 id
# 以上过程 仅仅使用 GET 而不用模拟 Browser
# id_url_dict: 是否可以 嵌套 添加 以 level 区分
[{A}
 {B}
 {C}
 {D}
 ...
 ]
%26%23x9a6c%3B%26%23x514b%3B%26%23x601d%3B%26%23x3001%3B%26%23x6069%3B%26%23x683c%3B%26%23x65af%3B%26%23x3001%3B%26%23x5217%3B%26%23x5b81%3B%26%23x3001%3B%26%23x65af%3B%26%23x5927%3B%26%23x6797%3B%26%23x3001%3B%26%23x6bdb%3B%26%23x6cfd%3B%26%23x4e1c%3B%26%23x3001%3B%26%23x9093%3B%26%23x5c0f%3B%26%23x5e73%3B%26%23x751f%3B%26%23x5e73%3B%26%23x548c%3B%26%23x4f20%3B%26%23x8bb0%3B

http://202.200.151.19/browse/cls_browsing_book.php?s_doctype=all&cls=A7&clsname=%26%23x9a6c%3B%26%23x514b%3B%26%23x601d%3B%26%23x3001%3B%26%23x6069%3B%26%23x683c%3B%26%23x65af%3B%26%23x3001%3B%26%23x5217%3B%26%23x5b81%3B%26%23x3001%3B%26%23x65af%3B%26%23x5927%3B%26%23x6797%3B%26%23x3001%3B%26%23x6bdb%3B%26%23x6cfd%3B%26%23x4e1c%3B%26%23x3001%3B%26%23x9093%3B%26%23x5c0f%3B%26%23x5e73%3B%26%23x751f%3B%26%23x5e73%3B%26%23x548c%3B%26%23x4f20%3B%26%23x8bb0%3B
