from django.contrib import admin
from django.urls import path, include
from base_framework import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #test
    path('tests/', include('tests.urls')),
]
