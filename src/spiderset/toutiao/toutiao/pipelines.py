# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
import common

class ToutiaoPipeline:
    def process_item(self, item, spider):

        tmpOutPath = common.out_tmp_file_path
        tmpOutFileName = tmpOutPath + '/toutiaoSuggest.txt'
        print('pipelines tmp output file: ' + tmpOutFileName)
        
        toutiaoSuggestResponseText = item[common.item_toutiao_suggest_response_text_key]
        print("pipelines toutiaoSuggestResponseText: " + toutiaoSuggestResponseText)

        # obj = {}
        # obj.update(common.item_toutiao_suggest_response_text_key, toutiaoSuggestResponseText)

        with open(tmpOutFileName, 'a', encoding='utf-8') as f:
            f.write(toutiaoSuggestResponseText)
            f.close()

        return item
