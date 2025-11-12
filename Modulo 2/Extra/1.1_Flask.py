# Crie um app flask que exibe ola  mundo na rota principal

from flask import Flask

app = Flask(__name__) # Representa o nome do arquivo o codigo deve ser escrito entre o app e o app.run

@app.route('/') #Decorador de função
def home():
    return 'Olá mundo!'

if __name__  == '__main__':
    app.run(debug=True)