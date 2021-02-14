from django.shortcuts import render
from django.db import connection

def createtab(request):
    if request.method=="POST":
       if request.POST.get('table'):
           cursor = connection.cursor()
           cursor.execute(request.POST.get('table'))
           return render(request,'index.html') 

        else
           return render(request,'index.html')