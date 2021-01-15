
from django.db import models


class Cliente(models.Model):
    Nome = models.CharField( max_length= 25, verbose_name= 'Nome')
    sobrenome = models.CharField(max_length=30, verbose_name= 'Sobrenome', null=True)

class Cadastro(models.Model):
    cliente = models.CharField(max_length= 25, verbose_name= 'Nome')
    Sobrenome = models.CharField(max_length= 30, verbose_name= 'Sobrenome')
    Data_de_nascimento = models. DateField (max_length=12, verbose_name='Data de nascimento')
    Email = models.EmailField(max_length= 20, verbose_name= 'Email')
    Apelido = models.CharField(max_length=15, verbose_name='Apelido',null=True)
    Observações = models.TextField(max_length= 200, verbose_name= 'Observações', null=True)

    class Meta:
        ordering = ["cliente"]



# Create your models here.
