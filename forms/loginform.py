from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    capitan_id = StringField('id капитана', validators=[DataRequired()])
    capitan_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')
