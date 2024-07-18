from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_obituaries, name='view_obituaries'),
    path('submit/', views.obituary_form, name='obituary_form'),
]
