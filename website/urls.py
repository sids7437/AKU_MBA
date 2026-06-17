from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('faculty/', views.faculty, name='faculty'),

    path('notices/', views.notices, name='notices'),

    path('events/', views.events, name='events'),

    path('about/', views.about, name='about'),

    path('programme/', views.programme, name='programme'),

    path('contact/', views.contact, name='contact'),

]