from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=True)
    site = models.URLField(blank=True, null=False)

    def __str__(self):
        return f'({self.id}) {self.nome} '