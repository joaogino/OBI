from django.db import models

# Create your models here.
from django.db import models

class Niveis(models.TextChoices):
    NIVEL_JR = "Nivel_Jr", "Nível Jr"
    NIVEL_1 = "Nivel_1", "Nível 1"
    NIVEL_2 = "Nivel_2", "Nível 2"
    NIVEL_S = "Nivel_S", "Nível Sênior"

class Fases(models.TextChoices):
    FASE_1 = "Fase_1", "Fase 1"
    FASE_2 = "Fase_2", "Fase 2"
    FASE_3 = "Fase_3", "Fase 3"

class Anos(models.TextChoices):
    Ano2020 = "ANO2020", "2020"
    Ano2019 = "ANO2019", "2019"

class Videoaula(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.CharField(max_length=20, choices=Anos.choices)
    nivel = models.CharField(max_length=20, choices=Niveis.choices)
    fase = models.CharField(max_length=20, choices=Fases.choices)
    link_youtube = models.URLField()
    arquivo_codigo = models.FileField(upload_to='arquivos_codigo/', null=True, blank=True)
    thumb = models.ImageField(upload_to='thumbs/', null=True, blank=True)

    def __str__(self):
        return self.titulo