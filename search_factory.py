# -*- coding: utf-8 -*-

from spiders import *

# 爬虫对应的ID
search_ids = {
    0: PatentSpider,  # 专利
    1: TrademarkSpider,  # 商标
    2: CreditSpider,  # 国家信用信息
    3: BusinessCheckSpider  # 企查查
}


class SearchFactory:
    """工厂类"""
    maps = search_ids

    def __new__(cls, search_id):
        if search_id in SearchFactory.maps.keys():
            return SearchFactory.maps[search_id]()
        else:
            return
