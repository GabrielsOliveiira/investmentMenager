from appInvest import db
from datetime import datetime, timezone
from flask_login import UserMixin

class Investor(db.Model, UserMixin):
    __tablename__ = "investor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    investimentos = db.relationship("Imobiliario", backref="dono", lazy=True)

class Imobiliario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    invested_value = db.Column(db.Float, nullable=False)
    dividend_received = db.Column(db.Float, default=0)
    current_value = db.Column(db.Float, nullable=False)
    quantidades_cotas = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    investors_id = db.Column(db.Integer, db.ForeignKey("investor.id"), nullable=False)
