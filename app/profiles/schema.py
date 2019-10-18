import graphene
from graphene_django import DjangoObjectType

from .models import CustomerProfile, ManagerProfile


class CustomerProfileType(DjangoObjectType):
    class Meta:
        model = CustomerProfile


class ManagerProfileType(DjangoObjectType):
    class Meta:
        model = ManagerProfile


class UpdateCustomerProfile(graphene.Mutation):
    customer_profile = graphene.Field(CustomerProfileType)

    class Arguments:
        phone_no = graphene.String()
        gender = graphene.String()
        date_of_birth = graphene.Date()

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('must be logged in first')

        if user.role == 'customer':
            profile = CustomerProfile.objects.get(user=user)
        else:
            raise Exception('user must be a customer')

        phone_no = kwargs.get('phone_no')
        gender = kwargs.get('gender')
        date_of_birth = kwargs.get('date_of_birth')

        if phone_no:
            profile.phone_no = phone_no
        if gender:
            profile.gender = gender
        if date_of_birth:
            profile.date_of_birth = date_of_birth

        profile.save()

        return UpdateCustomerProfile(customer_profile=profile)


class UpdateManagerProfile(graphene.Mutation):
    manager_profile = graphene.Field(ManagerProfileType)

    class Arguments:
        phone_no = graphene.String()
        gender = graphene.String()
        date_of_birth = graphene.Date()

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('must be logged in first')
        if user.role == 'manager':
            profile = ManagerProfile.objects.get(user=user)
        else:
            raise Exception('user must be a manager')

        phone_no = kwargs.get('phone_no')
        gender = kwargs.get('gender')
        date_of_birth = kwargs.get('date_of_birth')

        if phone_no:
            profile.phone_no = phone_no
        if gender:
            profile.gender = gender
        if date_of_birth:
            profile.date_of_birth = date_of_birth

        profile.save()

        return UpdateManagerProfile(manager_profile=profile)


class Query(graphene.ObjectType):
    customers_profile = graphene.List(CustomerProfileType)
    managers_profile = graphene.List(ManagerProfileType)

    def resolve_customers_profile(self, info):
        return CustomerProfile.objects.all()

    def resolve_managers_profile(self, info):
        return ManagerProfile.objects.all()


class Mutation(graphene.ObjectType):
    update_customer_profile = UpdateCustomerProfile.Field()
    update_manager_profile = UpdateManagerProfile.Field()
