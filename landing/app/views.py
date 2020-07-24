from collections import Counter

from django.http import HttpResponse
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    trigger = request.GET.get('from-landing')
    if trigger == 'original':
        counter_click['origin'] += 1
    elif trigger == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request):
    test = request.GET.get('ab-test-arg')
    if test == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    elif test == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')


def stats(request):
    try:
        count_test = counter_click['test'] / counter_show['test']
    except ZeroDivisionError:
        count_test = "Переходов не было"
    try:
        count_orig = counter_click['origin'] / counter_show['original']
    except ZeroDivisionError:
        count_orig = "Переходов не было"

    return render_to_response('stats.html', context={
        'test_conversion': count_test,
        'original_conversion': count_orig,
    })
