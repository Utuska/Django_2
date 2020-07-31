from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.http import HttpResponse

import csv
# знаю что надо использовать django.conf но почему то не работает
from app import settings

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        CONTENT = list(csv.DictReader(csvfile))

    by_page = 100
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, by_page)
    page_index = paginator.get_page(current_page)
    content = page_index.object_list
    if page_index.has_next():
        next_page_url = page_index.next_page_number()
    else:
        next_page_url = current_page
    if page_index.has_previous():
        previous_page_url = page_index.previous_page_number()
    else:
        previous_page_url = current_page

    print(content)

    return render_to_response('index.html', context={
        'bus_stations': content,
        'current_page': current_page,
        'prev_page_url': f'bus_stations?page={previous_page_url}',
        'next_page_url': f'bus_stations?page={next_page_url}',
    })

