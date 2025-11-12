from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello flask'

@app.route('/sobre')
def sobre():
    return "Olá, meu nome é Abed e sou uma desenvolvedor Python."



@app.route('/lista')
def lista():
    alunos = ['Abed', 'Renan', 'Raphael', 'Felipe']
    return render_template('ex_3-2.html',lista=alunos)

if __name__ == '__main__': 
    app.run(debug=True)