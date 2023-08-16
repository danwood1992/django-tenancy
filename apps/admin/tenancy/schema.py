import graphene

class Query(Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)