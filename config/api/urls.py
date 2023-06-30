from django.urls import path
from . import views

urlpatterns = [
    path("cars", views.getCars, name="get_cars"),
    path("car/<str:pk>/get", views.getCar, name="get_car"),
    path("car/create", views.createCar, name="create_car"),
    path("car/<str:pk>/update", views.updateCar, name="update_car"),
    path("car/<str:pk>/delete", views.deleteCar, name="delete_car"),
    path("contact/", views.contact, name="contact"),
]
