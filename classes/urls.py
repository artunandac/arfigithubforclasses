from django.urls import path
from . import views

urlpatterns = [
    path('<str:sinif>/', views.index, name='classindex'),
    path('<str:sinif>/index/', views.index, name='classindex'),
    path('<str:sinif>/about/', views.about, name='classabout'),
    path('<str:sinif>/classhata/', views.hatabildir, name='classhata'),
    # path('<str:sinif>/classhata/hatayatesekkur/', views.hatayatesekkur, name='classhatatesekkur'),


]