# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import time
from CommonScrapy.items import ErshoucheItem

class ZhilianSpiderSpider(scrapy.Spider):
    name = 'zhilian_spider'
    # allowed_domains = ['www.zhaopin.com']
    start_urls = ['https://zz.58.com/ershouche/pn1/']

    def parse(self, response):
        for i in range(1,71):
            next_url='https://zz.58.com/ershouche/pn{}/'.format(i)
            time.sleep(3)
            yield Request(next_url,callback=self.parse_xq)

    def parse_xq(self, response):
        for i in range(2,165):
            rs1=response.xpath('//ul/li[{}]/div[2]/a/h1/font/text()'.format(i)).extract()
            rs = response.xpath('//ul/li[{}]/div[2]/a/h1/text()'.format(i)).extract()
            rl0=''
            for r0 in rs:
                rl0+=r0
            rl=''
            for r in rs1:
                rl+=r
            rs2=response.xpath('//ul/li[{}]/div[2]/div[1]/span/text()'.format(i)).extract()
            rl2=''
            for r2 in rs2:
                rl2+=r2
            rs3=response.xpath('//ul/li[{}]/div[3]/h3/text()'.format(i)).extract()
            rl3=''
            for r3 in rs3:
                rl3+=r3
            item=ErshoucheItem()
            item['name_c']=rl+rl0.replace(' ','')
            item['data_c']=rl2
            item['money']=rl3

            yield item
