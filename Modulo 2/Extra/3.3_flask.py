# Exercicío  3.3: Condicionais em templates
# Crie uma rota que envie uma idade e, no template use if para mostrar uma mensagem.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/sobre')
def sobre():
    return 'Olá eu sou um aluno do curso de python'

@app.route('/idade/<int:idade>') # Terceira pagina
def idade(idade):
    return render_template('ex_3-3.html', idade=idade)

if __name__ == '__main__':
    app.run(debug=True)

