from flask import Flask,render_template,request
import requests
import json
from urllib.request import urlopen

#for fetching user country details and ip addresses
url='https://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)

# print(city)

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':


        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ebe8bc80775f683f2f1f1cb25b020176'
        city=request.form.get('inputTxt')
        r=requests.get(url.format(city)).json()   #it will fetch the data from api and retun it in json format
        weather={
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        return render_template('index.html',weather=weather)
    else:
            
            city1=data['city']
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ebe8bc80775f683f2f1f1cb25b020176'
            # city=request.form.get('inputTxt')
            r=requests.get(url.format(city1)).json()   #it will fetch the data from api and retun it in json format
            weather={
                'city':city1,
                'temperature':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon':r['weather'][0]['icon']
            }
            
            return render_template('index.html',weather=weather)




app.run(debug=True,port=7000)

