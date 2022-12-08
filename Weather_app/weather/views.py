from django.shortcuts import render, redirect
from weather.key import api_key

import datetime 
import zoneinfo
import requests
import math
import json
import urllib.request

""" from .models import City
from .forms import CityForm """
"""         print(dataset)"""
def index(request):
    #create time zones  
    tz_buenosAires = zoneinfo.ZoneInfo("America/Buenos_Aires")
    tz_tokyo = zoneinfo.ZoneInfo("Asia/Tokyo")
    tz_nuevaYork = zoneinfo.ZoneInfo("America/New_York")
    tz_finland = zoneinfo.ZoneInfo("Europe/Helsinki")

    #create time objects
    time_buenosAires = datetime.datetime.now(tz_buenosAires)
    time_tokyo = datetime.datetime.now(tz_tokyo)
    time_nuevaYork = datetime.datetime.now(tz_nuevaYork)
    time_finland = datetime.datetime.now(tz_finland)

    #create time strings with day month hour am or pm
    time_buenosAires = time_buenosAires.strftime(" %d %b, %I:%M %p")
    time_tokyo = time_tokyo.strftime("%d %b, %I:%M %p")
    time_nuevaYork = time_nuevaYork.strftime(" %d %b, %I:%M %p")
    time_finland = time_finland.strftime("%d %b, %I:%M %p")

    context = {
        "time_buenosAires": time_buenosAires,
        "time_tokyo": time_tokyo,
        "time_nuevaYork": time_nuevaYork,
        "time_finland": time_finland,
    }

    return render(request, "weather/index.html", context)

def results(request):
    if request.method == "POST":
        city = request.POST['city'].lower()
        if " " in city:
            city = city.replace(" ", "%20")
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
        http = requests.get(url).json()

        if http['cod'] != "200":
            return render(request, "weather/results.html", {"error": "City not found"})
            
        source = urllib.request.urlopen(url).read()
        dataset = json.loads(source)
        
        try: 
            context = {
                ###
                "country": dataset['city']['country'],
                "city": dataset['city']['name'],
                "degree": dataset['list'][0]['wind']['deg'],
                'status': dataset['list'][0]['weather'][0]['description'],
                'wind': dataset['list'][0]['wind']['speed'],
                'clouds': dataset['list'][0]['clouds']['all'],
                'date0': dataset['list'][0]["dt_txt"],
                'date1': dataset['list'][1]["dt_txt"],
                'date2': dataset['list'][2]["dt_txt"],
                'date3': dataset['list'][3]["dt_txt"],
                'date4': dataset['list'][4]["dt_txt"],
                'date5': dataset['list'][5]["dt_txt"],
                'date6': dataset['list'][6]["dt_txt"],


                "temp": round(dataset["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(dataset["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(dataset["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(dataset["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(dataset["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(dataset["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(dataset["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(dataset["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(dataset["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(dataset["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(dataset["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(dataset["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(dataset["list"][6]["main"]["temp_max"] -273.0),


                "pressure":dataset["list"][0]["main"]["pressure"],
                "humidity":dataset["list"][0]["main"]["humidity"],
                "sea_level":dataset["list"][0]["main"]["sea_level"],


                "weather":dataset["list"][1]["weather"][0]["main"],
                "description":dataset["list"][1]["weather"][0]["description"],
                "icon0":dataset["list"][0]["weather"][0]["icon"],
                "icon1":dataset["list"][1]["weather"][0]["icon"],
                "icon2":dataset["list"][2]["weather"][0]["icon"],
                "icon3":dataset["list"][3]["weather"][0]["icon"],
                "icon4":dataset["list"][4]["weather"][0]["icon"],
                "icon5":dataset["list"][5]["weather"][0]["icon"],
                "icon6":dataset["list"][6]["weather"][0]["icon"],
            }

        except: 
            context = {
                "error": "City not found",
            }

        return render(request, "weather/results.html", context)
    
    else:
        return redirect("home")

def cameras(request):
    
    return render(request, "weather/cameras.html")

def contact(request):
    return render(request, "weather/contact.html")

def thankyou(request):
    return render(request, "weather/thankyou.html")