from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=250 , db_index=True)
    slug = models.SlugField(max_length=250 , unique=True)

    class Meta:
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name
    


class Product(models.Model):

    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250 , default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title