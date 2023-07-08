from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.
dff=(
    ("Jan","January"),
    ('Feb','February'),

)
class Month(models.Model):
    Month_name=models.CharField(max_length=100,choices=dff)

    def __str__(self):
        return self.Month_name


class tasks(models.Model):
    name=models.CharField(max_length=200)
    month=models.ForeignKey(Month,on_delete=CASCADE)
    date=models.DateTimeField('User decided time',help_text="when to complete a task")
    complete=models.BooleanField()
    mark=models.IntegerField
    deadline=models.DateField('last date')
    important=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    logo=models.ImageField(blank=True)

    def __str__(self):
        return self.name

class userp(models.Model):
    username=models.CharField(max_length=200)
    current=models.ImageField()
    preview=models.ImageField()
    submit=models.ImageField()
    logo=models.ImageField()

class Template(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    text=models.CharField(max_length=200)
    Fimage=models.ImageField()
    logo=models.ImageField()

    def get_absolute_url(self):
        return reverse("todo:display", kwargs={"pk": self.pk})
    
    



    
    
   

