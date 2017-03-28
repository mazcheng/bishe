#!/apps/ns/python/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Sequence, DateTime, text
from sqlalchemy.sql import func, select

db_args = 'oracle://smns:smns@几毛/orcl?charset=utf8'

db = create_engine(db_args, encoding='utf8', echo=False)

metadata = MetaData(db)

conn = db.connect()
keyword = Table('TB_WEBRAY_KEYWORD', metadata,
		Column('ID', Integer, Sequence('TB_WEBRAY_KEYWORD_SEQ'), primary_key=True),
		Column('KEYWORD', String),
		Column('RECEIVED_AT', DateTime),
		Column('RECORD_TIME', DateTime),
		Column('DOMAIN', String),
		Column('TEST', String)
		)
db_conn_sql = "alter session set nls_date_format='yyyy-mm-dd hh24:mi:ss'"
conn.execute(db_conn_sql)
conn.begin()
# 实现 id > 30 の keyword
# 神他妈
#  s= select("SELECT ID, KEYWORD FROM TB_WEBRAY_KEYWORD")
s = keyword.select(keyword.c.ID < 30)
print s
rp = conn.execute(s)
for _ in rp.fetchall():
	print _
#  s = keyword.select()
#  s = select([keyword.c.ID])
#  print help(keyword.select)
#  rp = conn.execute(s)
#  print rp.first()  # 返回 第一 列 然后关闭 connect
#  print rp.fetchone()  # 跟上面一样 不关
#  print rp.scalar()  # 返回 id
#  print rp.scalar()  # 当前游标走到了 第 2 列 id
#  for _ in rp:
	#  print _.KEYWORD  # 保证 与 Table 定义同名
	#  if _.ID < 30:
		#  print _.KEYWORD
		#  print _[0]
#  print rp.keys()  # 返回 对应 列名
#  print rp.fetchall()
