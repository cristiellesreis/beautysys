from django.urls import path
from app_home.views import home, landing_page

urlpatterns = [
    path('landing_page', landing_page, name='landing_page'),
    path('home/', home, name='home'),
]