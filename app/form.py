from flask_wtf import FlaskForm
from wtforms import StringField

class SurveyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    
    
