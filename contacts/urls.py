from django.urls import path

from .views import ContactListView, ContactDetailView

urlpatterns = [
    path("", view=ContactListView.as_view(), name="contact-list"),
    path("<int:pk>/", view=ContactDetailView.as_view(), name="contact-detail"),
]
