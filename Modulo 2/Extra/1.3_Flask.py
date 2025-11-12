from flask import Flask

app = Flask (__name__) # representa o nome do arquivo
# o codigo deve ser escrito entre o app e o app.run

@app.route('/') # @decorador de função
def home():
    return 'Olá Mundo!'

@app.route('/sobre') 
def sobre():
    return "Olá, meu nome é Abed eu sou um desenvolvedor de Python."

@app.route('/saudacao/<nome>') # para abrir a página precisamos adicionar o nome
def saudacao(nome):
    return f'Olá {nome}! Seja bem vindo'

if __name__ == '__main__':
    app.run(debug=True)