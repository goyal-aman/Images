from rest_framework import serializers

# local imports
from timeline.models import Card
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card 
        fields = ['text', 'date']