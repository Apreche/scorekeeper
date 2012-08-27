from django.contrib import admin
from games import models

class GameAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Game, GameAdmin)
