from django.urls import path
from .views import CinemaHallListCreateView, CinemaHallRetrieveUpdateDestroyView

urlpatterns = [
    path("cinema-halls/", CinemaHallListCreateView.as_view(), name="cinema-hall-list-create"),
    path("cinema-halls/<int:pk>/", CinemaHallRetrieveUpdateDestroyView.as_view(), name="cinema-hall-detail"),
]
