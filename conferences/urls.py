from django.urls import path
from . import views

urlpatterns = [
    path('', views.conference_list, name='conference_list'),
    path('conference/<int:pk>/', views.conference_detail, name='conference_detail'),
]