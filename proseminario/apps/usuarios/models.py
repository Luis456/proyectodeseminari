from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
# Create your models here.
class Registro(models.Model):
	nick=models.CharField(max_length=150)
	email=models.EmailField()
	usuario=models.ForeignKey(User)