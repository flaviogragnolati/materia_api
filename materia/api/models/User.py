from django.db import models


class User(models.Model):
    """Model definition for User."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    dob = models.DateField('date of birth', auto_now=False, auto_now_add=False)
    email = models.EmailField('user email', max_length=254)
    phone = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now=False, auto_now_add=True)
    last_login = models.DateField(auto_now=False, auto_now_add=False)
    modified_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        pass

    def save(self):
        """Save method for User."""
        pass

    def get_absolute_url(self):
        """Return absolute url for User."""
        return ('')

    # TODO: Define custom methods here
