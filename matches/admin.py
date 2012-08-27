from django.contrib import admin
from matches import models

class PlayInline(admin.TabularInline):
    model = models.Play
    raw_id_fields = ('player','match',)

class MatchAdmin(admin.ModelAdmin):
    inlines = [
        PlayInline,
    ]
    raw_id_fields = ('game',)

admin.site.register(models.Match, MatchAdmin)
