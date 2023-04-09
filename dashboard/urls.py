from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
      path('dashboard', views.dashboard, name='dashboard'),
      path('dashboard_delete/<int:id>/', views.dashboard_delete, name='projectdetails_delete'),
      path('country', views.country, name='country'),
      path('Country_language', views.Country_language, name='Country_language'),
      path('', views.index, name='index'),
      path('search',views.search, name='search')
]