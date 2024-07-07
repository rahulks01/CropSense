from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('temp/', views.temp, name='temp'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.crop_record, name='record'),
    path('delete_record/<int:pk>', views.delete_crop_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('weather/', views.weather, name='weather'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommend/<str:location>/', views.recommend_crops, name='recommend_crops'),
]