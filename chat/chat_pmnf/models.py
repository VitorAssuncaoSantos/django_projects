from django.db import models
from django.contrib.auth.models import User, Group
# Create your models

class Sala(models.Model):
    nome = models.CharField(max_length=50)
    participante = models.ManyToManyField(User, blank=True)
    grupo = models.ForeignKey(Group, verbose_name="Group", null=True, on_delete=models.CASCADE)

class Messagem(models.Model):
    user = models.ForeignKey(User, verbose_name ="Usuario", on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, verbose_name="sala", on_delete=models.CASCADE)
    conteudo = models.TextField("Mensagem")
    dt_inclusao = models.TimeField("", auto_now=False, auto_now_add = True)


