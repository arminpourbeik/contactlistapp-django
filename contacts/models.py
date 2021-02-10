from django.db import models
from django.contrib.auth import get_user_model


class Contact(models.Model):
    """
    Contact database table
    """

    country_code = models.CharField(max_length=5)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    contact_picture = models.URLField(null=True, blank=True)
    is_favorite = models.BooleanField(default=False)
    owner = models.ForeignKey(
        to=get_user_model(),
        related_name="contacts",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (
            "first_name",
            "last_name",
        )

    def __str__(self) -> str:
        return f"{self.first_name}-{self.last_name}"
