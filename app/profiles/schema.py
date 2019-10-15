import graphene
from graphene_django import DjangoObjectType

from .models import CustomerProfile, ManagerProfile


class CustomersProfileType(DjangoObjectType):
    class Meta:
        model = CustomerProfile


class ManagersProfileType(DjangoObjectType):
    class Meta:
        model = ManagerProfile


class Query(graphene.ObjectType):
    customers_profile = graphene.List(CustomersProfileType)
    managers_profile = graphene.List(ManagersProfileType)

    def resolve_customers_profile(self, info):
        return CustomerProfile.objects.all()

    def resolve_managers_profile(self, info):
        return ManagerProfile.objects.all()


schema = graphene.Schema(query=Query)
