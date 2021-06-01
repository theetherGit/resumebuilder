from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ether/', admin.site.urls),
    path('', include('builder.urls')),
]
