from flask import Flask, Blueprint, render_template, url_for

bp = Blueprint("main", __name__, url_prefix="/")

@bp.route("/")
def main():
    return "boston!"


@bp.route("/join")
def join():
    return "join"

@bp.route("/news")
def news():
    return render_template("/main/news.html")


@bp.route("/youtube")
def youtube():
    return render_template("/main/youtube.html")