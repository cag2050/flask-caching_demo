### 说明
1. Flask-Caching 是 Flask-Cache 扩展（ https://github.com/thadeusb/flask-cache ）的派生（fork），旨在替代缺乏维护的后者。
2. 为了区分程序运行环境，Flask提供了一个 FLASK_ENV 环境变量用来设置环境，默认为 production（生产）。在开发时，我们可以将其设为 development（开发），这会开启所有支持开发的特性。
3. `@cache.cached()` 和 `@cache.memoize()` 都可以缓存视图函数和不包含参数的非视图函数；如果非视图函数包含参数，则需要用 `@cache.memoize()`。 

### Flask-Cache 学习资料

Flask-Cache 学习资料 | 说明
--- | ---
官方文档 | http://www.pythondoc.com/flask-cache/index.html
Flask-Cache缓存使用小记 | https://heshangbuxitou.github.io/2017/11/21/flask-cache/
Flask-Caching | https://flask-caching.readthedocs.io/en/latest/
13.2 使用Flask-Caching设置缓存（《Flask Web开发实战：入门、进阶与原理解析》） | https://weread.qq.com/web/reader/26132b70715ec2fd26119eek1f032c402131f0e3dad99f3