import graphene
import logging

from apps.core.todo.queries import Query as ToDoQueries
from apps.core.todo.mutations import Mutation as ToDoMutations
from apps.core.seats.mutations import Mutation as SeatsMutations

logger = logging.getLogger(__name__)
class Query(ToDoQueries,graphene.ObjectType):
    pass

class Mutation(SeatsMutations,ToDoMutations,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)