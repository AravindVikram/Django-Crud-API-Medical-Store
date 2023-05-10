from django.urls import path

from . import views
from . import views


urlpatterns = [
    path("signup/", views.Signup, name="signup"),    
    path("login/", views.Login, name="login"), 
    path("logout/", views.Logout, name="logout"), 
    path('', views.List, name='list'),
    path('create', views.Create, name='create'),
    path('update/<int:id>', views.Update, name='update'),
    path('delete/<int:id>', views.Delete, name='delete'),
    
]