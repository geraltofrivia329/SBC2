from django.shortcuts import render
from SmashApp.models import SmashChars
from django.http import HttpResponse

def SmashApp(request):
    return render(request, 'SmashApp/index.html')
def SmashMario(request):
    #query the db to return all project objects
    Smashfun= SmashChars.objects.all()
    return render(request,'Smashfun/mario.html',
                {'Smashfun':Smashfun})
def about(request):
    return render(request, "SmashApp/about.html")
def Captain_Falcon(request):
    return render(request, "SmashApp/falcon.html")
