from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof='инженерные' if 'инженер' or 'строитель' in prof else 'научные')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
