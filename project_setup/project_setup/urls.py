from django.contrib import admin
from django.urls import path
from app_luancarminatti import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('books/', views.books, name='books'),
    path('resume/', views.resume, name='resume'),
    path('admin/', admin.site.urls),    
]
