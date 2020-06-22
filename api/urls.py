from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('project-list/', views.project_list, name='project-list'),
    path('project-detail/<str:pk>/', views.project_detail, name='project-detail'),
    path('project-create/', views.project_create, name='project-create'),
    path('project-update/<str:pk>/', views.project_update, name='project-update'),
    path('project-delete/<str:pk>/', views.project_delete, name='project-delete'),

]