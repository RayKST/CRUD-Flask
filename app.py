from flask import Flask, redirect, render_template, request, url_for
from dataOperations import CatchData, CreateData

# Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", products = CatchData("products"), categorys = CatchData("category"))

@app.route("/create_products", methods=['POST','GET'])
def create_products():
    if request.method == 'POST':
        name = request.form['NAME'] 
        price = request.form['PRICE']
        description = request.form['DESCRIPTION']
        category_id = request.form['CATEGORY_ID']
        product_infos = [(name, price, description, category_id)]
        CreateData("products", product_infos)
        return redirect(url_for("index")) 
        #Depois de realizar as operações na db fazer o redirect para o index

    else:
        return render_template("create_products.html")

@app.route("/create_categorys", methods=['POST','GET'])
def create_categorys():
    if request.method == 'POST':
        name = request.form['NAME'] 
        description = request.form['DESCRIPTION']
        category_infos = [(name, description)]
        CreateData("category", category_infos)
        return redirect(url_for("index")) 
        #Depois de realizar as operações na db fazer o redirect para o index
        
    else:
        return render_template("create_categorys.html")