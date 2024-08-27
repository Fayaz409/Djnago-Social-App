from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    profileimg=models.ImageField(upload_to='profile_images', )
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + str(self.age)