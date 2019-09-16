from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index_page'),
    path('login', views.Login.as_view(), name='login'),
]
