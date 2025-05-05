from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()

router.register(
    prefix="projects",
    viewset=ProjectViewSet,
    basename="projects",
)

urlpatterns = router.urls