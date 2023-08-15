from graphene_django import DjangoObjectType
from .models import Assignment, Task, Reminder, Category, Group

class AssignmentType(DjangoObjectType):
    class Meta:
        model = Assignment
        fields = "__all__"
class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = "__all__"
class ReminderType(DjangoObjectType):
    class Meta:
        model = Reminder
        fields = "__all__"

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"
class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = "__all__"
        