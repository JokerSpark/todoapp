from django.db import models

# Create your models here.


class task(models.Model):
    task = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task