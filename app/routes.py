from flask import render_template
from app import app
from app.form import SurveyForm

@app.route('/')
@app.route('/index')
def index():
    form = SurveyForm()
    return render_template('survey.html', form=form)