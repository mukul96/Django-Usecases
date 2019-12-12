from . import views
from django.urls import path


urlpatterns = [
    path('index/<str:stringParameter>', views.index, name='index'),
    path('indexPost', views.indexPost, name='indexPost'),
   
   

]