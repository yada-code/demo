from django.db import models

class License(models.Model):
    uuid = models.CharField(max_length=255)
    license_key = models.CharField(max_length=255)

    def __str__(self):
        return f"UUID: {self.uuid}, License: {self.license_key}"
