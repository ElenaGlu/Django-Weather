from django.shortcuts import render

from .app_services import get_forecast_for_today, get_forecast_for_five_days
from .forms import PlaceForm


def loading_search_page(request):
    return render(request, 'App/base.html')


def displays_weather_forecast_in_the_city(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            forecast_for_today = get_forecast_for_today(city)
            forecast_for_five_days = get_forecast_for_five_days(city)

            return render(request, 'App/weather_forecast.html', {'forecast_for_today': forecast_for_today,
                                                                 'forecast_for_five_days': forecast_for_five_days})

        raise ValueError()

