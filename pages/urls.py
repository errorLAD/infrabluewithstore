from django.urls import path
from . import views


urlpatterns = [
    path('homeworker/', views.homeworker, name='homeworker'),
    path('contact', views.contact, name='contact'),
]