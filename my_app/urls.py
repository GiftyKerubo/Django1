from django.urls import path
from my_app import views


urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),


]