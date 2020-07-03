from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

#having trouble with routers ATM
# router = routers.DefaultRouter()
# router.register('tasks', views.TaskList)
# router.register('users', views.UsersList)

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    # path('', include(router.urls)),
    path('tasks/<int:pk>', views.TaskDetail.as_view()),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('subtasks/', views.SubtaskList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)