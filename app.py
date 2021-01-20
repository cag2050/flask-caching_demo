import os
from flask import Flask, request
from flask_caching import Cache

app = Flask(__name__)

# simple
# cache = Cache(config={'CACHE_TYPE': 'simple'})

# filesystem
# '''
basedirs = os.path.abspath(os.path.dirname(__file__))
basedir = basedirs + '/cache'
cache = Cache(config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': basedir,
    # 最大的缓存条目数，超过该数会删除一些缓存条目。仅仅用于SimpleCache和 FileSystemCache。
    'CACHE_THRESHOLD': 5,
    # 单位为秒
    'CACHE_DEFAULT_TIMEOUT': 5,
})
# '''

cache.init_app(app)


@app.route('/test_cached')
@cache.cached()
def test_cached():
    print('test_cached: 调用了，没走缓存时，会打印')
    return 'Hello, cached!'


@app.route('/test_cached_query_string')
# 在对包含查询参数的路由，使用cache.cached()装饰器时，需要将参数query_string设为True，这会将排序后的查询参数散列值作为键
@cache.cached(query_string=True)
def test_cached_query_string():
    # linux命令行里curl请求例子：curl 'http://localhost:5000/test_cached_query_string?a=1&b=2'
    print('test_cached_query_string: 调用了，没走缓存时，会打印')
    a = request.args.get('a', '')
    b = request.args.get('b', '')
    return a + b + 'c'
