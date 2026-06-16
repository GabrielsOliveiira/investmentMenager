from appInvest import db
from datetime import datetime, timezone
from flask_login import UserMixin

class Investor(db.Model, UserMixin):
    __tablename__ = "investor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    carteira = db.relationship("Carteira", back_populates="investor", uselist=False)

class Carteira(db.Model):
    __tablename__ = "carteira"

    id = db.Column(db.Integer, primary_key=True)
    investor_id = db.Column(db.Integer, db.ForeignKey("investor.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    investor = db.relationship("Investor", back_populates="carteira")
    imobiliario = db.relationship("Imobiliario", back_populates="carteira", lazy=True)
    renda_fixa = db.relationship("RendaFixa", back_populates="carteira", lazy=True)
    acao = db.relationship("Acao", back_populates="carteira", lazy=True)

class Imobiliario(db.Model):
    __tablename__ = "imobiliario"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    invested_value = db.Column(db.Float, nullable=False)
    quantidades_cotas = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    carteira_id = db.Column(db.Integer, db.ForeignKey("carteira.id"), nullable=False)
    carteira = db.relationship("Carteira", back_populates="imobiliario")

class RendaFixa(db.Model):
    __tablename__ = "renda_fixa"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    invested_value = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    maturity_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    carteira_id = db.Column(db.Integer, db.ForeignKey("carteira.id"), nullable=False)
    carteira = db.relationship("Carteira", back_populates="renda_fixa")

class Acao(db.Model):
    __tablename__ = "acao"

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    invested_value = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    carteira_id = db.Column(db.Integer, db.ForeignKey("carteira.id"), nullable=False)
    carteira = db.relationship("Carteira", back_populates="acao")


# class FundoInvestimento(db.Model):

#     __tablename__ = "fundo_investimento"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     invested_value = db.Column(db.Float, nullable=False)
#     quantity = db.Column(db.Float, nullable=False)
#     created_at = db.Column( db.DateTime, default=lambda: datetime.now(timezone.utc))

#     investors_id = db.Column(db.Integer, db.ForeignKey("carteira.id"), nullable=False)

# # class Criptomoeda(db.Model):
    # __tablename__ = "criptomoeda"

    # id = db.Column(db.Integer, primary_key=True)
    # symbol = db.Column(db.String(20), nullable=False)
    # name = db.Column(db.String(100), nullable=False)
    # invested_value = db.Column(db.Float, nullable=False)
    # quantity = db.Column(db.Float, nullable=False)
    # created_at = db.Column(
    #     db.DateTime,
    #     default=lambda: datetime.now(timezone.utc)
    # )

    # investors_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey("carteira.id"),
    #     nullable=False
    # )