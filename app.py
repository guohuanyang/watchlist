# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         app
# Description:  
# Author:       guohuanyang
# Date:         2020/11/3
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
from flask import Flask
from flask import escape, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to my watchlist!!!'


@app.route('/user/<name>')
def user_page(name):
    return 'User page: {}'.format(escape(name))


@app.route('/test')
def test_url_for():
    print(url_for('test_url_for'))
    print(url_for('hello'))
    print(url_for('user_page', name='guohuayang'))
    print(url_for('user_page', name='chenjiani'))
    print(url_for('test_url_for', name=1))
    return 'test page'
