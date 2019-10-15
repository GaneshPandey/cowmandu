import graphene
from graphene_django import DjangoObjectType

from .models import User


class UsersType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UsersType)

    def resolve_users(self, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)

