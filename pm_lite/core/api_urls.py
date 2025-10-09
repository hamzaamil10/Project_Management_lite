from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet, UserViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'Projects', ProjectViewSet, basename='project')
router.register(r'Tasks', TaskViewSet, basename='task')
router.register(r'Comments', CommentViewSet, basename='comment')
router.register(r'Users', UserViewSet, basename='user')

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
    # API endpoints
    path('api/', include(router.urls)),
]