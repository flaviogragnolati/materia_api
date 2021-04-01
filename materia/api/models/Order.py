from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    """Model definition for Order."""

    class OrderStatus(models.IntegerChoices):
        CANCELLED = 0, _('Cancelled')
        SUBMITTED = 1, _('Submitted')
        CONFIRMED = 2, _('Confirmed')
        BOOKED = 3, _('Booked and upfront recieved')
        PAYED = 4, _('Completely payed')
        DELIVERED = 5, _('Delivered to user')
        RETURNED = 6, _('Returned from user')

    # TODO: Define fields here
    order_num = models.PositiveIntegerField()
    total = models.SmallIntegerField()
    sub_total = models.SmallIntegerField()
    grand_total = models.SmallIntegerField()
    tax = models.SmallIntegerField()
    global_discount = models.SmallIntegerField()
    status = models.SmallIntegerField(choices=OrderStatus.choices)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return self.order_num

    # def save(self):
    #     """Save method for Order."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for Order."""
        return ('')

    # TODO: Define custom methods here
