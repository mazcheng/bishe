#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import time
import pickle
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

# TODO(yes) 实现 不同 分类 对应 集合 の URL 记录 并记录到 csv 中

browseUrl = 'http://202.200.151.19/browse/'

headers = {
    'Host': '202.200.151.19',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'PHPSESSID=m2vna2hih0qikp6024ntbi0fj2',
    'Connection': 'keep-alive'
}

def update_book_cls(book_cls):
    """
    Update the book_cls
    :params book_cls: book_cls Dict
    """
    with open('./book_cls_pickle_20170330/', 'w') as p:
        pickle.dump(book_cls, p)

def get_expand_tree(cls=None):
    """
    :params cls: book -> class Ex: 'A', 'A2'
    :return: bs.object
    """
    baseUrl = browseUrl + 'cls_browsing_tree.php'
    if cls:
        lvl = get_cls2level(cls)
    else:
        lvl = None
    pyload = {'s_doctype': 'all', 'cls': cls, 'lvl': lvl}
    response = requests.get(baseUrl, params=pyload, timeout=5, headers=headers)
    bsObj = BeautifulSoup(response.text, 'html.parser')
    return bsObj


def make_cls_record(cls=None, clsname=None, page=None):
    """
    :params cls: book -> class String
    :params clsname: book -> classname String
    :params page: book list -> page
    :return: bsObj
    """
    baseUrl = browseUrl + 'cls_browsing_book.php'
    pyload = {'s_doctype': 'all', 'cls': cls, 'clsname': clsname, 'page': page}
    try:
        response = requests.get(baseUrl, params=pyload, timeout=5, headers=headers)
        bsObj = BeautifulSoup(response.text, 'html.parser')
        # 'http://202.200.151.19/browse/cls_browsing_book.php' の length
        baseUrl_len = len(baseUrl)
        book_cls_id = cls
        _, b_clsname_tag, _, b_clsnum_tag = bsObj.find(id='titlenav').find_all('font')
        book_clsname = unicode(b_clsname_tag.text.split(' ')[1].encode('latin1').decode('utf8'))
        book_url = response.url[baseUrl_len:]
        book_cls_num = int(b_clsnum_tag.text)
        b_page_tag = bsObj.find('select', attrs={'name': 'topage'})
        if not b_page_tag:
            page_num = None
        else:
            page_num = int(b_page_tag.contents[-2].text)
        book_cls_record = {
        'cls_id': book_cls_id, 'cls_name': book_clsname,
        'base_url': book_url, 'cls_num': book_cls_num, 'max_page_num': page_num
        }
        return book_cls_record
    except Exception as e:
        return None
    

def get_cls2level(cls_id):
    """
    :params cls_id: book -> class id
    :return: current book cls level
    """
    cls_id = ''.join(cls_id.split('-'))
    level = len(cls_id)
    return level


def is_bottom_lvl(ele_tag):
    """
    :params ele_tag: element Tag object
    :return: TF
    """
    if not ele_tag.get('onclick', None):
        return True
    else:
        return False


def find_stepright_cls(bsObj, lvl):
    """
    :params bsObj: BeautifulSoup object
    :params lvl: current book cls level
    :return: match level Tag
    """
    cls_attr = 'stepright' + str(lvl)
    lvl_tag = bsObj.find_all(class_=cls_attr)
    return lvl_tag


def write_record(book_cls_list):
    with open('./level2url.csv', 'ab+') as csvfile:
        fieldnames = ['cls_id', 'cls_name', 'base_url', 'cls_num', 'max_page_num']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        # writer.writerow()
        # writer.writerow('\n')
        writer.writerows(book_cls_list)


def read_record(cls_id=None, clsname=None, baseUrl=None, max_page_num=None):
    with open('./level2url.csv', 'rb+') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pass


level1 = {}
level2 = {}

tree1 = get_expand_tree()
lvl_tag1 = find_stepright_cls(tree1, 1)

print 'start Tree...'
for _ in lvl_tag1:
    level1[_['id']] = _.text
    tree2 = get_expand_tree(_['id'][4:])
    lvl_tag2 = find_stepright_cls(tree2, 2)
    for _ in lvl_tag2:
        if is_bottom_lvl(_):
            # bottom level
            level2[_['id']] = (_.text, _.find('span')['onclick'])
        else:
            # not level = 2 but not bottom
            level2[_['id']] = (_.text, _.find_all('a')[1l]['onclick'])

book_cls = []

print 'start Book...'
for _ in level2:
    cls, clsname = level2[_][1][8:].split(',')
    cls = cls.strip("'")
    clsname = clsname.split(')')[0].strip("'")
    book_cls_record = make_cls_record(cls=cls, clsname=clsname)
    if isinstance(book_cls_record, dict):
        book_cls.append(book_cls_record)
    else:
        print cls
        continue
    time.sleep(2)

print 'start Csv...'
write_record(book_cls)