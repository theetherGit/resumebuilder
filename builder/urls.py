from django.urls import path
from .views import home, signup, loginuser, logoutuser, dashboard


urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('login/', loginuser, name="login"),
    path('logout/', logoutuser, name="logout"),
    path('dashboard', dashboard, name="dashboard"),
]
