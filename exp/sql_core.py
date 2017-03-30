#!/apps/ns/python/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Sequence, DateTime, text, and_, or_, not_, update, delete
from sqlalchemy.sql import func, select
from datetime import datetime

db_args = 'oracle://smns:smns@172.20.21.212:1521/orcl?charset=utf8'

db = create_engine(db_args, encoding='utf8', echo=False)

metadata = MetaData(db)

conn = db.connect()
keyword = Table('TB_WEBRAY_KEYWORD', metadata,
		Column('ID', Integer, Sequence('TB_WEBRAY_KEYWORD_SEQ'), primary_key=True),
		Column('KEYWORD', String),
		Column('RECEIVED_AT', DateTime, default=func.now()),
		Column('RECORD_TIME', DateTime, default=func.now()),
		Column('DOMAIN', String),
		Column('TEST', String),
		Column('URL', String)
		)
db_conn_sql = "alter session set nls_date_format='yyyy-mm-dd hh24:mi:ss'"
conn.execute(db_conn_sql)
#  sqlalchemy.engine.base.RootTransaction object
tran = conn.begin()
#  实现 分组
#  group_by #  实现 连接
#  实现 表 别名
#  key = keyword.alias('key_alias')
#  stmt = select([key.c.ID]).where(and_(key.c.ID == 11111111, key.c.URL== 'www.1212.cn'))
#  print stmt
#  实现 删除
#  d = delete(keyword).where(keyword.c.ID == 10000)
#  res = conn.execute(d)
# 实现 更新
#  u = update(keyword).where(keyword.c.ID == 10000)
#  u = u.values(KEYWORD=(keyword.c.KEYWORD + u'热得很'))
#  #  u = u.values(KEYWORD='热得很')
#  res = conn.execute(u)
# 实现 插入
#  ins = keyword.insert().values(
#                  ID = 10000,
#                  KEYWORD = u'任子行',
#                  RECEIVED_AT = datetime(2016, 6, 3, 15, 53, 33),
#                  RECORD_TIME = datetime(2016, 6, 3, 15, 53, 33),
#                  DOMAIN = 'www.1218.com',
#                  TEST = 'test',
#                  URL = 'www.1218.com'
#                  )
#  result = conn.execute(ins)
tran.commit()
#  print result.inserted_primary_key
conn.close()
# 实现 id > 30 の keyword
# 神他妈
#  s= select("SELECT ID, KEYWORD FROM TB_WEBRAY_KEYWORD")
#  TODO(mzc) 实现 对 select 控制 の 使用
#  s = keyword.select(keyword.c.ID < 30)
#  print s
#  rp = conn.execute(s)
#  for _ in rp.fetchall():
	#  print _[0]
#  m = select([keyword.c.KEYWORD, keyword.c.DOMAIN, keyword.c.ID])
#  m = select([keyword.c.ID])
#  m = keyword.select(keyword.c.ID < 30)
#  m = m.order_by(keyword.c.ID)
#  m = m.limit(5)  # 限制 查询 条数 是 5 条
#  m = select([func.sum(keyword.c.ID)])  # 求 ID 和
#  m = select([func.count(keyword.c.ID)])  # 求 条数(满足条件的)
#  rp = conn.execute(m)
#  #  print rp.scalar()
#  res = rp.first()
#  print res.keys()  # 神他妈 这里 直接将 对应 key 替换成 count_1
#  print res.count_1
#  m = select([func.count(keyword.c.ID).label(u'我曹')])  # 设置别名
#  m = select([keyword]).where(keyword.c.ID == 30) 过滤
#  m = select([keyword]).where(keyword.c.KEYWORD.like(u'中%'))  # 过滤 使用 like
#  m = select([keyword]).where(and_(keyword.c.ID < 100, keyword.c.KEYWORD.like(u'中%')))  # 过滤 使用 like
#  rp = conn.execute(m)
#  print rp.first()[1]
#  print rp.keys()[0]
#  print rp.first()
#  for _ in rp.fetchall():
#          print _
	#  print _.ID, _.KEYWORD
#  for _ in rp.fetchall():
	#  print _
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
