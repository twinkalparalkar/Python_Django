from todo.form import ContactForm
from django.shortcuts import get_object_or_404, render
from .models import *
from django.http.response import HttpResponse
from .models import Contact
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'todo/welcome.html')

def detail(request,id):
    out=get_object_or_404(tasks,id)
    return render(request,'todo/detail.html',{'out':out,})

def home(request,id):
    m=get_object_or_404(Month,pk=id)
    return render(request,'todo/home.html',{'month':m,'error_message':"not exit",})

def important(request,pkl):
    m=get_object_or_404(Month,id=pkl)
    try:
        selected_task=m.tasks_set.get(pk=request.POST['tasks'])
    except(KeyError,tasks.DoesNotExist):
        return render(request,'todo/home.html',{'month':m,'error_message':'you did not select'})
    else:
        selected_task.important=True
        selected_task.save()
        return render(request,'todo/home.html',{'month':m})  

def contact(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        logo=request.POST.get('logo')
        contact=Contact()
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.logo=logo
        contact.save()
        return HttpResponse("THANKS FOR CONTACT US")
        
    return render(request,'todo/contact.html')

def template(request):
    form= ContactForm()
    context={'form': form,}
    return render(request,'todo/template.html',context)

def diaplay(request):
    if request.method=="POST":
        templ=request.POST.get('temp')  
        context={"templ":templ,}
        return render(request,'todo/display.html',context) 
    return render(request,'todo/display.html') 
        
class TemplateCreate(CreateView):
    model=Template
    fields=['logo','name']
    template_name='todo/add.html'

