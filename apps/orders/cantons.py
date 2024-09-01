from django.db import models


class Cantons(models.TextChoices):
    Latacunga = 'Latacunga'
    Pangua = 'Pangua'
    Pujilí = 'Pujilí'
    Salcedo = 'Salcedo'
    Saquisilí = 'Saquisilí'
    Sigchos = 'Sigchos'