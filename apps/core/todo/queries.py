import graphene
from .models import StaffSeat
from .types import AssignmentType, TaskType, ReminderType, CategoryType, GroupType

class Query(graphene.ObjectType):
    assignments = graphene.List(AssignmentType)
    tasks = graphene.List(TaskType)
    reminders = graphene.List(ReminderType)
    categories = graphene.List(CategoryType)
    groups = graphene.List(GroupType)

    def resolve_all_assignments(self, info, **kwargs):
        return AssignmentType.objects.all()
    
    def resolve_all_tasks(self, info, **kwargs):
        return TaskType.objects.all()
    
    def resolve_all_reminders(self, info, **kwargs):
        return ReminderType.objects.all()
    
    def resolve_all_categories(self, info, **kwargs):
        return CategoryType.objects.all()
    
    def resolve_all_groups(self, info, **kwargs):
        return GroupType.objects.all()
    