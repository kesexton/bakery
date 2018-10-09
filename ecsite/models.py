from django.db import models
from django.utils import timezone

class Menu(models.Model):
    title = models.CharField(max_length=200)
    size1 = models.CharField(max_length=200)
    size2 = models.CharField(max_length=200)
    price1 = models.CharField(max_length=20)
    price2 = models.CharField(max_length=20)
    text = models.TextField()
    imageUrl = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title