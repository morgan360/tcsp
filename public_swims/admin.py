from django.contrib import admin
from .models import PublicSwim, SwimSchedule, SwimPrice, AgeGroup


# Register your models here.
class SwimScheduleInline(admin.TabularInline):
    model = SwimSchedule


class SwimPriceInline(admin.TabularInline):
    model = SwimPrice


@admin.register(PublicSwim)
class PublicSwimAdmin(admin.ModelAdmin):
    inlines = [SwimScheduleInline]


@admin.register(SwimSchedule)
class SwimCustomerAdmin(admin.ModelAdmin):
    list_display = ('swim', 'start_time', 'end_time', 'day_of_week', 'num_places', 'active', 'prices')
    inlines = [SwimPriceInline]

    def prices(self, obj):
        return ", ".join([f"€{str(price.price)} {price.age_group}" for price in obj.prices.all()])

    prices.short_description = 'Prices'


# admin.site.register(PublicSwim)
admin.site.register(SwimPrice)
admin.site.register(AgeGroup)
