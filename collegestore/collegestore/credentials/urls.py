from . import views
from django.urls import path

app_name = 'credentials'

urlpatterns = [

    path('register/', views.register_request, name='register'),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]

