from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'base.html')
    # return HttpResponse("Hello everyone")