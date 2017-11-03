# -*- coding: utf-8 -*-
import scrapy
from hellobi.items import HellobiItem
from scrapy.http import Request

class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/1']


    def parse(self, response):
        lesson = HellobiItem()
        lesson['title'] = response.xpath('//li[@class="active"]/text()').extract()
        lesson['link'] = response.xpath('//li[@class="active"]/a/@href').extract()
        lesson['number'] = response.xpath('//span[@class="course-view"]/text()').extract()

        yield lesson
        for i in range(2,200):
            url = 'https://edu.hellobi.com/course/'+str(i)
            yield Request(url,callback=self.parse)
