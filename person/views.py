from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def person_view(request):
    return HttpResponse('<h1>4564!</h1>')