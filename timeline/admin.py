from django.contrib import admin 
from timeline.models import Card 

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass 