from django.urls import path, include

from SISO import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='sign-in'),
    path('signout/', views.signout, name='sign-out'),

]
