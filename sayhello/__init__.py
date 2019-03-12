# 构造文件,包含程序实例

from flask import Flask
from sqlalchemy import SQLAlchemy

# 环境变量：FLASK_APP=sayhello
app = Flask('sayhello') # 使用包组织代码的时候，最好采用硬解码的形式给出包的名称作为程序名称

app.config.from_pyfile('settings.py') # 从配置文件加载配置
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

from sayhello import views, errors, commands

