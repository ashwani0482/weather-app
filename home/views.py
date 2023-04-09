from django.shortcuts import render
import requests


def home(request):
    
    city = request.GET.get('city', 'Pathankot')
    url = f'http://api.weatherapi.com/v1/current.json?key=3e2f4d7b4f4a4216914112023230904&q={city}&aqi=yes'

    data = requests.get(url).json()
    payload = {'city':data['location']['name'],
            'date': data['location']['localtime'],  
            'country': data['location']['country'],
            'weather' : data['current']['condition']['text'], 
            'icon': data['current']['condition']['icon'], 
            'temprature_c': data['current']['temp_c'], 
            'temprature_f': data['current']['temp_f'], 
            'pressure_mb':data['current']['pressure_mb'], 
            'humidity': data['current']['humidity']}
    context = {'data': payload}
    return render(request, 'home.html', context)
