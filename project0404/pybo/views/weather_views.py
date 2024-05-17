from flask import render_template, Blueprint, Flask
import pandas as pd
import requests, json, math, certifi
from time import sleep
import time


bp = Blueprint("weather", __name__, url_prefix="/weather")
df = pd.read_excel("pybo/static/others/기상청_격자_위경도.xlsx")
df1 = df.copy()

df2 = df.drop(df.columns[7:-3], axis="columns")
df2 = df2.drop(df2.columns[[0,-1]], axis="columns")
df3 = df2.rename(columns={"격자 X":"X", "격자 Y":"Y", "경도(초/100)":"경도", "위도(초/100)":"위도"})

@bp.route("/item/<date>/<address>")
def get_weather_item(date, address):
    global df3
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
    api = "9jQuebyMuMclGG%2FnrLqbFDdLYuOJouKyBF3By3WWSeDYlQX%2Bicevyw3bAu6BEwDPKF5e%2FXoFywFK8V%2BqTS8iJg%3D%3D"
    df3_result = get_xy(address)
    
    nx = df3_result[0]
    ny = df3_result[1]

    url = f'{url}?serviceKey={api}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={date}&base_time=0600&nx={nx}&ny={ny}'

    response = requests.get(url)

    json_bytes = response.content
    json_str = json_bytes.decode("utf-8")
    weather = json.loads(json_str)
    item = weather["response"]["body"]["items"]["item"]

    return item



def change_city_name(city):
    dic1 = {
        "경기":"경기도",
        "서울":"서울특별시",
        "경남":"경상남도",
        "경북":"경상북도",
        "전남":"전라남도",
        "전북":"전라북도",
        "충남":"충청남도",
        "부산":"부산광역시",
        "강원":"강원특별자치도",
        "충북":"충청북도",
        "인천":"인천광역시",
        "대구":"대구광역시",
        "광주":"광주광역시",
        "대전":"대전광역시",
        "울산":"울산광역시",
        "제주":"제주특별자치도",
        "세종":"세종특별자치시",
        "이어":"이어도"
    }
    
    try:
        return dic1[city]
    except KeyError as e:
        return city
        
    


def get_xy(address):
    arr = address.split(" ")
    
    arr[0] = change_city_name(arr[0])
    
    cond1 = df3["1단계"].str.contains(arr[0])
    
    size = len(arr)
    
    val = ""
    
    if size == 1:
        cond2_na = df3["2단계"].isnull()
        cond3_na = df3["3단계"].isnull()
        
        val = df3.loc[cond1 & cond2_na & cond3_na]
        
    elif size == 2:
        cond2 = df3["2단계"].str.contains(arr[1])
        cond3_na = df3["3단계"].isnull()
        
        val =  df3.loc[cond1 & cond2 & cond3_na]
    
    elif size == 3:
        cond2 = df3["2단계"].str.contains(arr[1])
        cond3 = df3["3단계"].str.contains(arr[2])
        
        val =  df3.loc[cond1 & cond2 & cond3]
    
    idx = val.index.tolist()[0]
    
    return val.loc[idx, "X"], val.loc[idx, "Y"]