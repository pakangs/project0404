from flask import Flask, Blueprint, render_template, url_for, redirect, request, g, flash
from pybo.models import Shop, Product
from werkzeug.utils import redirect
from datetime import datetime
from pybo import db
from pybo.forms import ShopForm, ProductForm
from pybo.views.auth_views import required_login

bp = Blueprint("product", __name__, url_prefix="/product")

@bp.route("/insert/<int:shop_id>", methods=("GET", "POST"))
def insert(shop_id):
    shop = Shop.query.get_or_404(shop_id)

    form = ProductForm()

    if request.method == "POST":
        if form.validate_on_submit():
            
            name = form.name.data
            cost = form.cost.data
            info = request.form["info"]
            user_id = form.user_id.data

            product = Product(user_id=user_id, name=name, cost=cost, info=info, manufacturing_date=datetime.now(), expiration_date=datetime.now())
            shop.product_set.append(product)
            db.session.add(product)
            db.session.add(shop)
            db.session.commit()
            return redirect(url_for('shop.detail', shop_id=shop.id))
        
        else:
            print("###"*20)
            return render_template('/shop/shop_list.html', shop_id=shop_id, form=form)
    
    return render_template("product/product_form.html", shop_id=shop_id, form=form)
    


@bp.route("/detail/<int:shop_id>/<int:product_id>")
def detail(product_id, shop_id):
    form = ProductForm()
    product = Product.query.get(product_id)

    return render_template("product/product_detail.html", shop_id=shop_id, product=product, form=form)



@bp.route("/update/<int:shop_id>/<int:product_id>", methods=("GET", "POST"))
def update(product_id, shop_id):
    product = Product.query.get(product_id)

    if g.user != product.user:
        flash("수정권한이 없습니다.")
        return render_template('product/product_update.html', shop_id=shop_id, product_id=product_id, form=form)

    if request.method == "GET":
        print("%"*20)
        form = ProductForm(obj=product)

    else:
        form = ProductForm()
        print(form.user_id)
        if form.validate_on_submit():
            form.populate_obj(product)

            name = form.name.data
            cost = form.cost.data
            info = request.form["info"]

            product.name = name
            product.cost = cost
            product.info = info

            db.session.commit()

            print(form.user_id)
            print("$"*20)

            return redirect(url_for("product.detail", shop_id=shop_id, product_id=product.id))
            # return redirect(url_for('product.detail', product_id=product_id))
    return render_template('product/product_update.html', shop_id=shop_id, product=product, form=form)



@bp.route("/delete/<int:shop_id>/<int:product_id>")
def delete(product_id, shop_id):

    product = Product.query.get(product_id)

    if g.user.id != product.user_id:
        flash("수정 권한이 없습니다!")
    else:
        product = Product.query.get(product_id)

        db.session.delete(product)
        db.session.commit()

    return redirect(url_for('shop.detail', shop_id=shop_id, product_id=product_id))