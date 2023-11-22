from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Solution Sprint - Fase 05"

if __name__ == '__main__':
    app.run()