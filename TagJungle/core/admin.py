from django.contrib import admin
from core.models import MetaKey

# Register your models here.
class MetaKeyAdmin(admin.ModelAdmin):
    pass

admin.site.register(MetaKey, MetaKeyAdmin)