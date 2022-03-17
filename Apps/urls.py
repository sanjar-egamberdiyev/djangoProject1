from django.urls import path
from .views import HomePageView, Home2PageView, Home3PageView

urlpatterns = [
    path('home3/', Home3PageView.as_view(), name = 'home3'),
    path('home2/', Home2PageView.as_view(), name = 'home2'),
    path('', HomePageView.as_view(), name = 'home'),
]