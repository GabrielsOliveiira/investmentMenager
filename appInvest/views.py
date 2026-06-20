from appInvest import app, db
from flask import render_template, url_for, request, redirect
from flask_login import current_user, login_required, login_user, logout_user

from appInvest.stringMenager import toFloat
from appInvest.forms import InvestorForm, ImobiliarioForm, Renda_fixaForm, AcaoForm
from appInvest.models import Investor, Imobiliario, RendaFixa, Acao
from werkzeug.datastructures import MultiDict

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/cadastrar/", methods=['GET', 'POST'])
def invertorForm():
    emailUsado = False
    form = InvestorForm()
    if form.validate_on_submit():
        novo_usuario = form.save()
        if novo_usuario != "Email já cadastrado":
            login_user(novo_usuario)
            return redirect(url_for("perfil"))
        
        emailUsado = True

    context = {
        "emailUsado": emailUsado
    }

    return render_template('investorForm.html', form=form, context=context)

@app.route("/login/")
def login():
    email = request.args.get("email")
    senha = request.args.get("password")
    investidor = Investor.query.filter_by(email=email, senha=senha).first()

    if investidor:
        login_user(investidor)
        return redirect(url_for("perfil"))
    
    return render_template('login.html', naoEncontrado=email)

# Tipo de investimentos

@app.route("/investimento_imobiliario/", methods=['GET', 'POST'])
@login_required
def addImobiliario():
    if request.method == "POST":
        data = MultiDict(request.form)
        data["invested_value"] = str(toFloat(data.get("invested_value", "")))
        form = ImobiliarioForm(data)
    else:
        form = ImobiliarioForm()
        
    if form.validate_on_submit():
        form.save()
        return redirect(url_for("perfil"))
    return render_template('imobiliarioForm.html', form=form)

@app.route("/investimento_renda_fixa", methods=['GET', 'POST'])
@login_required
def addRenda_fixa():
    form = Renda_fixaForm()

    if form.validate_on_submit():
        form.save()
        return redirect(url_for("perfil"))


    return render_template('renda_fixaForm.html', form=form)    

@app.route("/investimento_acao/", methods=['POST', 'GET'])
@login_required
def addAcao():
    form = AcaoForm()

    if form.validate_on_submit():
        form.save()
        return redirect(url_for("perfil"))
    
    return render_template('acaoForm.html', form=form)

@app.route("/perfil/escolher_investimento")
@login_required
def escolher_investimento():
    return render_template("escolher_investimento.html")

# Perfil

@app.route("/perfil/", methods=['GET', 'POST'])
@login_required
def perfil():
    resultado = None
    resultado_lucro = None
    investimento_id = None
    valor_cota = None
    tipo = False

    if request.method=='POST':
        acao, tipo = request.form.get("acao").split("-")
        investimento_id = request.form.get("investimento_id")

        investimento = Imobiliario.query.get(investimento_id)

        if acao == "previsao":
            previsaoCota = toFloat(request.form.get("previsaoCota"))
            resultado = round( previsaoCota * investimento.quantidades_cotas, 2)

        elif acao == "lucro":
            valor_cota = toFloat(request.form.get("lucro"))
            resultado_lucro= round((valor_cota * investimento.quantidades_cotas) - investimento.invested_value, 2)

    context = {
        "investidor": current_user,
        "carteira": current_user.carteira,
        "resultado": resultado,
        "investimento_calculado_id": investimento_id,
        "resultado_lucro": resultado_lucro,
        "valor_cota": valor_cota,
        "tipo": tipo
    }

    return render_template('perfil.html', context=context)

# Funções

@app.route("/perfil/adicionar_cota/<int:id>", methods=['GET', 'POST'])
@login_required
def addCota(id):
    investment = Imobiliario.query.get_or_404(id)

    if investment.carteira_id != current_user.carteira.id:
        return "Não autorizado", 403

    if request.method == "POST":
        valor = request.form.get("invested_value")
        cotas = request.form.get("quantidades_cotas")

        if valor:
            investment.invested_value += float(valor)
        if cotas:
            investment.quantidades_cotas += int(cotas)

        db.session.commit()

        return redirect(url_for("perfil"))

    return render_template('adicionarCota.html')

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/deleteInvestment/<int:id>/<string:type>")
@login_required
def deleteInvestment(id, type):

    investment = False

    if type == 'imobiliario':
        investment = Imobiliario.query.get_or_404(id)

    if type == 'renda_fixa':
        investment = RendaFixa.query.get_or_404(id)

    if type == 'acao':
        investment = Acao.query.get_or_404(id)

    if not investment:
        return "Não autorizado", 403

    db.session.delete(investment)
    db.session.commit()

    return redirect(url_for("perfil"))

@app.route("/atulizar nome/", methods=['GET', 'POST'])
@login_required
def updateName():
    novo_nome = request.form.get("novo_nome")
    current_user.nome = novo_nome
    db.session.commit()
    return redirect(url_for("perfil"))