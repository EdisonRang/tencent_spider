# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()       # 职位名称
    link = scrapy.Field()       # 详细链接
    category = scrapy.Field()   # 职位类别
    num = scrapy.Field()        # 需求人数
    address = scrapy.Field()    # 就职地点
    pub_time = scrapy.Field()   # 发布时间