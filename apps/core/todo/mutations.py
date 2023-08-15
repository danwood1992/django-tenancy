import graphene
from graphene_django import DjangoObjectType
from .models import Task, Assignment, Group, Category, Reminder
from .types import TaskType, AssignmentType, GroupType, CategoryType, ReminderType
from apps.core.seats.models import StaffSeat
from apps.core.seats.types import StaffType
from apps.admin.tenancy.models.tenant import Tenant


class CreateTaskAndAssign(graphene.Mutation):
    task = graphene.Field(TaskType)
    assignment = graphene.Field(AssignmentType)
    success = graphene.Boolean()
    
    class Arguments:
        tenant_id = graphene.UUID(required=True)
        category_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String(required=False)
        due_date = graphene.Date(required=False)
        assigned_by_id = graphene.UUID(required=True)
        assigned_to_id = graphene.UUID(required=True)

    def mutate(self, info, tenant_id, category_id, title, assigned_by_id, assigned_to_id, description=None, due_date=None):
        # First, get the objects needed for ForeignKeys

        tenant = Tenant.objects.get(id=tenant_id)
        category = Category.objects.get(id=category_id)
        assigned_by = StaffSeat.objects.get(id=assigned_by_id)
        assigned_to = StaffSeat.objects.get(id=assigned_to_id)
        
        # Create the task
        task = Task(tenant=tenant, category=category, title=title, description=description, due_date=due_date)
        task.save()

        # Assign the task to the staff
        assignment = Assignment(task=task, assigned_by=assigned_by, assigned_to=assigned_to)
        assignment.save()

        return CreateTaskAndAssign(success=True, task=task, assignment=assignment)
   

class Mutation(graphene.ObjectType):
    assign_task = CreateTaskAndAssign.Field()

