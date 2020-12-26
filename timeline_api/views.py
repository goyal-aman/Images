from rest_framework import mixins, generics
# local import
from timeline.models import Card 
from timeline_api.serializers import CardSerializer

# Create your views here.

class CardList(
    mixins.ListModelMixin,
    generics.GenericAPIView):
    """
    APIView : return json response of all card objects
    """
    queryset = Card.objects.all().order_by('-date')
    serializer_class  = CardSerializer 

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
