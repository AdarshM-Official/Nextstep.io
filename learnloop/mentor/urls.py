from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentor_list, name='mentor_list'),
    path('<int:id>/', views.mentor_detail, name='mentor_detail'),
    path('<int:id>/book/', views.book_appointment, name='book_appointment'),
]
