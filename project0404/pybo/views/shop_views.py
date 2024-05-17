from flask import Flask, Blueprint, render_template, url_for, request, session, g, flash
from pybo.models import Shop, Product, User
from pybo import db
from werkzeug.utils import redirect
from datetime import datetime
from pybo.forms import ShopForm
import time, os
from pybo.views.auth_views import required_login
from pybo.views.test_views import extract_origin_name, make_new_name, makedirectory

bp = Blueprint("shop", __name__, url_prefix="/shop")


@bp.before_app_request # 어떤 요청이 들어오더라도 반드시 먼저 실행하는 코드
def set_g():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route("/")
def shop():
    return render_template("/shop/shop_main.html")


@bp.route("/list", methods=("GET", "POST"))
def list():

    per_page = 10
    # if request.method == "POST":

    page = request.args.get("page", type=int, default=1)
    shop_list = Shop.query.order_by(Shop.create_date)
    shop_list = shop_list.paginate(page=page, per_page=per_page)
    return render_template("/shop/shop_list.html", shop_list=shop_list)



@bp.route("/create", methods=("GET", "POST"))
@required_login
def create():

    form = ShopForm()

    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data # form 태그에서 데이터 가져오기
        owner = form.owner.data
        user_id = form.user_id.data

        file = request.files["file"]
        filename = file.filename

        filename = make_new_name(filename)
        upload_path = makedirectory()

        path = os.path.join(upload_path, filename)
        path = path.replace("\\", "/")

        file.save(path)

        idx = path.find("/static/upload")
        file_path = path[idx:]

        shop = Shop(user_id=user_id, name=name, owner=owner, create_date=datetime.now(), update_date=datetime.now(), file_path=file_path)


        db.session.add(shop)

        db.session.commit()
        return redirect(url_for('shop.list'))
    else:
        return render_template("shop/shop_form.html", form=form)



@bp.route("/detail/<int:shop_id>")
def detail(shop_id):
    
    shop = Shop.query.get(shop_id)
    return render_template("/shop/shop_detail.html", shop = shop)



@bp.route("/update/<int:shop_id>", methods=("GET", "POST"))
def update(shop_id):

    shop = Shop.query.get(shop_id)
    
    if request.method == "POST":
        form = ShopForm()

        print("name: ", form.name.data)
        print("owner: ", form.owner.data)
        print("file_path: ", form.file_path.data)


        if form.validate_on_submit():

            if g.user != shop.user:
                flash("수정권한이 없습니다.")
                return redirect(url_for("shop.update", shop_id=shop_id))

            del_img = request.form.get("del_img")
            delete_filename = form.file_path.data
            delete_file_path = "pybo" + delete_filename

            if del_img == "-1":
                if delete_filename:
                    os.remove(delete_file_path)
                    shop.file_path=None

            file = request.files["file"]
            if file:
                if delete_filename:
                    os.remove(delete_file_path)

                filename = file.filename

                filename = make_new_name(filename)
                upload_path = makedirectory()

                path = os.path.join(upload_path, filename)
                path = path.replace("\\", "/")

                file.save(path)

                idx = path.find("/static/upload")
                file_path = path[idx:]

                shop.file_path = file_path

            name = form.name.data
            owner = form.owner.data
            shop.name = name
            shop.owner = owner
            
            shop.update_datetime = datetime.now()

            db.session.commit()
            return redirect(url_for('shop.detail', shop_id=shop_id))
    else:
        form = ShopForm(obj=shop)
        g.is_update=True
    
    return render_template("shop/shop_update.html", shop_id=shop_id, form=form)





@bp.route("/delete/<int:shop_id>")
def delete(shop_id):
    shop = Shop.query.get(shop_id)
    if g.user != shop.user:
        return redirect(url_for('shop.detail', shop_id=shop_id))
    
    db.session.delete(shop)
    db.session.commit()

    return redirect(url_for("shop.list"))