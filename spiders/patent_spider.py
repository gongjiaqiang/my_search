# -*- coding: utf-8 -*-
"""
专利爬虫
"""
import requests


class PatentSpider(object):
    captcha_url = 'http://cpquery.sipo.gov.cn/freeze.main?txn-code=createImgServlet&freshStept=1'
    pass

    def draw(self, *args, **kwargs):
        result = {
            "专利名称": "邱哥钓鱼",
            "专利号": "1024",
            "专利类别": "发明",
            "日期": "2019.02.28"
        }

        #  爬虫获取抓取结果，保存到数据库中，并返回结果
        return result


