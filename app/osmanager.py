from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, ClientForm
app = Flask(__name__)

app.config ['SECRET_KEY'] = '732c3eeec9fb75e61d6edc6458d2faad'

os = {"numero": "xxxxx",
    "cliente": "Daniel Gomes Molina",
    "equipamento": "Balança Filizola",
    "status": "Em manutenção"
}

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", os=os)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Conta Criada para {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)

@app.route('/client', methods=['GET', 'POST'])
def client():
    form = ClientForm()
    return render_template("client.html", title='Novo Cliente', form=form)

if __name__ == "__main__":
    app.run(debug=True)