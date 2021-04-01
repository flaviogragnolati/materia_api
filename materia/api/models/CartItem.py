from django.db import models
from .Cart import Cart
from .Product import Product


class CartItem(models.Model):
    """Model definition for CartItem."""

    # TODO: Define fields here
    qty = models.SmallIntegerField()
    added_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateField(auto_now=False, auto_now_add=False)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        """Meta definition for CartItem."""

        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    def __str__(self):
        """Unicode representation of CartItem."""
        return f"{self.product} of {self.cart}"

    # def save(self):
    #     """Save method for CartItem."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for CartItem."""
        return ('')

    # TODO: Define custom methods here
