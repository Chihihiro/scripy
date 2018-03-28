# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class GetDoubanItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
class zhaoyangItem(scrapy.Item):
    fund_id = scrapy.Field()
    fund_full_name = scrapy.Field()
    foundation_date = scrapy.Field()
    fund_manager = scrapy.Field()
    fund_status= scrapy.Field()
    fund_manager_nominal= scrapy.Field()
    fund_member= scrapy.Field()
    data_source= scrapy.Field()
    fund_name = scrapy.Field()
    reg_code = scrapy.Field()
    fund_type_structure = scrapy.Field()
    open_date = scrapy.Field()
    type_name = scrapy.Field()
    data_freq = scrapy.Field()
    fund_custodian = scrapy.Field()
    locked_time_limit = scrapy.Field()
    min_purchase_amount = scrapy.Field()
    purchase_status = scrapy.Field()
    fund_stockbroker = scrapy.Field()
    redemption_status = scrapy.Field()
    recommendation_end = scrapy.Field()
    reg_time = scrapy.Field()
    orientation= scrapy.Field()





