# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuemojiItem(scrapy.Item):
    image_url = scrapy.Field()
    answer_id = scrapy.Field()