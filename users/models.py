from django.db import models
from uuid import uuid4

# Create your models here.

class Users(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.FloatField()
    marital_status = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    create_at = models.DateField(auto_now_add=True)




    
#nome
#sobrenome
#idade
#altura
#estado civil
#estado
#cidade
#cpf
#create_at
