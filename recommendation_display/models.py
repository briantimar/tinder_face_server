from django.db import models

# Create your models here.

class User(models.Model):
    """ represents a single Tinder user """
    #user's first name
    first_name = models.CharField(max_length=50)
    #user's last name
    last_name = models.CharField(max_length=50)
    # user's tinder authentification
    tinder_auth_token = models.CharField(max_length=200)
