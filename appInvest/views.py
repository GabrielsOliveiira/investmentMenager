from appInvest import app, db
from flask import render_template, url_for, request, redirect
from flask_login import current_user, login_required, login_user, logout_user

from appInvest.forms import InvestorForm, ImobiliarioForm
from appInvest.models import Investor

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/cadastrar/", methods=['GET', 'POST'])
def invertorForm():
    form = InvestorForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for("homepage"))

    return render_template('investorForm.html', form=form)

@app.route("/login/", methods=['GET', 'POST'])
def login():
    email = request.args.get("email")
    investidor = Investor.query.filter_by(email=email).first()

    if investidor:
         login_user(investidor)
         return redirect(url_for("perfil"))
    
    return render_template('login.html')

@app.route("/cadastrar investimento/", methods=['GET', 'POST'])
@login_required
def investmentForm():
    form = ImobiliarioForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for("perfil"))
    return render_template('imobiliarioForm.html', form=form)

@app.route("/perfil/")
@login_required
def perfil():   
    return render_template('perfil.html', investidor=current_user)


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))