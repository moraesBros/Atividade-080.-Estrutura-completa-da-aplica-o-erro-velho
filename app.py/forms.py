from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email

class NameForm(FlaskForm):
    name = StringField('Informe o seu nome', validators=[DataRequired()])
    surname = StringField('Informe o seu sobrenome:', validators=[DataRequired()])
    institution = StringField('Informe a sua Instituição de ensino:', validators=[DataRequired()])
    prontuario = StringField('Informe o seu prontuário:', validators=[DataRequired()])
    email = StringField('Informe seu e-mail institucional:', validators=[DataRequired(), Email()])
    discipline = SelectField(u'Informe a sua disciplina:', 
                           choices=[('dswa5', 'DSWA5'), ('dwba4', 'DWBA4'), ('GPSA5', 'Gestão de projetos')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Informe o seu usuário', validators=[DataRequired()])
    password = PasswordField('Informe a sua senha:', validators=[DataRequired()])
    submit = SubmitField('Enviar')
