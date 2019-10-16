import graphene
from graphene_django import DjangoObjectType

from .models import BillingProfile


class BillingProfileType(DjangoObjectType):
    class Meta:
        model = BillingProfile


class Query(graphene.ObjectType):
    billingprofiles = graphene.List(BillingProfileType)

    def resolve_billingprofiles(self, info):
        return BillingProfile.objects.all()


schema = graphene.Schema(query=Query)
