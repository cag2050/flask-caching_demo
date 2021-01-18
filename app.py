from flask import Flask
# from flask_cache import Cache
# 可使用 flask_caching 代替 flask_cache
from flask_caching import Cache
import os

app = Flask(__name__)

# simple
# cache = Cache(config={'CACHE_TYPE': 'simple'})

# filesystem
# '''
basedirs = os.path.abspath(os.path.dirname(__file__))
basedir = basedirs + '/cache'

cache = Cache(config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': basedir
})
# '''

cache.init_app(app)


@app.route('/test_cache')
# timeout 单位为秒
@cache.memoize(timeout=5)
def hello_world():
    print('如果在缓存有效期内，此行不会输出')
    return 'Hello, World!'
