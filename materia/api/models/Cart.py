from django.db import models
from .User import User


class Cart(models.Model):
    """Model definition for Cart."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        """Meta definition for Cart."""

        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        """Unicode representation of Cart."""
        pass

    def save(self):
        """Save method for Cart."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Cart."""
        return ('')

    # TODO: Define custom methods here
