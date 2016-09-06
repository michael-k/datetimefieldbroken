from django.contrib import admin

from main.models import Dummy


@admin.register(Dummy)
class DummyAdmin(admin.ModelAdmin):
    pass
