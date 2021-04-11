from . import views

from django.urls import path

app_name = "main"

urlpatterns = [
    path('home/translate/', views.translate, name="translate"),
    path('clear/', views.clear_sen, name="clear"),
]
