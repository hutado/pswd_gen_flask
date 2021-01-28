# -*- coding: utf-8 -*-

from flask import render_template, flash

from app import app
from app.forms import StringForm

from pswd import pswd


@app.route('/', methods=['GET', 'POST'])
def index():
    form = StringForm()
    if form.validate_on_submit():
        pswd.set_passwd(form.pin.data)
        pswd.set_url(form.domen.data)
        pswd.set_length(form.pass_length.data or 12)
        flash(pswd.decrypt())
    return render_template('index.html', form=form)
