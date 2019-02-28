# -*- coding: utf-8 -*-
import re
import time
import flask_excel as excel
from search_factory import SearchFactory
from settings import url_maps, name_maps
from common.ms_logs import log
from flask import Flask, render_template, jsonify, request

# name_map = url_map = 'hello world'
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', url_map=url_maps, name_map=name_maps)


@app.route('/exp_excel/<e_id>')
def exp_excel(e_id):
    """
    :param e_id: 根据e_id 决定下载Excel文件
    :return:
    """
    # 根据e_id 从数据库中查询信息，返回Excel文件
    result = {
        "专利名称": "邱哥钓鱼",
        "专利号": "1024",
        "专利类别": "发明",
        "日期": "2019.02.28"
    }
    column_names = list(result.keys())
    return excel.make_response_from_dict(
        result,
        column_names=column_names,
        file_type='xls',
        file_name='专利.xls'
    )


@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    web_site = data.get('web_site')
    web_site = int(web_site) if web_site else ''
    if web_site == 0:  # 专利
        patent_id = data.get('patent_id')
        patent_code = data.get('patent_code')
        # 校验参数是否完整
        if not all([patent_id, patent_code]):
            return jsonify({'code': 602, 'msg': '参数不完整！'})
        #  校验专利号是否合法
        if not re.match(r'\d{9}|\d{13}', patent_id):
            return jsonify({'code': 601, 'msg': '专利号不合法！'})
        post_data = {
            'patent_id': patent_id, 'patent_code': patent_code
        }
        log.info(post_data)
        # 调用爬虫，返回抓取结果
        result = SearchFactory(int(web_site)).draw(post_data)
        time.sleep(3)
        if not result:
            return jsonify({'code': 625, 'msg': '未获取信息，稍后重试'})
        return jsonify({'code': 600, 'e_id': patent_id, 'result': result})
    elif web_site == 1:  # 商标
        return jsonify({'msg': 'this is test'})
    elif web_site == 2:  # 国家企业信息
        return jsonify({'msg': 'this is test'})
    elif web_site == 3:  # 企查查
        return jsonify({'msg': 'this is test'})
    else:
        return jsonify({'msg': '没有选择站点'})


if __name__ == '__main__':
    log.init_log('info', True)
    excel.init_excel(app)
    app.run(debug=True)
