# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http  import Request
from hellobi.items import AutoHellobiItem
import time


class AutolessonSpider(CrawlSpider):
    name = 'autolesson'
    allowed_domains = ['hellobi.com']
    '''start_urls = ['http://hellobi.com/']'''
    def start_requests(self):
        head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10771.400'}
        yield Request(url='https://edu.hellobi.com/', headers=head)

    rules = (
        Rule(LinkExtractor(allow=r'https://edu.hellobi.com/course/.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        auto = AutoHellobiItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        auto['title'] = response.xpath('//li[@class="active"]/text()').extract()
        auto['link'] = response.xpath('//li[@class="active"]/a/@href').extract()
        auto['number'] = response.xpath('//span[@class="course-view"]/text()').extract()
        auto['price'] = response.xpath('//span[@class="price-expense"]/text()').extract()
        auto['free'] = response.xpath('//span[@class="price-free"]/text()').extract()
        return auto

