# 数据库模型

from datetiem imort datetime
form sayhello import db

# 存储留言的模型
class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True) # 留言时间戳




