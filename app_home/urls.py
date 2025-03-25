from django.urls import path
from app_home.views import *

urlpatterns = [
    path('', home, name='home')
]