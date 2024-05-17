from flask import Flask, Blueprint, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from . import config
from sqlalchemy import MetaData

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

# db = SQLAlchemy()
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models
    
    from .filter import datetime_fmt
    app.jinja_env.filters['datetime'] = datetime_fmt

    from .views import main_views, shop_views, product_views, test_views, auth_views, weather_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(shop_views.bp)
    app.register_blueprint(product_views.bp)
    app.register_blueprint(test_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(weather_views.bp)


    return app