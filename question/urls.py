from . import views
from django.urls import path
urlpatterns = [
    path('home/',views.index,name="home"),
    path('api/getquiz/',views.get_quiz,name="get_quiz"),
    path('quiz/',views.quiz,name="quiz")

]
