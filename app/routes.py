from app import app, db
from app.forms import ProductForm, CategoryForm
from app.models import Product, Category
from flask import render_template, redirect, url_for

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_products", methods=['POST','GET'])
def create_products():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name = form.name.data, 
            description = form.description.data, 
            price = form.price.data, 
            category_id = form.category_id.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_products.html', title='Create Product', form=form)


@app.route("/create_categorys", methods=['POST','GET'])
def create_categorys():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(
            name = form.name.data, 
            description = form.description.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_categorys.html', title='Create Category', form=form)


@app.route("/view_product/")
def view_product():
    products = Product.query.all()
    return render_template("view_product.html", title = 'View Products', products = products)

'''
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



@app.route("/update_product/<int:id>", methods=["POST", "GET"])
def update_product(id):
    if request.method == 'POST':
        if id == 0:
            id_product = request.form['ID_PRODUCT']
            return redirect(url_for("update_product", id = id_product))
        else:
            name = request.form['NAME'] 
            price = request.form['PRICE']
            description = request.form['DESCRIPTION']
            category_id = request.form['CATEGORY_ID']
            product_info = [(name, price, description, category_id)]
            UpdateData('products', product_info, id)
            return redirect(url_for("index")) 
            #Depois de realizar as operações na db fazer o redirect para o index

    else:
        if id == 0:
            return render_template("update_product.html", info = CatchDataByID("products", id), conditon = True)
        else:
            return render_template("update_product.html", info = CatchDataByID("products", id), conditon = False)


@app.route("/update_category/<int:id>", methods=["POST", "GET"])
def update_category(id):
    if request.method == 'POST':
        if id == 0:
            id_category = request.form['ID_CATEGORY']
            return redirect(url_for("update_category", id = id_category))
        else:
            name = request.form['NAME'] 
            description = request.form['DESCRIPTION']
            category_info = [(name, description)]
            UpdateData('category', category_info, id)
            return redirect(url_for("index")) 
            #Depois de realizar as operações na db fazer o redirect para o index
            
    else:
        if id == 0:
            return render_template("update_category.html", info = CatchDataByID("category", id), conditon = True)
        else:
            return render_template("update_category.html", info = CatchDataByID("category", id), conditon = False)

@app.route("/delete_product/<int:id>", methods=["POST", "GET"])
def delete_product(id):
    if request.method == 'POST':
        id_product = request.form['ID_PRODUCT']
        DeleteData("products", id_product)
        return redirect(url_for("delete_product", id = id_product))
    else:
        if id == 0:
            return render_template("delete_product.html", conditon = True)
        else:
            return render_template("delete_product.html", productID = id, conditon = False)

@app.route("/delete_category/<int:id>", methods=["POST", "GET"])
def delete_category(id):
    if request.method == 'POST':
        id_category = request.form['ID_CATEGORY']
        DeleteData("category", id_category)
        return redirect(url_for("delete_category", id = id_category))
    else:
        if id == 0:
            return render_template("delete_category.html", conditon = True)
        else:
            return render_template("delete_category.html", categoryID = id, conditon = False)
'''