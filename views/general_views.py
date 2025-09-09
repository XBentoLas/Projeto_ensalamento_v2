from flask import Blueprint, render_template

# Criamos um novo Blueprint para as páginas gerais, como a homepage
general_bp = Blueprint('general', __name__)

@general_bp.route("/")
def homepage():
    # Supondo que você tenha um homepage.html em sua pasta 'templates'
    return render_template("homepage.html")
