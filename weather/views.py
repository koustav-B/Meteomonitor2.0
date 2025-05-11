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
                weather_info = {
    'city': city,
    'region': data['location']['region'],
    'country': data['location']['country'],
    'local_time': data['location']['localtime'],
    'temperature_c': current['temp_c'],
    'feelslike_c': current['feelslike_c'],
    'condition_text': current['condition']['text'],
    'condition_icon': current['condition']['icon'],
    'wind_kph': current['wind_kph'],
    'wind_dir': current['wind_dir'],
    'pressure_mb': current['pressure_mb'],
    'precip_mm': current['precip_mm'],
    'humidity': current['humidity'],
    'cloud': current['cloud'],
    'uv': current['uv'],
    'vis_km': current['vis_km'],
    'gust_kph': current['gust_kph'],
    'last_updated': current['last_updated'],
}

                saved_data = WeatherData.objects.create(
    city=city,
    region=data['location']['region'],
    country=data['location']['country'],
    local_time=data['location']['localtime'],
    temperature_c=current['temp_c'],
    feelslike_c=current['feelslike_c'],
    condition_text=current['condition']['text'],
    condition_icon=current['condition']['icon'],
    wind_kph=current['wind_kph'],
    wind_dir=current['wind_dir'],
    pressure_mb=current['pressure_mb'],
    precip_mm=current['precip_mm'],
    humidity=current['humidity'],
    cloud=current['cloud'],
    uv=current['uv'],
    vis_km=current['vis_km'],
    gust_kph=current['gust_kph'],
    last_updated=parse_datetime(current['last_updated']),
)

    else:
        form = CityForm()

    return render(request, 'weather/weather.html', {'form': form, 'weather_info': weather_info})
