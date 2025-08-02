# profiles/urls.py

from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, LinkViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'links', LinkViewSet, basename='link')

urlpatterns = router.urls