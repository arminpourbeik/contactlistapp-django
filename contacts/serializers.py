from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for contact instance
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Contact
        fields = (
            "pk",
            "country_code",
            "first_name",
            "last_name",
            "phone_number",
            "contact_picture",
            "is_favorite",
            "owner",
        )
