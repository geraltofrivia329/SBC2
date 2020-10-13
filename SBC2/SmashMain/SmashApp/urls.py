from django.urls import path
from SmashApp import views


appname = "SmashApp"

urlpatterns = [
    path('',views.SmashApp, name = 'SmashApp'),
    #path('mario/', views.SmashMario, name = mario),
]
