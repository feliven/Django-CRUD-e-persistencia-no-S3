from django.db import models

from datetime import datetime

from django.contrib.auth.models import User


def upload_to_date(instance, filename):
    # Uses the date provided in data_fotografia, or fallback to current datetime
    date = instance.data_fotografia or datetime.now()
    return date.strftime(f"fotos/%Y/%m/%d/{filename}")


class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to=upload_to_date, blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name="user"
    )

    def __str__(self):
        return self.nome
