from django.shortcuts import render
from django.http import HttpResponse
from .models import loginmodel
from .forms import loginForm
def login(request):
    return render(request,'login.html')

#saving data into database
def savedetails(request):
    form= loginForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
    return render(request, 'login.html', context)