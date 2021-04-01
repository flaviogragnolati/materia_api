from django.db import models
from django.utils.translation import gettext_lazy as _


class Transaction(models.Model):
    """Model definition for Transaction."""

    class TransactionMode(models.TextChoices):
        DEBIT = 'DB', _('Debit')
        MERCADO_PAGO = 'MP', _('MercadoPago')
        TODO_PAGO = 'TP', _('TodoPago')
        CREDIT = 'CR', _('Credit')

    class TransactionStatus(models.TextChoices):
        AWAITING = 'AW', _('Awaiting Payment')
        PROCESSING = 'PR', _('Processing Payment')
        REJECTED = 'RJ', _('Payment Rejected')
        CONFIRMED = 'OK', _('Payment Confirmedd')

    # TODO: Define fields here
    transaction_code = models.SmallIntegerField()
    mode = models.CharField(max_length=2, choices=TransactionMode.choices)
    status = models.CharField(max_length=2, choices=TransactionStatus.choices)
    transaction_start_date = models.DateField(
        auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Transaction."""

        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        """Unicode representation of Transaction."""
        pass

    def save(self):
        """Save method for Transaction."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Transaction."""
        return ('')

    # TODO: Define custom methods here
