from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class Shopp(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.title}  {self.address}'
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
        ):
        self.slug = slugify(self.title)
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

class Product(models.Model):
    name = models.CharField(max_length=255)
    shop_name = models.ManyToManyField(Shopp, null=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=2558, blank=True, unique=True)

    def __str__(self):
        return  f"{self.name} - {self.price}"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f"{self.name}-{self.price}")
        return super().save()


