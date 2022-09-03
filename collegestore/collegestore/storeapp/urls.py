from . import views
from django.urls import path

app_name = 'storeapp'

urlpatterns = [

    path('', views.home, name='home'),
    path('order/',views.order,name='order'),
    path('ajax/load_courses/', views.load_courses, name='ajax_load_courses'),
]