from django.db import models

class Usuario(models.Model):
    id_usuario  =   models.AutoField(primary_key=True)
    tipo = models.TextField(max_length=255)
    valor = models.IntegerField()
    cor = models.TextField(default='blank',max_length=255)
    gen = models.TextField(default='blank',max_length=255)
    forn = models.TextField(default='blank',max_length=255)
    
