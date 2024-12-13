from django.db import models


# model from boutique ado 
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    def __str__(self):
        return self.name
    def get_friendly_name(self):
        return self.friendly_name

# model based of off boutique ado
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # what ive added in 
    genre = models.CharField(max_length=254, null=True, blank=True)  # For game genre
    platform = models.CharField(max_length=254, null=True, blank=True)  # For gaming platform
    release_date = models.DateField(null=True, blank=True)  # Release date of the game
    publisher = models.CharField(max_length=254, null=True, blank=True)
    def __str__(self):
        return self.name