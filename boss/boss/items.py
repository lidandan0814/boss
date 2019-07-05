# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BossItem(Item):
    岗位名称 = Field()
    薪资范围 = Field()
    工作地 = Field()
    工作经验 = Field()
    学历要求 = Field()
    公司名称 = Field()
    所属行业 = Field()
    融资阶段 = Field()
    公司规模 = Field()
