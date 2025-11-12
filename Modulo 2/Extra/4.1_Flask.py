from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])# Primeira página
def index():
    if request.method == 'POST':
        nome= request.form['nome']
        return f'Olá {nome}! seja bem vindo a fábrica de programadores!'
    return render_template('ex_4-1.html')
    
if __name__ == '__main__':
    app.run(debug=True)