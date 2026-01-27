from django.db import models
from apps.services.models import Service


class Barber(models.Model):
    name = models.CharField(
        "Nome do barbeiro",
        max_length=200
    )

    services = models.ManyToManyField(
        Service,
        related_name="barbers",
        verbose_name="Serviços",
        blank=True
    )

    is_active = models.BooleanField(
        "Ativo",
        default=True
    )

    created_at = models.DateTimeField(
        "Criado em",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        "Atualizado em",
        auto_now=True
    )

    class Meta:
        verbose_name = "Barbeiro"
        verbose_name_plural = "Barbeiros"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class BarberWorkingHour(models.Model):
    WEEK_DAYS = (
        (0, "Segunda"),
        (1, "Terça"),
        (2, "Quarta"),
        (3, "Quinta"),
        (4, "Sexta"),
        (5, "Sábado"),
        (6, "Domingo"),
    )

    barber = models.ForeignKey(
        Barber,
        on_delete=models.CASCADE,
        related_name="working_hours"
    )

    week_day = models.IntegerField(
        "Dia da semana",
        choices=WEEK_DAYS
    )

    start_time = models.TimeField("Início")
    end_time = models.TimeField("Fim")

    class Meta:
        verbose_name = "Horário de trabalho"
        verbose_name_plural = "Horários de trabalho"
        unique_together = ("barber", "week_day")

    def __str__(self):
        return f"{self.barber} - {self.get_week_day_display()}"