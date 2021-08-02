from app import app
import datetime
import time

@app.route('/api/home')
def home():
    return {'hello': 'hello world'}

@app.route('/api/time')
def get_time():
    return {
        'datetime': str(datetime.datetime.now()),
        'time': str(time.localtime(time.time()))
    }