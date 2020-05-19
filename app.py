from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from src.Translator import Translator
from src.TehManager import TehManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

translatorIndoToSunda = Translator("Indonesia To Sunda", "indonesia")
translatorSundaToIndo = Translator("Sunda To Indonesia", "sunda")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sunda/', methods=['POST', 'GET'])
def sundaToIndonesia():
    translated = ""
    if(request.method == 'POST'):
        try:
            method = request.form.get('algoritma')
            translatorSundaToIndo.setMethod(method)
            text = request.form['text']
            text = TehManager.deleteUselessWord(text)
            translated = translatorSundaToIndo.getTranslation(text)
        except:
            translated = ""
    return render_template('translate.html', translator = translatorSundaToIndo, translatedSentence = translated)

@app.route('/indonesia/', methods=['POST', 'GET'])
def indonesiaToSunda():
    translated = ""
    if(request.method == 'POST'):
        try:
            method = request.form.get('algoritma')
            translatorIndoToSunda.setMethod(method)
            text = request.form['text']
            translated = translatorIndoToSunda.getTranslation(text)
            useTeh = request.form.get('useTeh')
            if(useTeh != None):
                translated = TehManager.useTeh(translated)
        except:
            translated = ""
    return render_template('translate.html', translator = translatorIndoToSunda, translatedSentence = translated)

if __name__ == "__main__":
    app.run(debug=True)

