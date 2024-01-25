from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('input/', views.process_form, name='input_form'),
]
