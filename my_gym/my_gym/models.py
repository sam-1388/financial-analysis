from django.db import models

class Client (models.Model):
    mail=models.CharField(max_length=100)
    passs=models.CharField(max_length=100)