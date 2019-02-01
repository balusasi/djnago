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

#api creation for post and get methods
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import loginSerializer
class loginapiview(APIView):
    def get(self,request,format=None):
        login=loginmodel.objects.all()
        serializer=loginSerializer(login,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=loginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Newobject is added into database'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

