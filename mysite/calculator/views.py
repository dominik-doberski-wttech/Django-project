from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request, number):
    # View code here
    return HttpResponse(f"Hello, World! {number}")


