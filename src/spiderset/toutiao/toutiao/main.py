from scrapy import cmdline

print("toutiao spider Hello World!")

cmdline.execute("scrapy crawl toutiao_suggest".split())       #--nolog是以不显示日志的形式运行，如果需要看详细信息，可以去掉