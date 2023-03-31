from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
#根据自己的情况修改这两行的参数
cookie = "" # 可以是任意的一个数字或字符串
passwd = "" #自己定义

def check_cookies(request):
    try:
        task_cookies = request.cookies['my_cookie']
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
        if user_password == passwd:
            return "{\"status\":true,\"cookie\":\cookie\"}"
        else:
            return "{\"status\":false,\"cookie\":\"\"}"
        
@app.route('/error_404/',methods=['GET'])
def error_404():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
