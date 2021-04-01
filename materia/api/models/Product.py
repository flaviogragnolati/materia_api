from django.db import models
# from .Review import Review


class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField("Product's name", max_length=50)
    description = models.TextField()
    slug = models.SlugField()
    stock = models.PositiveSmallIntegerField()
    sku = models.CharField(max_length=50)
    metadata = models.CharField(max_length=50)
    live = models.BooleanField()
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    review = models.ManyToManyField(
        'Review', through='ProductReview', related_name='review_id')

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        pass

    def save(self):
        """Save method for Product."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Product."""
        return ('')

    # TODO: Define custom methods here
