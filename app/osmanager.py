from flask import Flask, render_template, url_for
app = Flask(__name__)

os = {"numero": "xxxxx",
    "cliente": "Daniel Gomes Molina",
    "equipamento": "Balança Filizola",
    "status": "Em manutenção"
}

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", os=os)

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)