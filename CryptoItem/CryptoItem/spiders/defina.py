import scrapy
import json
import datetime
from time import sleep


class DefinaSpider(scrapy.Spider):
    name = 'defina'
    # market.theforce.trade
    allowed_domains = ['market.theforce.trade']
    # https://market.theforce.trade/home
    start_urls = ['https://market.theforce.trade/v2/sellorder/new_arrivals']

    def parse(self, response):
        # xpath .body不全含有css，以后再改
        # with open('defina.html', 'wb') as f:
        #     f.write(response.body)

        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('-----------', time, '-------------')
        #print(response.text)
        data_dict = json.loads(response.text)['data']
        for data in data_dict:
            name = data['name']
            # 获取最后的价格
            last_price = data['last_sale'][0:-18]
            if name == 'HeroBox':
                pass
                #print('卡片类型 Box   价格：' + last_price)
                # if int(last_price) <= 300:
                #     print('盲盒价格较低')
            else:
                # 获取卡片类型
                trait = data['trait']['rarity']
                trait1 = trait  # 复制一份
                # 补足3位长度
                if len(trait1) == 1:
                    trait1 = '  ' + trait
                elif len(trait1) == 2:
                    trait1 = ' ' + trait1
                if trait == 'A':
                    print('卡片类型 ' + trait + '  价格：' + last_price)
                    # if int(last_price) <= 40:
                    #     print('A卡价格较低')
                    # win32api.MessageBox(0, 'A卡价格较低', '提示', win32con.MB_OK
                elif trait == 'S':
                    print('卡片类型 ' + trait + '  价格：' + last_price)
                    # if int(last_price) <= 80:
                    #     print('S卡价格较低')
                    # win32api.MessageBox(0, 'S卡价格较低', '提示', win32con.MB_OK)
                elif trait == 'SS':
                    print('卡片类型 ' + trait + '  价格：' + last_price)
                    # if int(last_price) <= 500:
                    #     print('SS卡价格较低')
                    # win32api.MessageBox(0, 'SS卡价格较低', '提示', win32con.MB_OK)
                elif trait == 'SSS':
                    print('卡片类型 ' + trait + '  价格：' + last_price)
                    # if int(last_price) <= 3000:
                    #     print('SSS卡价格较低')
                    # win32api.MessageBox(0, 'SSS卡价格较低', '提示', win32con.MB_OK)
                else:
                    print('查询失败')
                    sleep(60)
        sleep(30)
        yield scrapy.Request(self.start_urls[0], callback=self.parse, dont_filter=True, meta={'download_timeout':20})




