from django.db import models


class ProductCategory(models.Model):
    """Model definition for ProductCategory."""

    # TODO: Define fields here
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='products_category')
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='categories')

    class Meta:
        """Meta definition for ProductCategory."""

        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategorys'

    def __str__(self):
        """Unicode representation of ProductCategory."""
        return f"P:{self.product} - C:{self.category}"

    # def save(self):
    #     """Save method for ProductCategory."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for ProductCategory."""
        return ('')

    # TODO: Define custom methods here
