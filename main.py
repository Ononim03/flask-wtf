from flask import Flask, render_template, url_for

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


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    answers_dict = {'title': 'Анкета на Марс',
                    'surname': 'Зинатуллин',
                    'name': 'Тимур',
                    'education': 'Школьное неполное',
                    'profession': 'Школьник',
                    'sex': 'male',
                    'motivation': '110 score',
                    'ready': True,
                    'css_file': url_for('static', filename='css/style.css')}
    return render_template('auto_answer.html', title=answers_dict['title'],
                           surname=answers_dict['surname'],
                           name=answers_dict['name'],
                           education=answers_dict['education'],
                           profession=answers_dict['profession'],
                           sex=answers_dict['sex'],
                           motivation=answers_dict['motivation'],
                           ready=answers_dict['ready'],
                           css_file=answers_dict['css_file'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
