from django.urls import path
from . import views

urlpatterns = [
    path('stopwatch/', views.stopwatch, name='stopwatch'),
]