import graphene
import logging

logger = logging.getLogger(__name__)
class Query(graphene.ObjectType):
    logging.info("Query class called")
    hello = graphene.String(default_value="Hi!")

schema = graphene.Schema(query=Query)