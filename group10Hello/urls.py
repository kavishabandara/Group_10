from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('funding', views.funding , name='funding'),
    path('info/<str:membername1>/', views.info, name='info'),
]