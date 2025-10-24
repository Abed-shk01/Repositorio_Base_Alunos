from flask import Flask, render_template

app = Flask(__name__)
# Cria rota para a pagina inicial "do site"
@app.route('/')
def inedx():
    return render_template('index.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

# Executar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)