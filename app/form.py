from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField, IntegerField, RadioField, SelectField, SelectMultipleField
    )
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import DataRequired

class SurveyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    age = IntegerField('Age')
    gender = RadioField('Gender', choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('neutral', 'Neutral'),
        ('undisclosed', 'No preference'),
    ])
    path = SelectField(
        'Which web development path do you identify yourself with?',
        choices=[
            ('front', 'Front End'),
            ('back', 'Back End'),
            ('full','Full Stack'),
        ])
    language = SelectMultipleField(
        'What programming languages do you use?',
        choices = [
        ('js', 'JavaScript'),
        ('ts', 'TypeScript'),
        ('py', 'Python'),
        ('csharp', 'C#'),
        ('java', 'Java'),
        ('other', 'Other'),
        ],
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False))
    submit = SubmitField('Submit')