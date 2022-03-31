from flask import Flask, redirect, render_template, request, url_for
from dataOperations import CatchData, CreateData, CatchDataByID

# Flask
app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == 'POST':
        id_category = request.form["ID_CATEGORY"]
        return redirect(url_for("view_category", id = id_category))
    return render_template("index.html")

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

@app.route("/view_category/<int:id>", methods = ['POST', 'GET'])
def view_category(id):
    if request.method == 'POST':
        id_category = request.form['ID_CATEGORY']
        return redirect(url_for("view_category", id = id_category))

    else:
        if id == 999999: # arrumar essa condição feia do código
            return render_template("view_category.html", info = CatchData("category"), conditon = False)
        elif id != 0:
            return render_template("view_category.html", info = CatchDataByID("category", id), conditon = False)
        else:
            return render_template("view_category.html", info = CatchDataByID("category", id), conditon = True)

@app.route("/view_product/<int:id>", methods=["POST", "GET"])
def view_product(id):
    if request.method == 'POST':
        id_product = request.form['ID_PRODUCT']
        return redirect(url_for("view_product", id = id_product))
        
    else:
        if id == 999999: # arrumar essa condição feia do código
            return render_template("view_product.html", info = CatchData("products"), conditon = False)
        elif id != 0:
            return render_template("view_product.html", info = CatchDataByID("products", id), conditon = False)
        else:
            return render_template("view_product.html", info = CatchDataByID("products", id), conditon = True)