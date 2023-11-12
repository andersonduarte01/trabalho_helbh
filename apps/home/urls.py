from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    #path('home', views.Home1.as_view(), name='index1'),
]
