from django.contrib import admin
from players import models

class PlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Player, PlayerAdmin)
