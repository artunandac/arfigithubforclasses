from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:sinif>/', views.index, name='index'),
    path('<str:sinif>/about/', views.about, name='about'),
]