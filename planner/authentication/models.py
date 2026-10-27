from django.db import models

from django.contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):

    DEVELOPER = 'developer','developer'
    
    ADMIN = 'Admin','Admin'

    PROJECT_COORDINATOR = 'project_coordinator','project_coordinator'

class Profile(AbstractUser):

    role = models.CharField(max_length = 20,choices = RoleChoices.choices)

    class Meta :

        verbose_name ='Profiles'

        verbose_name_plural =' Profiles'

    def __str__(self):

        return self.username

# Create your models here.
