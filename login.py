from flask import Flask,render_template,request
app = Flask(__name__)

import datetime

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/login')
def login():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    return render_template('login.html',nome=nome,cognome=cognome)

@app.route('/login2')
def login2():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    if nome == "admin" and cognome == "xxx123##":
        return render_template('form.html')
    else:
        return render_template('loginerrato.html')


   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)