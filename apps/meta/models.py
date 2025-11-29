from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=255, unique=True)
    label = models.CharField(max_length=100)
    verbose_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["label"]

    def __str__(self) -> str:
        return self.verbose_name
