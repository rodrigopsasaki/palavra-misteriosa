from flask import Flask
from flask import render_template
from flask import request
from functions import match, palavras_possiveis

app = Flask(__name__)

@app.route("/", methods=(['GET', 'POST']))
def palavra():
    if request.method == 'POST':
        letras = list()
        for i in range(1, 11):
            letras.append(request.form['letra' + str(i)].upper())
            
        palavras = palavras_possiveis(letras)
        return render_template('output.html', palavras=palavras)
    return render_template('palavra.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
