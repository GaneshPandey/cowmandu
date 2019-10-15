import graphene
import users.schema
import profiles.schema

from graphene_django.debug import DjangoDebug


class Query(
    users.schema.Query,
    profiles.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)
