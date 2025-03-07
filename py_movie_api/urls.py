from django.urls import path
from py_movie_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cinema-halls/', views.cinema_halls_list),
    path('', views.home),
]
