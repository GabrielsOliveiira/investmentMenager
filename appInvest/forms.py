from flask_wtf  import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Email

from appInvest import db
from appInvest.models import Investor

class InvestorForm(FlaskForm):
    birth_date = DateField('date', format="%Y-%m-%d", validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    cpf = StringField('cpf', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        investor = Investor(
            name = self.name.data,
            email = self.email.data,
            cpf = self.cpf.data,
            birth_date = self.birth_date.data,
        )

        db.session.add(investor)
        db.session.commit()