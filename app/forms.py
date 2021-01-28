# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired


class StringForm(FlaskForm):
    pin = StringField('Ключевое слово:', validators=[DataRequired()])
    domen = StringField('Сайт:', validators=[DataRequired()])
    pass_length = DecimalField('Длина пароля:', validators=[DataRequired()])
    submit = SubmitField('Получить пароль')
