from django.contrib import admin
from .models import BankAccount, Customer, Transfer
# Register your models here.

class BankAccountInline(admin.StackedInline):
    extra = 1
    model = BankAccount

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [BankAccountInline]
    list_display = ["user"]

admin.site.register(Transfer)