from django.contrib import admin
from django.urls import path
from cinema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cinema-halls/', views.cinema_halls_list),
    path('', views.home),
]
