from django.urls import path
from assignment import views

urlpatterns = [
    path('assignment/', views.assignment_create),
    path('assignment/all/', views.all_assignments_list),
    path('assignment/<int:pk>/', views.assignment_rud),
    path('assignment/<int:pk>/submission/', views.submission_create),
    path('assignment/<int:pk>/submissions/', views.submissions_by_assignment_list),
    path('assignment/part/<str:part_name>/', views.assignments_by_part_list),
]