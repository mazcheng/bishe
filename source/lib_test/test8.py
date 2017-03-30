#!/usr/bin/env python
# -*- coding: utf-8 -*-

<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
=======
import re
import requests
from bs4 import BeautifulSoup, NavigableString
>>>>>>> refs/remotes/origin/master

# TODO(mzc)实现 对 全局 书 的统计 和 记录 数字
# TODO(mzc) 需要想办法实现对 所有 级别 的 书 进行分别记录啊
# 乱码的主要原因 beautifulsoup 自动将 str 转换成 Unicode

browseUrl = 'http://202.200.151.19/browse/'

def get_expand_tree(cls=None):
	baseUrl = browseUrl + 'cls_browsing_tree.php'
	if cls:
		lvl = get_cls2level(cls)
	else:
		lvl = None
	pyload = {'s_doctype': 'all', 'cls': cls, 'lvl': lvl}
	response = requests.get(baseUrl, params=pyload)
<<<<<<< HEAD
=======
	print response.url
>>>>>>> refs/remotes/origin/master
	bsObj = BeautifulSoup(response.text, 'html.parser')
	return bsObj

def get_expand_book(cls=None, clsname=None, page=None):
	baseUrl = browseUrl + 'cls_browsing_book.php'
	pyload = {'s_doctype': 'all', 'cls': cls, 'clsname': clsname, 'page': page}
	response = requests.get(baseUrl, params=pyload)
	# print response.url
	bsObj = BeautifulSoup(response.text, 'html.parser')
	return bsObj

def get_cls2level(cls_id):
	cls_id = ''.join(cls_id.split('-'))
	level = len(cls_id)
	return level

def is_bottom_lvl(ele_tag):
	if not ele_tag.get('onclick', None):
		return True
	else:
		return False

def find_stepright_cls(bsObj, lvl):
	cls = 'stepright' + str(lvl)
	lvl_tag = bsObj.find_all(class_=cls)
	return lvl_tag

id_title_searchF = {}
level1 = {}
level2 = {}
level3 = {}
level4 = {}
level5 = {}
level6 = {}

# 可以说明 不能 通过简单 的 字符串 来判断 我要的是第几集 好坑啊 若是 lvl 与 cls 无法匹配 就无法正常显示
tree = get_expand_tree()
lvl_tag = find_stepright_cls(tree, 1)
for _ in lvl_tag:
	level1[_['id']] = _.text
	tree2 = get_expand_tree(_['id'][4:])
	lvl_tag2 = find_stepright_cls(tree2, 2)
	for _ in lvl_tag2:
		if is_bottom_lvl(_):
			# 已经到底啦
			level2[_['id']] = (_.text, _.find('span')['onclick'])
		else:
			# 经检验 没有 WHY 在 level 2 中
			# len(level2) = 263
			level2[_['id']] = (_.text, _.find_all('a')[1].get('onclick', 'WHY'))
			# tree3 = get_expand_tree(_['id'][4:])
			# lvl_tag3 = find_stepright_cls(tree3, 3)
			# for _ in lvl_tag3:
			# 	if is_bottom_lvl(_):
			# 		level3[_['id']] = _.text
			# 	else:
			# 		level3[_['id']] = _.text
# 目前来说 从 当前 获取 所有 书 的 可能性 就在 lvl 2
summ = 0
for _ in level2.values():
	cls, clsname = _[1][8:].split(',')
	# print cls.strip("'"), clsname.split(')')[0].strip("'")
	# 因为获取到 の 字符串 会有 引号 括号 乱七八糟
	cls = cls.strip("'")
	clsname = clsname.split(')')[0].strip("'")
	book = get_expand_book(cls=cls, clsname=clsname)
	# print book.find(id='titlenav').find_all('font')[3].text
	summ += int(book.find(id='titlenav').find_all('font')[3].text)
print summ
# 时间大概 2 mins
<<<<<<< HEAD
# 379966 ~= 38W
=======
# 379966 ~= 38W
>>>>>>> refs/remotes/origin/master
