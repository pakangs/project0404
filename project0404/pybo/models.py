from pybo import db

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref=db.backref("shop_set"))

    name = db.Column(db.String(50), nullable=False)
    owner = db.Column(db.String(50), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    update_date = db.Column(db.DateTime(), nullable=False)
    file_path = db.Column(db.String(200), nullable=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id', ondelete='CASCADE'))
    shop = db.relationship('Shop', backref=db.backref('product_set'))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref=db.backref("product_set_"))

    name = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    info = db.Column(db.String(100), nullable=True)
    manufacturing_date = db.Column(db.DateTime(), nullable=False)
    expiration_date = db.Column(db.DateTime(), nullable=False)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)



