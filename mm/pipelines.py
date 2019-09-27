# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import requests

from mm.settings import IMAGES_STORE

from mm.spiders.girl import headers


class MmPipeline(object):
    def process_item(self, item, spider):
        """
        1、首先需要创建文件对应的顶头文件
        2、创建对应的图集文件
        3、将对应的照片下载到对应的图集中去
        :param item:
        :param spider:
        :return:
        """
        title = item['title']
        img_list = item['url']
        # print(img_list)
        # print(title, img_list)
        if not os.path.exists(IMAGES_STORE):
            os.mkdir(IMAGES_STORE)
        # 图集文件夹路径
        collection_url = os.path.join(IMAGES_STORE, title)
        # print(collection_url)
        if not os.path.exists(collection_url):
            os.mkdir(collection_url)
        for i in range(len(img_list)):
            cmp_url = os.path.join(collection_url, str(i))
            with open(cmp_url + '.jpg', 'wb') as fp:
                fp.write(requests.get(img_list[i], headers=headers).content)
                print('insert successfully!!!')





        # return item
