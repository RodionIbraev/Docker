from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    image = models.TextField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField(max_length=255)
