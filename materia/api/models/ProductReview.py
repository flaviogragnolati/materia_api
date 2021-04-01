from django.db import models
# from .Product import Product
# from .Review import Review


class ProductReview(models.Model):
    """Model definition for ProductReview."""

    # TODO: Define fields here
    product = models.ForeignKey(
        'Product', on_delete=models.DO_NOTHING, related_name='products_reviews')
    review = models.ForeignKey(
        'Review', on_delete=models.DO_NOTHING, related_name='reviews')
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for ProductReview."""

        verbose_name = 'ProductReview'
        verbose_name_plural = 'ProductReviews'

    def __str__(self):
        """Unicode representation of ProductReview."""
        return f"{self.product}"

    # def save(self):
    #     """Save method for ProductReview."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for ProductReview."""
        return ('')

    # TODO: Define custom methods here
