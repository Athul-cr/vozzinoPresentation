from django.db import models


# Create your models here.
class ProfileMod(models.Model):
    user_name = models.CharField(max_length=120, unique=True)
    passwd = models.IntegerField()
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.user_name
