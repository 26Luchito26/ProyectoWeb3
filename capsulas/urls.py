from django.urls import path

from . import views

urlpatterns = [
    path('capsulas/', views.capsulas, name="capsulas"),
]