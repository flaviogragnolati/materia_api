from django.db import models


class OrderItem(models.Model):
    """Model definition for OrderItem."""

    # TODO: Define fields here
    qty = models.SmallIntegerField()
    added_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        """Unicode representation of OrderItem."""
        pass

    def save(self):
        """Save method for OrderItem."""
        pass

    def get_absolute_url(self):
        """Return absolute url for OrderItem."""
        return ('')

    # TODO: Define custom methods here
