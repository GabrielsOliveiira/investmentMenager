from appInvest import app, db
from flask import render_template, url_for, request, redirect
from flask_login import current_user, login_required, login_user, logout_user

from appInvest.forms import InvestorForm, ImobiliarioForm
from appInvest.models import Investor, Imobiliario

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

@app.route("/login/")
def login():
    email = request.args.get("email")
    investidor = Investor.query.filter_by(email=email).first()

    if investidor:
         login_user(investidor)
         return redirect(url_for("perfil"))
    
    return render_template('login.html', naoEncontrado=email)

@app.route("/cadastrar investimento/", methods=['GET', 'POST'])
@login_required
def investmentForm():
    form = ImobiliarioForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for("perfil"))
    return render_template('imobiliarioForm.html', form=form)

@app.route("/perfil/", methods=['GET', 'POST'])
@login_required
def perfil():
    investimento_id = request.form.get("investimento_id")
    previsaoCota = request.form.get("previsaoCota")

    resultado = None

    if investimento_id and previsaoCota:
        investimento = Imobiliario.query.get(investimento_id)

        previsaoCota = float(previsaoCota)

        resultado = round( previsaoCota * investimento.quantidades_cotas, 2)
        
    return render_template('perfil.html', investidor=current_user, resultado=resultado,  investimento_calculado_id=int(investimento_id))


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/deleteInvestment/<int:id>")
@login_required
def deleteInvestment(id):
    investment = Imobiliario.query.get_or_404(id)

    if investment.investors_id != current_user.id:
        return "Não autorizado", 403

    db.session.delete(investment)
    db.session.commit()

    return redirect(url_for("perfil"))