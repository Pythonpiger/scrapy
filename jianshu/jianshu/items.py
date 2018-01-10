# -*- coding: utf-8 -*-

import scrapy
class JianshuItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    times = scrapy.Field()
    url = scrapy.Field()
    admire = scrapy.Field()
    likes = scrapy.Field()
