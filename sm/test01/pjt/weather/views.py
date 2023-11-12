from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
from .serializers import WeatherSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city = "Seoul,KR"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url).json()
    return Response(response)
# for li in response.get('list'):
#     save_data = {
#         'dt_txt': li.get('dt_txt'),
#         'temp': li.get('main').get('temp'),
#         'feels_like': li.get('main').get('feels_like'),
#     }

# serializer = WeatherSerializer(data=save_data)
# if serializer.is_valid(raise_exception=True):
#     serializer.save()
# return Response(serializer.data)