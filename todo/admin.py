
from .models import *
from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)
admin.site.register(Month)
admin.site.register(tasks)
admin.site.register(Contact)
admin.site.register(Template)