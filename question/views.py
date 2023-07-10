from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,JsonResponse
import random

def index(request):
    context={'topics':Topic.objects.all()}
    if request.GET.get('topic'):
        return redirect(f"/quiz/?topic={request.GET.get('topic')}")
    return render(request,'home.html',context)

def quiz(request):
    context={'topics':request.GET.get('topic')}
    return render(request,'quiz.html',context)

def get_quiz(request):
    try:
        question_objs=Question.objects.all()
        if request.GET.get('topic'):
            question_objs=question_objs.filter(topic__topic_name__icontains=request.GET.get('topic'))
        
        data=[]
        question_objs=list(question_objs)
        print(question_objs,request.GET.get('topic'))
        random.shuffle((question_objs))
        for question_obj in question_objs:
            data.append({
                'uid':question_obj.uid,
                'topic':question_obj.topic.topic_name,
                'question':question_obj.question_name,
                'marks':question_obj.marks,
                'answers':question_obj.get_answer()
            })

        payload={'status':True,'data':data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
        return HttpResponse("Something Went Wrong")

