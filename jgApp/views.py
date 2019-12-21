from django.shortcuts import render

# Create your views here.

#没用到模板的简易视图
from django.http import HttpResponse

def index(request):
    return HttpResponse("JG respones")
