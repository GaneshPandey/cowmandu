import graphene
import graphql_jwt
import users.schema
import profiles.schema
import addresses.schema
import billings.schema

from graphene_django.debug import DjangoDebug


class Query(
    users.schema.Query,
    profiles.schema.Query,
    addresses.schema.Query,
    billings.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(
    users.schema.Mutation,
    addresses.schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)
