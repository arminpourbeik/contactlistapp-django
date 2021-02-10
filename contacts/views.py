from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters

from .serializers import ContactSerializer
from .models import Contact


class ContactListView(generics.ListCreateAPIView):
    """
    View for list and creating contacts
    """

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "last_name"]

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrive, update, and destroy contact instance
    """

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
