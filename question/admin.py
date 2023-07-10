from django.contrib import admin
from .models import *

admin.site.register(Topic)


class AnswerAdmin(admin.StackedInline):
    model=Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerAdmin]
     
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
