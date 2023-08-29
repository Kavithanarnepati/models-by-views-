from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def topic_name(request):
    tn=input('enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    return HttpResponse('data inserted sucessfully ')

def insert_webpage(request):
    tn=input('enter topic_name:  ')
    to=Topic.objects.get_or_create(topic_name=tn)[0] 
    to.save()
    n=input('enter name :')
    u=('enter URL : ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('data inserted sucessfully')

def inser_Acessrecords(request):
    tn=input('topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter URL : ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    a=input('enter author: ')
    e=input('enter emali: ')
    Ao=Acessrecords.objects.get_or_create(name=wo,author=a,email=e)[0]
    Ao.save()

    return HttpResponse('data is inserted sucessfully')

