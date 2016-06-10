from flask import Flask
from flask import render_template
from flask import request

def match(p1, p2):
    if not p1:
        return True
    else:
        if p2:
            if p1[0] == p2[0] or p1[0] == u'':
                return match(p1[1:], p2[1:])
            else:
                return False

def palavras_possiveis(letras):
    print letras
    palavras  = open('palavras_10.txt').read().split('\n')
    print len(palavras)
    return (palavra for palavra in palavras if match(letras, palavra))

app = Flask(__name__)

@app.route("/", methods=(['GET', 'POST']))
def palavra():
    if request.method == 'POST':
        letras = list()
        palavras = list()
        for i in range(1, 11):
            letras.append(request.form['letra' + str(i)].upper())
        palavras = palavras_possiveis(letras)
        return render_template('output.html', palavras=palavras)
    return render_template('palavra.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
