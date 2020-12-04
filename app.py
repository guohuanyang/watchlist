# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         app
# Description:  
# Author:       guohuanyang
# Date:         2020/11/3
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import os
import sys

from flask import Flask, render_template
from flask import escape, url_for
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)

tmp_name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.route('/')
def index():
    return render_template('index.html', name=tmp_name, movies=movies)


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
