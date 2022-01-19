import requests
from modules.sense import speak
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=5bddd4ad4f4f192f6dfffe714388c103');
	return res.json();
def print_weather(result,usercity):
    
    speak("{}'s temperature is {} degress Celcius ".format(usercity,result['main']['temp']-273))
    speak("Wind speed is {} meters per second".format(result['wind']['speed']))
	
    speak("The weather looks {}".format(result['weather'][0]['description']))
	
    print("Weather: {}".format(result['weather'][0]['main']))
def weathermain(usercity):
    try:
        query='q='+usercity;
        w_data=weather_data(query);
        print_weather(w_data, usercity)
        print()
    except:
        print('City name not found...')

