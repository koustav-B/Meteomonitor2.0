import requests
from django.shortcuts import render
from .forms import CityForm
from .models import WeatherData
from django.utils.dateparse import parse_datetime
from django.conf import settings

# Replace with your real API key
API_KEY = '7cfc85bea65c48e69d3195316250905'  # from https://www.weatherapi.com/my/

def get_weather_data(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def weather_view(request):
    weather_info = None
    saved_data = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            data = get_weather_data(city)
            if data:
                current = data['current']
                location = data['location']
                condition = current['condition']

                weather_info = {
                    'city': city,
                    'region': location['region'],
                    'country': location['country'],
                    'local_time': location['localtime'],
                    'temperature_c': current['temp_c'],
                    'temp_f': current['temp_f'],
                    'is_day': current['is_day'],
                    'condition_text': condition['text'],
                    'condition_icon': condition['icon'],
                    'condition_code': condition['code'],
                    'wind_mph': current['wind_mph'],
                    'wind_kph': current['wind_kph'],
                    'wind_degree': current['wind_degree'],
                    'wind_dir': current['wind_dir'],
                    'pressure_mb': current['pressure_mb'],
                    'pressure_in': current['pressure_in'],
                    'precip_mm': current['precip_mm'],
                    'precip_in': current['precip_in'],
                    'humidity': current['humidity'],
                    'cloud': current['cloud'],
                    'feelslike_c': current['feelslike_c'],
                    'feelslike_f': current['feelslike_f'],
                    'windchill_c': current.get('windchill_c', 0.0),
                    'windchill_f': current.get('windchill_f', 0.0),
                    'heatindex_c': current.get('heatindex_c', 0.0),
                    'heatindex_f': current.get('heatindex_f', 0.0),
                    'dewpoint_c': current.get('dewpoint_c', 0.0),
                    'dewpoint_f': current.get('dewpoint_f', 0.0),
                    'vis_km': current['vis_km'],
                    'vis_miles': current['vis_miles'],
                    'uv': current['uv'],
                    'gust_mph': current['gust_mph'],
                    'gust_kph': current['gust_kph'],
                    'last_updated': current['last_updated'],
                }

                saved_data = WeatherData.objects.create(
                    city=city,
                    region=location['region'],
                    country=location['country'],
                    local_time=location['localtime'],
                    temperature_c=current['temp_c'],
                    temp_f=current['temp_f'],
                    is_day=bool(current['is_day']),
                    condition_text=condition['text'],
                    condition_icon=condition['icon'],
                    condition_code=condition['code'],
                    wind_mph=current['wind_mph'],
                    wind_kph=current['wind_kph'],
                    wind_degree=current['wind_degree'],
                    wind_dir=current['wind_dir'],
                    pressure_mb=current['pressure_mb'],
                    pressure_in=current['pressure_in'],
                    precip_mm=current['precip_mm'],
                    precip_in=current['precip_in'],
                    humidity=current['humidity'],
                    cloud=current['cloud'],
                    feelslike_c=current['feelslike_c'],
                    feelslike_f=current['feelslike_f'],
                    windchill_c=current.get('windchill_c', 0.0),
                    windchill_f=current.get('windchill_f', 0.0),
                    heatindex_c=current.get('heatindex_c', 0.0),
                    heatindex_f=current.get('heatindex_f', 0.0),
                    dewpoint_c=current.get('dewpoint_c', 0.0),
                    dewpoint_f=current.get('dewpoint_f', 0.0),
                    vis_km=current['vis_km'],
                    vis_miles=current['vis_miles'],
                    uv=current['uv'],
                    gust_mph=current['gust_mph'],
                    gust_kph=current['gust_kph'],
                    last_updated=parse_datetime(current['last_updated']),
                )
    else:
        form = CityForm()

    return render(request, 'weather/weather.html', {'form': form, 'weather_info': weather_info})
