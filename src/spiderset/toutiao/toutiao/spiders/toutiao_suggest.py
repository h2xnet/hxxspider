import scrapy
from toutiao.items import ToutiaoItem

import sys
sys.path.append('..')
from toutiao.common import item_toutiao_suggest_response_text_key

#
# Desc: 头条推荐爬虫
# Auth: zfs
# Date: 2023-12-15
#
class ToutiaoSuggestSpider(scrapy.Spider):
    name = "toutiao_suggest"
    allowed_domains = ["www.toutiao.com"]
    start_urls = ["https://www.toutiao.com"]

    def parse(self, response):
        #pass
        item = ToutiaoItem()

        item[item_toutiao_suggest_response_text_key] = response.text

        # 提交item到管道文件
        yield item
