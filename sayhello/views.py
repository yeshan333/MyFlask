# 视图函数所在的文件

from flask import flash, redirect, render_template, url_for

from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HelloForm

@app.route('/',methods=['GET', 'POST'])
def index():
    # 根据timestamp字段降序罗列留言
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name) # 实例化模型类，创建记录
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world ! ')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
