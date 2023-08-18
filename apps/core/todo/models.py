from typing import Iterable, Optional
from django.db import models
import uuid
from apps.admin.realms.models import Realm
from apps.admin.realms.models import RealmAccount

class Group(models.Model): #group of tasks
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    tasks = models.ManyToManyField('Task', related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.Realm} - {self.name}'
    
class Category(models.Model): # task category
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'  
class Reminder(models.Model): # task reminder
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE)
    message = models.TextField(default='You have a task due',null=True, blank=True)
    notify_at = models.DateTimeField(null=True, blank=True)
    snooze = models.DateTimeField(null=True, blank=True)
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.message} - {self.assignment} - {self.Realm}'
    
    
class Task(models.Model): # task itself
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Assignment(models.Model):
    
    assigned_by = models.ForeignKey(RealmAccount, on_delete=models.CASCADE, related_name='assigned_by')
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(RealmAccount, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.task}'