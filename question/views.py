from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
import random

def index(request):
    return render(request,'home.html')

def get_quiz(request):
    try:
        question_objs=list(Question.objects.all())
        data=[]
        print(question_objs)
        random.shuffle((question_objs))
        for question_obj in question_objs:
            data.append({
                'topic':question_obj.topic.topic_name,
                'question':question_obj.question_name,
                'marks':question_obj.marks,
                'answer':question_obj.get_answer()
            })

        payload={'status':True,'data':data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
        return HttpResponse("Something Went Wrong")

