
from django.contrib import admin
from django.urls import path
from home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('getstudent',get_students,name="get_api"),
    path('poststudent',post_students,name="post_api")
]
