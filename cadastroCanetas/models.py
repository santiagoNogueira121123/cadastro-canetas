from django.db import models

class Caneta(models.Model):
    
    marca = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    data_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"marca: {self.marca} - cor: {self.cor} - preco: {self.preco:.2f} - data: {self.data_added.strftime('%d/%m/%Y %H:%M')}"