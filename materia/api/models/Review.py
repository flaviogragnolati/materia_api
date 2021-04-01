from django.db import models
from .User import User
# from .Product import Product


class Review(models.Model):
    """Model definition for Review."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.SmallIntegerField()
    comment = models.TextField()
    product = models.ManyToManyField(
        'Product', through='ProductReview', related_name='product_id')

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        """Unicode representation of Review."""
        pass

    def save(self):
        """Save method for Review."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Review."""
        return ('')

    # TODO: Define custom methods here
