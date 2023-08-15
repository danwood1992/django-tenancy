import graphene
import graphql_jwt
       
       
        
class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    

class Mutation(AuthMutation, graphene.ObjectType):
    pass

# Once you obtain the JWT token, include it in the Authorization header of your subsequent GraphQL requests: