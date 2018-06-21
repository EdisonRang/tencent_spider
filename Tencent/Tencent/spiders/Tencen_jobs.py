# -*- coding: utf-8 -*-
import scrapy


class TencenJobsSpider(scrapy.Spider):
    name = 'Tencen_jobs'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    def parse(self, response):
        pass
