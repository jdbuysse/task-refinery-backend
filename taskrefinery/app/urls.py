# from django.urls import path
# from app import views

# urlpatterns = [
#     path('tasks/', views.task_list),
#     path('tasks/<int:pk>/', views.task_detail),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('tasks/', views.task_list),
    path('tasks/<int:pk>', views.task_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)