from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_view, name='auth'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('mentor/dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
