from django.contrib import admin
from .models import Task, Assignment, Reminder, Category, Group

admin.site.register(Task)
admin.site.register(Assignment)
admin.site.register(Reminder)
admin.site.register(Category)
admin.site.register(Group)

