from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.Translator import Translator
from src.TehManager import TehManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    try:
        task_to_delete = Todo.query.get_or_404(id)
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = Todo.query.get_or_404(id)
    if(request.method == 'POST'):
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error updating that task"
    else:
        return render_template('update.html', task=task)

@app.route('/sunda/', methods=['POST', 'GET'])
def sundaToIndonesia():
    translated = ""
    translator = Translator("Sunda To Indonesia", "sunda")
    if(request.method == 'POST'):
        try:
            method = request.form.get('algoritma')
            translator.setMethod(method)
            text = request.form['text']
            text = TehManager.deleteTeh(text)
            translated = translator.getTranslation(text)
        except:
            translated = ""
    return render_template('translate.html', translator = translator, translatedSentence = translated)

@app.route('/indonesia/', methods=['POST', 'GET'])
def indonesiaToSunda():
    translated = ""
    translator = Translator("Indonesia To Sunda", "indonesia")
    if(request.method == 'POST'):
        try:
            method = request.form.get('algoritma')
            translator.setMethod(method)
            text = request.form['text']
            translated = translator.getTranslation(text)
            useTeh = request.form.get('useTeh')
            if(useTeh != None):
                translated = TehManager.useTeh(translated)
        except:
            translated = ""
    return render_template('translate.html', translator = translator, translatedSentence = translated)

if __name__ == "__main__":
    app.run(debug=True)

