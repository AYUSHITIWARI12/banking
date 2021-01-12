from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('', views.home, name='home'),
   path('viewcustomer', views.viewcustomer, name='viewcustomer'),
   path('about', views.about, name='about'),
   path('history', views.history, name='history'),
   path('login', views.login, name='login'),
   path('signup', views.signup, name='signup'),

]

