from appInvest import app, db
from flask import render_template, url_for, request, redirect
from datetime import datetime

from appInvest.forms import InvestorForm
from appInvest.models import Investor

@app.route("/")
def homepage():
    usuario = "ca"
    idade = 16
    context = {
        "usuario": usuario,
        "idade": idade
    }
    return render_template('index.html', context=context)

@app.route("/login/", methods=['GET', 'POST'])
def invertorForm():
    form = InvestorForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for("homepage"))

    return render_template('investorForm.html', context=context, form=form)

# app.route("/loginOld/", methods=['GET', 'POST'])
# def loginOld():
#     context = {}
#     if request.method == "GET":
#         pesquisa = request.args.get('pesquisa')
#         context.update({'pesquisa': pesquisa})
#         print(context)

#     if request.method == "POST":
#         date = request.form['date']
#         name = request.form['name']
#         cpf = request.form['cpf']
#         email = request.form['email']

#         date = datetime.strptime(date, '%Y-%m-%d').date()

#         investor = Investor(
#             birth_date = date,
#             name = name,
#             cpf = cpf,
#             email = email
#         )
#         db.session.add(investor)
#         db.session.commit()

#     return render_template('investorFormOld.html', context=context)