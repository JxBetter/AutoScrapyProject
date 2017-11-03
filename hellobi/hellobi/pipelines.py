# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HellobiPipeline(object):
    def process_item(self, item, spider):
        # print(item['title'])
        # print(item['link'])
        # print(item['number'])
        return item

class AutoHellobiPipeline(object):
    def __init__(self):
        self.fp = open('E:/python/20171103/result.txt','a')
    def process_item(self, item, spider):
        try:
            print(item['title'][0])
            print(item['link'][0])
            print(item['number'][0])
            if item['price']:
                print(item['price'])
            if item['free']:
                print(item['free'])
            print('-------------------------------')
            self.fp.write(item['title'][0]+'\n'+item['link'][0]+'\n'+item['number'][0])
        except Exception as e:
            print(e)
        return item
    def close_spider(self):
        self.fp.close()