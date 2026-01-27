from django.contrib import admin
from .models import Barber, BarberWorkingHour


class BarberWorkingHourInline(admin.TabularInline):
    model = BarberWorkingHour
    extra = 1

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    filter_horizontal = ("services",)
    inlines = [BarberWorkingHourInline]