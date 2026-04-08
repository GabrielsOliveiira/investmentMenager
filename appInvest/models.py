from appInvest import db
from datetime import datetime, timezone

class Investor(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    saldo = db.Column(db.Float, default=0.0)

created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))