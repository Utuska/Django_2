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

    CONTENT = []
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for element in reader:
            CONTENT.append([element["Name"], element["Street"], element["AdmArea"]])


    print(CONTENT)
    by_page = 10
    current_page = int(request.GET.get('page', 1))

    paginator = Paginator(CONTENT, by_page)
    page_index = paginator.get_page(current_page)
    content = page_index.object_list
    next_page_url = page_index.next_page_number()

    # Не знаю как в этот html записать чтобы составить именно таблицу. У меня получается только первый номер, или прям внутри context делать for
    # return render_to_response('index.html', context={
    #         'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
    #         'current_page': current_page,
    #         'prev_page_url': None,
    #         'next_page_url': next_page_url,
    #     })

    Name = [x[0] for x in content]
    Street = [x[1] for x in content]
    District = [x[2] for x in content]


    return render_to_response('index.html', context={
        'bus_stations': [{'Name': Name, 'Street': Street, 'District': District}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': f'bus_stations?page={next_page_url}',
    })

