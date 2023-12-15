from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
def hello_view(request):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project😍')

def current_date_view(request):
    print(request)
    current_date = timezone.now().date()
    return HttpResponse(f"Time in Bishkek:{current_date}⌛")

def goodby_view(request):
    print(request)
    return HttpResponse('Goodby user! bye bye😊')

