from django.contrib import admin
from .models import User  , Student , Classroom 
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Classroom)