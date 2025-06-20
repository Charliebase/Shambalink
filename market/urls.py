from django.urls import path
from . import views

urlpatterns = [
    path('', views.produce_list, name='produce_list'),
]
