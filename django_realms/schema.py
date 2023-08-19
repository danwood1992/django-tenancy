import graphene
import logging

from apps.core.todo.queries import Query as ToDoQueries
from apps.core.todo.mutations import Mutation as ToDoMutations

from apps.admin.realms.mutations import Mutation as RealmMutations
from apps.admin.realms.queries import Query as RealmQueries

logger = logging.getLogger(__name__)
class Query(ToDoQueries,graphene.ObjectType):
    pass

class Mutation(RealmMutations,ToDoMutations,graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query, mutation=Mutation )