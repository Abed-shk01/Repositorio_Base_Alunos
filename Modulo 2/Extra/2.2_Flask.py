# Links entre rotas 
# Adicioneum menu de navegação simples com links 

from flask import Flask, render_template

app = Flask(__name__) # representa o nome do arquivo


@app.route('/')
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return "Olá, meu nome é Alexsandra e sou uma desenvolvedora Python."

@app.route('/saudacao/<nome>') 
def saudacao(nome):
    return f'Olá {nome}! Tudo bem?'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    dobro = numero*2
    return f'O dobro de {numero} é {2*numero}.'

if __name__ == '__main__': 
    app.run(debug=True)