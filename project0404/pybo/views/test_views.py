from flask import Flask, Blueprint, render_template, url_for, request, send_file
from datetime import datetime
import time
import os
import random
import string

import pandas as pd

bp = Blueprint("test", __name__, url_prefix="/test")

@bp.route("/gdpark")
def gdpark():
    return render_template("test/gd_park.html")

@bp.route("/population/<int:month>")
def population(month):
    list_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if month in list_month:
        return render_template(f"test/{month}월_인구.html")
    else:
        return render_template(f"test/총합_인구.html")
    
@bp.route("/map")
def map():
    return render_template("test/0424_map1.html")

@bp.route("/chart")
def chart():
    df = pd.read_csv("pybo/static/csv/boston.csv")
    labels = list(df.columns)
    data = []
    data_float = list(df.loc[0])

    for num in data_float:
        data.append(int(num))
    print(labels)
    print(type(data[0]))
    print(type(data_float[0]))
    print("#"*20)
    return render_template("test/chart.html", labels=labels, data=data)






@bp.route("/download")
def download():
    filename = request.args.get("filename")
    print(":::::::::::::::::::::::::::::::::")
    print(filename)
    print(":::::::::::::::::::::::::::::::::")
    return send_file("./"+filename, 
                     download_name=extract_origin_name(filename),
                     as_attachment=True)



@bp.route("upload_ajax", methods=("POST",))
def upload_ajax():
    id = request.form.get("id")
    print(id)
    print(":::::::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::::::::")

    file = request.files["file_ajax"]
    filename = file.filename

    filename = make_new_name(filename)
    upload_path = makedirectory()

    path = os.path.join(upload_path, filename)

    file.save(path)

    idx = path.find("/static/upload")

    return path[idx:]



def extract_origin_name(filename):
    new_name = make_new_name(filename)
    idx = new_name.find("_") + 1
    for i in range(3):
        idx = new_name.find("_", idx) + 1
    return new_name[idx:]




def make_new_name(name):
    letters = string.ascii_lowercase

    name_ymd = datetime.now().strftime("%Y%m%d")
    rnd_name = [random.choice(letters) for i in range(10)]
    msg = "".join(rnd_name)


    return msg+"_"+name_ymd+"_"+name


def makedirectory():
    UPLOAD_DIR="pybo/static/upload"
    name_ymd = datetime.now().strftime("%Y%m%d")

    new_dir_path = os.path.join(UPLOAD_DIR, name_ymd)

    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)

    return new_dir_path


@bp.route("/upload", methods=("POST", ))
def upload():
    file = request.files["file"]
    filename = file.filename

    filename = make_new_name(filename)

    upload_path = makedirectory()

    path = os.path.join(upload_path, filename)
    path = path.replace("\\", "/")
    file.save(path)

    idx = path.find("/static/upload")

    return path[idx:]

@bp.route("/uploadform")
def uploadform():
    return render_template("test/file_upload.html")



@bp.route("/parent")
def parent():
    return render_template("test/parent.html")

@bp.route("/child")
def child():
    return render_template("test/child.html")


@bp.route("/join")
def join():
    return "join"


@bp.route("/check_id_form")
def check_id_form():
    return render_template("test/check_id.html")



@bp.route("/checkid/<int:id>")
def checkid(id):
    return str(id)+": test"










def mul(n):
    def wrapper(m):
        return n*m
    return wrapper

@bp.route("/deco")
def deco():
    w = monitor(hello)
    return hello()

def monitor(func):
    def wrapper(*args, **kwargs): # 값이 없으면 상관없음, 값이 있으면 무시
        start = time.time()
        func()
        end = time.time()

        return str(end-start)
    
    return wrapper


@monitor # hello 함수를 monitor 함수에 인자로 넣어주세요
def hello():
    start = time.time()

    for i in range(100):
        print("world")

    end = time.time()

    return str(end-start)