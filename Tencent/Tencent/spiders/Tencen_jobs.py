# -*- coding: utf-8 -*-
import scrapy

from Tencent.items import TencentItem


class TencenJobsSpider(scrapy.Spider):
    name = 'Tencen_jobs'
    allowed_domains = ['tencent.com']
    # 修改起始url
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        # 获取职位节点列表
        node_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")
        # 遍历列表抽取数据
        for node in node_list:
            item = TencentItem()
            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['link'] = "https://hr.tencent.com/" + node.xpath('./td[1]/a/@href').extract_first()
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['num'] = node.xpath('./td[3]/text()').extract_first()
            item['address'] = node.xpath('./td[4]/text()').extract_first()
            item['pub_time'] = node.xpath('./td[5]/text()').extract_first()
            yield item

        # 提取下一页链接
        next_url = response.xpath('//a[@id="next"]/@href').extract_first()
        if next_url != 'javascript:;':
            # 构建下一页URL
            next_url = 'https://hr.tencent.com/' + next_url

            yield scrapy.Request(next_url, callback=self.parse)

