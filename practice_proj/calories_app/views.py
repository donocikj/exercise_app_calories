from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    """ Renders (/sends) home page of the calories app """
    return HttpResponse('<h1>calories app home</h1>')
