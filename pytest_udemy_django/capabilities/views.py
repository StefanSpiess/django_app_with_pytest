from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class ProjectViewSet(ModelViewSet):
    "ModeViewSet for Project model"

    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
