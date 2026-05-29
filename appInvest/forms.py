from flask_wtf  import FlaskForm
from wtforms import StringField, DateField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email
from flask_login import current_user

from appInvest import db
from appInvest.models import Investor, Imobiliario

class InvestorForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        investor = Investor(
            name = self.name.data,
            email = self.email.data,
        )

        db.session.add(investor)
        db.session.commit()


class ImobiliarioForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    invested_value = FloatField('Valor Investido', validators=[DataRequired()])
    dividend_received = FloatField('Dividendos Recebidos', default=0)
    current_value = FloatField('Valor Atual', validators=[DataRequired()])
    quantidades_cotas = FloatField('Quantidade de Cotas', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        investimento = Imobiliario(
            name=self.name.data,
            invested_value=self.invested_value.data,
            dividend_received=self.dividend_received.data,
            current_value=self.current_value.data,
            quantidades_cotas=self.quantidades_cotas.data,
            investors_id=current_user.id
        )

        db.session.add(investimento)
        db.session.commit()