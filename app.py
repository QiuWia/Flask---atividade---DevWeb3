
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret_key"  # pra mensagens flash

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Validaçaõ
        if password != confirm_password:
            flash("Senhas não combinam", "danger")
        elif not any(char.isupper() for char in password):
            flash("Senha precisa ter pelo menos uma letra maiuscula!", "danger")
        elif not any(char.isdigit() for char in password):
            flash("senha precisa ter pelo menos um número!", "danger")
        elif not any(char in "!@#$%^&*()-_+=<>?/|\{}[]:;" for char in password):
            flash("Senha precisa conter um caractere especial!", "danger")
        else:
            flash("cadastrado com sucesso!", "success")
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def sobre():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
