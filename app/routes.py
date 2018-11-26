from flask import render_template, flash, redirect, url_for
from app import app
from app.form import SurveyForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        flash(f"Thanks {form.name.data}, your form has been submitted!")
        return redirect(url_for('index'))
    return render_template('survey.html', form=form)