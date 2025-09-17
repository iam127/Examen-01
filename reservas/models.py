from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    identity_document = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name