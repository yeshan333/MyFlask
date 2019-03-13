# 配置文件

import os
from sayhello import app

# os.path.dirname(os.root_path)获取上层目录所在的路径
dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

DEBUG_TB_INTERCEPT_REDIRECTS = False
SECRET_KEY = os.getenv("SECRET_KEY", "secret string")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)



""" import os
import sys

from sayhello import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db) """

