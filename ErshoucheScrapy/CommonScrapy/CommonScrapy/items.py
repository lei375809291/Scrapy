# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class CommonscrapyItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     # def process_item(self,job_des):
#     job_des=scrapy.Field()
class ErshoucheItem(scrapy.Item):
    name_c=scrapy.Field()
    data_c=scrapy.Field()
    money=scrapy.Field()
