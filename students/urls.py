from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='students_list'),
    path('create/', views.student_create, name='student_create'),
    path('<int:id>/', views.student_detail, name='students_detail'),
    path('<int:id>/edit/', views.student_update, name='student_update'),
    path('<int:id>/delete/', views.student_delete, name='student_delete'),
]