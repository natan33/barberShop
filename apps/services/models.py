from django.db import models


class Service(models.Model):
    name = models.CharField('Nome do serviço', max_length=100)
    price = models.DecimalField(
        'Preço',
        max_digits=8,
        decimal_places=2
    )

    duration_minutes = models.PositiveIntegerField(
        "Duração (minutos)"
    )

    is_active = models.BooleanField(
        "Ativo",
        default=True
    )

    created_at = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em',
        auto_now=True
    )

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural ="Serviços"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - R$ {self.price}"
    
    