from flask import Flask, render_template
from flask_fontawesome import FontAwesome
from service.marvel import herois

app = Flask(__name__)
fa = FontAwesome(app)


@app.route('/')
def index():
    lista_herois = herois()
    return render_template('index.html', lista_herois=lista_herois)


if __name__ == '__main__':
    app.run()
