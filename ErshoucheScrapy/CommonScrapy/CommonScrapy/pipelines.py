# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
# 存到sqlite数据库
class CommonscrapyPipeline(object):
    def __init__(self):
        """"""
        self.conn=sqlite3.connect('ershouche2.db')
        self.cursor=self.conn.cursor()
        self.cursor.execute('create table IF NOT EXISTS tongcheng(name_a,name_c text,data_c text,money text);')
        self.conn.commit()
    def process_item(self, item, spider):
        sql_str = "INSERT INTO tongcheng VALUES ('"+item["name_a"]+"','"+item["name_c"]+"','"+item["data_c"]+"','"+item["money"]+"')"
        self.cursor.execute(sql_str)
        self.conn.commit()
        return item
#     def process_item(self, item, spider):
#         conn = sqlite3.connect('country.db')
#         cursor = conn.cursor()
#         # save_dic = {'name': item['name'], 'data': item['data'], 'money':item['money']}
#
#         # 下面注释掉的只用一次，创建数据库用
#         # sql_insert = '''create table tongcheng(
#         #               name text,
#         #               data text,
#         #               money text)'''
#         # cursor.execute(sql_insert)
#         sql = '''insert into tongcheng(name,data,money) values (?,?,?)'''
#         cursor.execute(sql, (item['name'], item['data'], item['money']))
#         conn.commit()
#
#         return item