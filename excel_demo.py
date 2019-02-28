# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import flask_excel as excel
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exp_excel', methods=['GET'])
def exp_excel():
    fields = [['姓名', '年龄'], ["小明", 18], ["小红", 17], ['小邱', 25]]
    return excel.make_response_from_array(
        fields,
        column_names=['姓名', '年龄'],
        file_type='xls',
        file_name='user.xls'
    )


if __name__ == '__main__':
    excel.init_excel(app)
    app.run(debug=True)
