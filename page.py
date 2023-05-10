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

if __name__ == '__main__':
    app.debug = True
    app.run()