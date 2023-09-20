from django.urls import path, include
from . import views
import os
app_name = 'login'
urlpatterns = [
    path('signup', views.signup,name='signup'), 
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name ="signout")
]