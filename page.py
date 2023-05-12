from flask import Flask, render_template
import pymysql
import time
import random
import datetime
import pandas as pd
import numpy as np
import json

app = Flask(__name__)
@app.route('/')
def index():
    with open('steam.json', newline='') as f:
        data = json.load(f)
    return render_template('page.html',data = data)


@app.route('/statics')
def stats():
    with open('steam.json', newline='') as f:
        data = json.load(f)

    # 計算每個開發商出現次數
    publishers = {}
    for i in data:
        publisher = i['pubilsher']
        if publisher in publishers:
            publishers[publisher] += 1
        else:
            publishers[publisher] = 1

    # 排序開發商出現次數
    sorted_publisher = sorted(publishers.items(), key=lambda x: x[1], reverse=True)

    # 取出前10名開發商
    top_publishers = [publisher[0] for publisher in sorted_publisher[:10]]

    # 計算前10名開發商的出現次數
    publisher_counts = [publisher[1] for publisher in sorted_publisher[:10]]

    return render_template('stats.html', labels=top_publishers, values=publisher_counts)




if __name__ == '__main__':
    app.debug = True
    app.run()