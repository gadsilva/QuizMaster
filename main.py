from flask import Flask, render_template

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define uma rota para a página inicial
@app.route('/')
def index():
    # Renderiza o template index.html
    return render_template('index.html')

# Verifica se o arquivo main.py está sendo executado diretamente e, se sim, inicia o servidor Flask
if __name__ == "__main__":
    # Ativa o modo de depuração para facilitar o desenvolvimento
    app.run(debug=True)
