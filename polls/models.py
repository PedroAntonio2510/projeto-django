from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  phone_number = models.CharField(max_length=20)
  image = models.ImageField(upload_to='pics', default='default.svg')

  def __str__(self):
    return self.name