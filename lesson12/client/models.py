from django.db import models

from shop.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.product.name} - {self.username}")


