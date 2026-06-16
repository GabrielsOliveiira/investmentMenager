from flask_wtf  import FlaskForm
from wtforms.fields import StringField, DateField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email
from flask_login import current_user

from appInvest import db
from appInvest.models import Investor, Imobiliario, RendaFixa, Carteira, Acao

class InvestorForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    btnSubmit = SubmitField('Enviar')

    def save(self):

        existInvestor = Investor.query.filter_by(email=self.email.data).first()

        if existInvestor:
            return "Email já cadastrado"


        investor = Investor(
            name = self.name.data,
            email = self.email.data,
        )

        db.session.add(investor)
        db.session.commit()

        nova_carteira = Carteira(investor_id=investor.id)

        db.session.add(nova_carteira)
        db.session.commit()

class ImobiliarioForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    invested_value = FloatField('Valor Investido', validators=[DataRequired()])
    quantidades_cotas = FloatField('Quantidade de Cotas', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        imobiliario = Imobiliario(
            name = self.name.data,
            invested_value = self.invested_value.data,
            quantidades_cotas = self.quantidades_cotas.data,
            carteira_id = current_user.carteira.id
        )

        db.session.add(imobiliario)
        db.session.commit()

class Renda_fixaForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    invested_value = FloatField('Valor investido', validators=[DataRequired()])
    interest_rate = FloatField('Taxa', validators=[DataRequired()])
    maturity_date = DateField('Data de vencimento', format='%Y-%m-%d', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        renda_fixa = RendaFixa(
            name = self.name.data,
            invested_value = self.invested_value.data,
            interest_rate = self.interest_rate.data,
            maturity_date = self.maturity_date.data,
            carteira_id = current_user.carteira.id
        )

        db.session.add(renda_fixa)
        db.session.commit()

class Acao(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    name = StringField('Nome', validators=[DataRequired()])
    invested_value = FloatField('Valor investido', validators=[DataRequired()])
    quantity = IntegerField('Quantidade', validators=[DataRequired()])

    def save(self):
        acao = Acao(
            ticker = self.ticker.data,
            name = self.name.data,
            invested_value = self.invested_value.data,
            quantity = self.quantity.data,
            Carteira_id = current_user.carteira.id
        )

        db.session.add(acao)
        db.session.commit()