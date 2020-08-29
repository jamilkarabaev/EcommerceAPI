from rest_framework import viewsets, generics
from user import permissions as userpermissions
from item import permissions as itempermissions
from rest_framework import permissions, authentication
from item import serializers
from core import models

#list and retrieve item for buyer on homepage

class ListItemView(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()

class RetrieveItemView(generics.RetrieveAPIView):
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    lookup_field = 'pk'


#create and list and retrieve,update,destroy
class CreateItemView(generics.CreateAPIView):
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (userpermissions.IsSeller, )
    serializer_class = serializers.ItemSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class MyListedItemView(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (userpermissions.IsSeller, )
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()

    def get_queryset(self):
        return self.queryset.fitler(user=self.request.user)

class RetrieveUpdateDestroyItemView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (itempermissions.IsOwnerOfItem, )
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(seller=self.request.user)






    





