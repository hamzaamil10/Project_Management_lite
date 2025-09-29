from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet, UserViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'Projects', ProjectViewSet)
router.register(r'Tasks', TaskViewSet)
router.register(r'Comments', CommentViewSet)
router.register(r'Users', UserViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
]