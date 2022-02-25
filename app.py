from flask import Flask, render_template
from dataOperations import CatchData

# Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", products = CatchData("crud_produtos.db", "products"), categorys = CatchData("crud_produtos.db", "category"))