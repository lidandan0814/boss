# -*- coding: utf-8 -*-
import scrapy
from boss.items import BossItem


class BosszhipinSpider(scrapy.Spider):
    name = 'bosszhipin'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100-p100599/?page=1/']


    def parse(self, response):
        jobs = response.css('.job-box .job-list ul li .job-primary')
        for job in jobs:
            item = BossItem()
            item['岗位名称'] = job.css('.job-title::text').extract_first()
            item['薪资范围'] = job.css('.red::text').extract_first()
            item['工作地'] = job.css('.info-primary p::text').extract()[0]
            item['工作经验'] = job.css('.info-primary p::text').extract()[1]
            item['学历要求'] = job.css('.info-primary p::text').extract()[-1]
            item['公司名称'] = job.css('.company-text .name a::text').extract_first()
            item['所属行业'] = job.css('.company-text p::text').extract()[0]
            item['融资阶段'] = job.css('.company-text p::text').extract()[1]
            item['公司规模'] = job.css('.company-text p::text').extract()[-1]
            yield item

        next = response.css('.page .next::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
