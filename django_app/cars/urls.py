from django.urls import path
from . import views  #importing our view file 


urlpatterns = [
    path("", views.car_details, name="car_details"),
    path("cars/<int:pk>/", views.car_detail, name="car_detail"),
]