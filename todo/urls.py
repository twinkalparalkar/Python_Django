
from django.urls import path
from . import views

app_name='todo'
urlpatterns = [
    #/
    path('',views.welcome,name="welcome"),
    #/1/home/
    path('home/<int:id>/',views.home,name="home"),
    path('<int:id>/',views.detail,name="detail"),
    #/<int:id>/important
    path('contact/', views.contact, name='index' ),
    path('template/', views.template, name='template'),
    path('<str:pkl>/important',views.important,name="important"),
    path('display/', views.diaplay, name='display'),

    path('add/', views.TemplateCreate.as_view(), name='add'),

]