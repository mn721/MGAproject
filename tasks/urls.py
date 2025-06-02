from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskHistoryViewSet, UserRegisterView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'task-history', TaskHistoryViewSet, basename='taskhistory')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterView.as_view(), name='user-register'),
]