import graphene
import logging

from apps.core.todo.queries import Query as ToDoQueries
from apps.core.todo.mutations import Mutation as ToDoMutations

logger = logging.getLogger(__name__)
class Query(ToDoQueries,graphene.ObjectType):
    pass

class Mutation(ToDoMutations,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)