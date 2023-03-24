# Register your models here.
from django.contrib import admin
from .models import Player, NPC, Skill

admin.site.register(Player)
admin.site.register(NPC)
admin.site.register(Skill)
