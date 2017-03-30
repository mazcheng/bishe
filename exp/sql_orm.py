#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.orm import 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
	"""docstring for Book"""
	__tablename__ = 'book'

	def __init__(self):
		super(Book, self).__init__()
	
	book_id = Column(Integer(), primary_key=True)
	book_name = Column(String(), index=True)
	book_isbn = Column(String())
	book_author = Column(String())
	book_press = Column(String())
	book_price = Column(String())
	book_date = Column(DateTime())

class LibBook(Book):
	"""docstring for LibBook"""
	__tablename__ = 'libbook'

	def __init__(self, arg):
		super(LibBook, self).__init__()
	
	# 中图法 分类[不唯一](索书[唯一]) 号
	book_clc = Column(String())
	# 可能不止一本
	book_jdc= Column(String())
	book_addr = Column(String())
	book_status = Column(String())
	# 借阅趋势 dict?
	book_trend = Column()
	# 学科主题 不唯一
	book_xkzt = Column()
