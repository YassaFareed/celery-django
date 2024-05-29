
from django.shortcuts import render
from .forms import WeatherLocationForm
from .models import WeatherData
from .tasks import fetch_weather
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
import time
@csrf_exempt 
def weather_view(request):
    if request.method == 'POST':
        form = WeatherLocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            # Replace 'user_api_key' with the actual user's API key.
            api_key = '4c4f111fab89f5825e74348d573b664e'
            task_id = fetch_weather.apply_async((location, api_key))
            task_id = task_id.id
        else:
            task_id = None
    else:
        form = WeatherLocationForm()
        task_id = None
    # time.sleep(5)
    if task_id:
        result = AsyncResult(task_id)
        if result.ready():
            print("ready")
            weather_result = result.get()
            print(weather_result)
        else:
            print("processing")
            weather_result = {'status': 'Processing'}
    else:
        weather_result = None
    weather_data = WeatherData.objects.all().order_by('-timestamp')[:10]

    return render(request, 'weather.html', {'form': form, 'result': {'task_id': task_id} if task_id else None, 'weather_data': weather_data})

from django.http import JsonResponse

def task_status(request, task_id):
    result = AsyncResult(task_id)
    if result.ready():
        response_data = {
            'status': 'completed',
            'result': result.get()
        }
    else:
        response_data = {
            'status': 'processing'
        }
    return JsonResponse(response_data)