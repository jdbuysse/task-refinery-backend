from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>', views.TaskDetail.as_view()),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)