from django.db import models


class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    description = models.TextField()
    products = models.ManyToManyField(
        'Product', through='ProductCategory')

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

    # def save(self):
    #     """Save method for Category."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for Category."""
        return ('')

    # TODO: Define custom methods here
