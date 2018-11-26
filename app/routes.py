from flask import render_template, flash, redirect
from app import app
from app.form import SurveyForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        flash(f"Thanks {form.name}, your form has been submitted!")
        return redirect('/index')
    return render_template('survey.html', form=form)