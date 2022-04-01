from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

@myapp_obj.route("/")

def home():
  name = {'username':'Lisa'}
  city_names = ['Paris','London','Rome','Tahiti']
  
  return render_template('home.html', name=name, cities=city_names)

class LoginForm(FlaskForm):
    city_string = StringField('City Name', validators=[DataRequired()])
