from django.urls import path
from .views import home, signup, login


urlpatterns = [
    path('', home, name="home"),
    path('signup', signup, name="signup"),
    path('login', login, name="signup"),
]
