from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class SurveyForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    submit = SubmitField('Submit')

    
