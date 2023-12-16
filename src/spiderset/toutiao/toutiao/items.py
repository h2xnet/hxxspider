# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToutiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # toutiaoSuggest fields
    # 头条推荐爬虫字段
    toutiaoSuggestResponseText = scrapy.Field()

    pass
