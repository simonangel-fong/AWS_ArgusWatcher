from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('ec2/', include("AppEC2.urls")),
    path('admin/', admin.site.urls),
]
