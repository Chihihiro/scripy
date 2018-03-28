import pymysql
import pandas as pd
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from iosjk import to_sql

connect = pymysql.connect(  # 连接数据库服务器
    user="jr_admin_4",
    password="jr_admin_4",
    host="182.254.128.241",
    port=4171,
    db="base",
    charset="utf8"
)
conn = connect.cursor()  # 创建操作游标
# 你需要一个游标 来实现对数据库的操作相当于一条线索

                         # 查看
conn.execute("SELECT fund_id,fund_name,fund_full_name FROM fund_info WHERE fund_id like 'JR00000%'")  # 选择查看自带的user这个表  (若要查看自己的数据库中的表先use XX再查看)
rows = conn.fetchall()  # fetchall(): 接收全部的返回结果行，若没有则返回的是表的内容个数 int型
info=[]
for i in rows:
    info.append(i[0])

# print(i[1])
print(info)
allinfo=[]
# info=['JR00001','JR000002','JR000003','JR000004','JR000005','JR000006','JR000012','JR002002','JR000022']

result = pd.DataFrame(columns=['fund_id',
                               'typestandard_code',
                               'typestandard_name',
                               'type_code',
                               'type_name',
                               'stype_code',
                               'stype_name'
                               ])

k = [600, '按全产品分类', 60001, '全产品', 6000101, '全产品']
temp = [k]*len(info)
result.loc[:, 'fund_id'] = info
result.loc[:, [ 'typestandard_code',
                               'typestandard_name',
                               'type_code',
                               'type_name',
                               'stype_code',
                               'stype_name']] = temp
# for i in range(len(k)):
#     result.iloc[:, i+1] = k[i]
dataframe= result
print(result)
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root','','localhost',3306,'test', ), connect_args={"charset": "utf8"},echo=True,)
to_sql("fund_type_mapping_import", engine, dataframe)