from django.db import models
import uuid
import random

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract=True#to inherit

class Topic(BaseModel):
    topic_name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.topic_name

class Question(BaseModel):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='topic')
    question_name=models.CharField(max_length=100)
    marks=models.IntegerField(default=5)
    def __str__(self) -> str:
        return self.question_name
    
    def get_answer(self):
        answer_objs=list(Answer.objects.filter(question=self))
        random.shuffle((answer_objs))
        data=[]
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct':answer_obj.is_correct
            })
        return data

class Answer(BaseModel):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question_answer')
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.answer
