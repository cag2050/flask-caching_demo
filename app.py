from flask import Flask
from flask_cache import Cache

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})


@app.route('/test_cache')
@cache.cached(timeout=5)
def hello_world():
    print('if cache，the second request do not print')
    return 'Hello, World!'
