from django.contrib import admin
from .models import Disorder
class DisorderAdmin(admin.ModelAdmin):
    list_display = ('orpha_code', 'name', 'symptoms')

admin.site.register(Disorder, DisorderAdmin)
