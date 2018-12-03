from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Voter, Answer
from app.form import SurveyForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    if form.validate_on_submit():

        voter = Voter(name=form.name.data, email=form.email.data)
        db.session.add(voter)
        db.session.commit()

        answers = Answer(
            age=form.age.data,
            gender=form.gender.data,
            path=form.path.data,
            language=form.path.data,
            comment=form.text_area.data,
            voter=voter
            )
        db.session.add(answers)
        db.session.commit()

        flash(f"Thanks, the survey has been submitted!")
        return redirect(url_for('index'))
    return render_template('survey.html', form=form)
