from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('toggle/<int:pin_number>/', views.toggle, name='toggle'),
]