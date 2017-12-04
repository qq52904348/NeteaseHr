# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeteaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName=scrapy.Field()
    positionLink=scrapy.Field()
    positionType=scrapy.Field()
    workType=scrapy.Field()
    workLocation=scrapy.Field()
    positionNumber=scrapy.Field()
    publishTime=scrapy.Field()
