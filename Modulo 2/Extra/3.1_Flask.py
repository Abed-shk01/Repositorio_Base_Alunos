# Exercicios: Templates com variaveis
# Modifique o template para receber o nome  como variavel e exibir "Bem vindo"


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello flask'

@app.route('/sobre')
def sobre():
    return "Olá, meu nome é Abed e sou uma desenvolvedor Python."

@app.route('/saudacao/<nome>') 
def saudacao(nome):
    return render_template('ex_3-1.html', nome=nome)

@app.route('/dobro/<int:numero>')
def dobro(numero):
    dobro = numero*2
    return f'O dobro de {numero} é {2*numero}.'

if __name__ == '__main__': 
    app.run(debug=True)