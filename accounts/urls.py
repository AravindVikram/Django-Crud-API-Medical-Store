# API urls
from .views import LoginAPI, LogoutAPI, RegisterAPI  
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),   
    path('logout/', LogoutAPI.as_view(), name='logout'),  
]



