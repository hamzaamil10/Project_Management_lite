from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet, UserViewSet

router = DefaultRouter()
router.register(r'Projects', ProjectViewSet)
router.register(r'Tasks', TaskViewSet)
router.register(r'Comments', CommentViewSet)
router.register(r'Users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]