from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
### 需要你做更改的部分
cookie = "请随机输入一个cookie"
passwd = "请填入你的密码"

# 使用MD5算法对密码进行加密处理
def encrypt_password(password):
    hash_md5 = hashlib.md5()
    hash_md5.update(password.encode('utf-8'))
    return hash_md5.hexdigest()


def check_cookies(request):
    try:
        task_cookies = request.cookies.get('my_cookie')
        return task_cookies == cookie
    except:
        return False

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST','GET'])
def index():  # put application's code here
    if request.method == 'POST':
        if check_cookies(request):
            task_content = request.form['content']
            new_task = Todo(content = task_content, date_created=datetime.now())

            try:
                db.session.add(new_task)
                db.session.commit()
                return  redirect('/')
            except:
                return 'There was an issue adding your task!'
        else :
                return redirect('/error_404/')
    else:
        if check_cookies(request):
            tasks = Todo.query.order_by(Todo.date_created).all()
            return render_template('index.html', tasks=tasks)
        else:
            return render_template('authorize.html')


@app.route('/delete/<int:id>')
def delete(id):
    if check_cookies(request):
        task_to_delete = Todo.query.get_or_404(id)

        try:
            db.session.delete(task_to_delete)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem deleting that task'
    else:
         return redirect('/error_404/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    if check_cookies(request):
        task = Todo.query.get_or_404(id)

        if request.method == 'POST':
            task.content = request.form['content']

            try:
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an issue updating your task'
        else:
            return render_template('update.html', task=task)
    else:
         return redirect('/error_404/')


@app.route('/authorize/', methods=['POST'])
def authorize():  # put application's code here

    if request.method == 'POST':   
        user_password = request.form['content']
        
        encrypted_password = encrypt_password(passwd)

        if encrypted_password == user_password:
            response = {"status":True, "cookie": cookie}
        else:
            response = {"status":False, "cookie": ""}
        my_json = json.dumps(response)
        return my_json
        
@app.route('/error_404/',methods=['GET'])
def error_404():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
