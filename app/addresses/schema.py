import graphene
from graphene_django import DjangoObjectType

from .models import Address


class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class CreateAddress(graphene.Mutation):
    address = graphene.Field(AddressType)

    class Arguments:
        nearby_location = graphene.String()
        address_line_2 = graphene.String()
        address_line_1 = graphene.String(required=True)
        city = graphene.String(required=True)
        latitude = graphene.String()
        longitude = graphene.String()

    def mutate(self, info, **kwargs):
        nearby_location = kwargs.get('nearby_location')
        address_line_2 = kwargs.get('address_line_2')
        address_line_1 = kwargs.get('address_line_1')
        city = kwargs.get('city')
        latitude = kwargs.get('latitude')
        longitude = kwargs.get('longitude')

        address = Address(
            nearby_location=nearby_location,
            address_line_2=address_line_2,
            address_line_1=address_line_1,
            city=city,
            latitude=latitude,
            longitude=longitude
        )
        address.save()
        return CreateAddress(address=address)


class UpdateAddress(graphene.Mutation):
    address = graphene.Field(AddressType)

    class Arguments:
        nearby_location = graphene.String()

    def mutate(self, info, **kwargs):
        pass


class Query(graphene.ObjectType):
    addresses = graphene.List(AddressType)

    def resolve_addresses(self, info):
        return Address.objects.all()


class Mutation(graphene.ObjectType):
    create_address = CreateAddress.Field()
    update_address = UpdateAddress.Field()
