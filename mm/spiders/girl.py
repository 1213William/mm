# -*- coding: utf-8 -*-
import scrapy
from fake_useragent import UserAgent
from scrapy.selector import Selector
from mm.items import MmItem

headers = {
    # 'user-agent': UserAgent(verify_ssl=False).chrome
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'UM_distinctid=16d68e3ebfe32b-0c81530cf904fc-38607701-1aeaa0-16d68e3ebff7bd; Hm_lvt_672e68bf7e214b45f4790840981cdf99=1569422830,1569507842; Hm_lpvt_672e68bf7e214b45f4790840981cdf99=1569544030; CNZZDATA1277874215=1602513911-1569420044-%7C1569538896',
    'pragma': 'no-cache',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer': 'https://www.mm131.net'
}


class GirlSpider(scrapy.Spider):
    name = 'girl'
    allowed_domains = ['www.mm131.com']
    target_url = 'http://www.mm131.com/xinggan/list_6_%s.html'
    container = []

    def start_requests(self):
        for i in range(2, 200):
            url = self.target_url % i

            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        for img_list in sel.xpath('//*[@class="main"]/dl/dd'):
            url = img_list.xpath('a/@href').extract_first()
            title = img_list.xpath('a/text()').extract_first()
            if url.startswith('https'):
                yield scrapy.Request(url, callback=self.parse_url_img, meta={'title': title}, headers=headers,
                                     dont_filter=True)
                # print(url, title)
    #         self.container.append(url)
    #     # 下一页的相对路径
    #     next_url = self.container[-1]
    #     for i in self.container[:-2]:
    #         # print(i)
    #         yield scrapy.Request(i, callback=self.parse_url_img, headers=headers, dont_filter=True)

    def parse_url_img(self, response):
        item = MmItem()
        sel = Selector(response)
        container = []
        # 获得对应的图集下的照片的张数
        count = sel.xpath('//*[@class="content-page"]/span/text()').extract()
        all_count = count[0][1:3]
        num = response.url.split('/')[-1].strip('.html')
        for index in range(int(all_count)):
            cmp_url = f'https://img1.mmmw.net/pic/{num}/{index}.jpg'
            container.append(cmp_url)
            # print(container)
        item['url'] = container
        item['title'] = response.meta['title']
        yield item
        container.clear()



