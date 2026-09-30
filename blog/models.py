from django.db import models

# Create your models here.

class Users_test(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    age = models.PositiveIntegerField(blank=True, null=True)
    discription = models.TextField()
    image = models.ImageField(upload_to="images", blank=False)
    create_at = models.DateTimeField(auto_now_add=True)