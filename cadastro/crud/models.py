from msilib.schema import Class
from django.db import models

class Produtos(models.Model):
  nome=models.CharField(max_length=50)
  def __str__(self) -> str:
    return self.nome
  
class Cliente(models.Model):
  fullnome=models.CharField(max_length=50)
  endereco=models.CharField(max_length=50)
  produto=models.ForeignKey(Produtos,on_delete=models.CASCADE)
  
