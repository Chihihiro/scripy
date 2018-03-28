# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from engine import *
from items import zhaoyangItem
import pandas as pd

def dff_df(df):
    df2=df.T
    df4 = df2[df2[0] != ""]
    dff=df4.T
    return dff

class GetDoubanPipeline(object):
    def process_item(self, item, spider):
        c = pd.DataFrame([item])
        d=dff_df(c)
        to_sql("d_fund_info", engine5, d, type="update")
        return item







