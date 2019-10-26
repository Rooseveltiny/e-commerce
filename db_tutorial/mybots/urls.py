from django.urls import path
from . import views

urlpatterns = [
    path('vk_bot/', views.perform_bot, name='vk_bot'),
    path('get_schedule/', views.get_schedule, name='get_schedule')
]