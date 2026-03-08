from django.contrib import admin

# Register your models here.
from stock.models import Stock
from stock.models import Currency


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name", "description")

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
