from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from src.Translator import Translator
from src.TehManager import TehManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sunda/', methods=['POST', 'GET'])
def sundaToIndonesia():
    translated = ""
    translator = Translator("Sunda To Indonesia", "sunda")
    if(request.method == 'POST'):
        try:
            method = request.form.get('algoritma')
            translator.setMethod(method)
            text = request.form['text']
            text = TehManager.deleteUselessWord(text)
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

