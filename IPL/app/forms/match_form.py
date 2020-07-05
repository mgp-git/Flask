from flask_wtf import FlaskForm
from wtforms import TextField, DateTimeField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired

teams = [('RCB', 'RCB'),
     ('CSK', 'CSK'),
     ('KKR', 'KKR'),
     ('SRH', 'SRH'),
     ('MI', 'MI'),
     ('DD', 'DD'),
     ('RR', 'RR'),
     ('KXIP', 'KXIP')]

class MatchForm(FlaskForm):
    date = DateTimeField('Date',  format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    venue = TextField('Venue', validators=[DataRequired()])
    team_a = SelectField(u'Team_A', choices=teams)
    team_b = SelectField(u'Team_B', choices=teams)
    submit = SubmitField('Submit')

