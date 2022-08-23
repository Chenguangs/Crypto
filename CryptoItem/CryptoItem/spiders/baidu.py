import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print('--------111----------')
        title = response.xpath('/html/head/title/text()').extract_first()
        print(title)
