from django.urls import path

from main.apps import MainConfig
from main.views import HomeView

app_name = MainConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='prohome'),
]