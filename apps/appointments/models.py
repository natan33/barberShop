from django.db import models
from django.conf import settings
from datetime import timedelta


class AppointmentStatus(models.TextChoices):
    SCHEDULED = "scheduled", "Agendado"
    CONFIRMED = "confirmed", "Confirmado"
    CANCELLED = "cancelled", "Cancelado"
    COMPLETED = "completed", "Concluído"


class Appointment(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    barber = models.ForeignKey(
        "barbers.Barber",
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    service = models.ForeignKey(
        "services.Service",
        on_delete=models.PROTECT,
        related_name="appointments"
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.SCHEDULED
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_time"]
        indexes = [
            models.Index(fields=["barber", "start_time"]),
            models.Index(fields=["client", "start_time"]),
        ]

    def __str__(self):
        return f"{self.client} - {self.service} ({self.start_time:%d/%m %H:%M})"

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = self.start_time + timedelta(
                minutes=self.service.duration
            )
        super().save(*args, **kwargs)