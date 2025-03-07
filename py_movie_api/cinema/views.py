from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CinemaHall
from .serializers import CinemaHallSerializer


@api_view(['GET'])
def cinema_halls_list(request):
    cinema_halls = CinemaHall.objects.all()
    serializer = CinemaHallSerializer(cinema_halls, many=True)
    return Response(serializer.data)
