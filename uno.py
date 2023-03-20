from flask import Flask,render_template,request
app = Flask(__name__)

import datetime

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/login')
def login():= request.args.get('nome')
    
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    return render_template('login.html',nome=nome,cognome=cognome)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)