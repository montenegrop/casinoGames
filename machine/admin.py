from django.contrib import admin

from machine.models import Machine


# Register your models here.


class MachineAdmin(admin.ModelAdmin):
    readonly_fields = ('roi',)


admin.site.register(Machine, MachineAdmin)
