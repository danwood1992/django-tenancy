import graphene
from graphene_django import DjangoObjectType
from .models import Task, Assignment, Group, Category, Reminder
from .types import TaskType, AssignmentType, GroupType, CategoryType, ReminderType
from apps.core.seats.models import StaffSeat
from apps.core.seats.types import StaffType
from apps.admin.tenancy.models.models import Tenant

# I have commented heavily for an easier time creating a new mutation 

class CreateTaskAndAssign(graphene.Mutation):
    # Define the output fields of the mutation.
    # The mutation will return an instance of a Task, an Assignment and a boolean indicating if the operation was successful.
    task = graphene.Field(TaskType)
    assignment = graphene.Field(AssignmentType)
    success = graphene.Boolean()
    
    # Arguments class specifies the input fields required to perform the mutation.
    class Arguments:
        tenant_id = graphene.UUID(required=True)
        category_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String(required=False)
        due_date = graphene.Date(required=False)
        assigned_by_id = graphene.UUID(required=True)
        assigned_to_id = graphene.UUID(required=True)

    def mutate(self, info, tenant_id, category_id, title, assigned_by_id, assigned_to_id, description=None, due_date=None):
        
        # Retrieve objects from the database that are referenced by foreign keys.
        # Fetch the tenant using its unique ID.
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
        # Return the newly created task, assignment and a success flag set to True.
        return CreateTaskAndAssign(success=True, task=task, assignment=assignment)
   

class TaskCompletion(graphene.Mutation):
    task = graphene.Field(TaskType)
    success = graphene.Boolean()
    class Arguments:
        
        task_id = graphene.UUID(required=True)
        
    def mutate(self, info, task_id):
        
        task = Task.objects.get(id=task_id)
        if task.completed:
            task.completed = False
        else:
            task.completed = True
            
        task.save()
        return TaskCompletion(task=task, success=True,)
    


class Mutation(graphene.ObjectType):
    task_completion = TaskCompletion.Field()
    assign_task = CreateTaskAndAssign.Field()

