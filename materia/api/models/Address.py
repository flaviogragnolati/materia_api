from django.db import models
from .User import User


class Address(models.Model):
    """Model definition for Address."""

    # TODO: Define fields here
    address = models.TextField()
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    address_phone = models.SmallIntegerField()
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING)

    class Meta:
        """Meta definition for Address."""

        verbose_name = 'Address'
        verbose_name_plural = 'Addresss'

    def __str__(self):
        """Unicode representation of Address."""
        pass

    def save(self):
        """Save method for Address."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Address."""
        return ('')

    # TODO: Define custom methods here
