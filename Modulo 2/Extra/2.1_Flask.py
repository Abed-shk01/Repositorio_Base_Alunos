# MOdificar a rota principal de html ucom titulo
# Paragrafo e um link para outra rota 
# Usar render_template para renderizar o arquivo.html
# usar o url_for() nas ancoras tags do script html


from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/') # @decorador de função
def home():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return "Fabrica de programadores."

@app.route('/zezinho') # para abrir a página precisamos adicionar o nome 
def zezinho():
    return 'achou a rota'



if __name__ == '__main__': 
    app.run(debug=True)