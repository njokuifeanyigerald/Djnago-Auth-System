from django.urls import path
from .views import loginUser, register, home, logoutUser


urlpatterns = [
    path('', home, name="home"),
    path('login/', loginUser, name="login"),
    path('register', register, name="register"),
    path('logout/',logoutUser , name="logout"),
]

