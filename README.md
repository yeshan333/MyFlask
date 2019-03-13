# About

## 原型设计工具[https://www.mockplus.cn/](https://www.mockplus.cn/)、[https://www.axure.com/](https://www.axure.com/)


## Flask-DebugToolBar调试

    pipenv install flask-debugtoolbar


```python
from flask import Flask
from flask_debugtoolbar import DebugToolarExtension

app = Flask(__name__)

toolbar = DebugToolbarExtension(app)

# 关闭对重定向的拦截,在settings.py中设置
DEBUG_TB_INTERCEPT_REDIRECTS = False

```

![AFfvM4.png](https://s2.ax1x.com/2019/03/13/AFfvM4.png)
