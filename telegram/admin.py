from django.contrib import admin
from telegram.models import update


class UpdateAdmin(admin.ModelAdmin):
    model = update
    list_display = ('id', 'fromid', 'fromLastName', 'fromFirstName', 'date', 'text', )
    list_filter = ('fromid', 'date', )

admin.site.register(update, UpdateAdmin)
