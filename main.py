from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
               'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
               'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман',
               'пилот дронов']


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    profession = 'и' if 'инженер' in prof or 'строитель' in prof else 'н'
    return render_template('training.html', prof=profession)


@app.route('/list_prof/<type>')
def list_prof(type):
    return render_template('list.html', type=type, list=professions)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
