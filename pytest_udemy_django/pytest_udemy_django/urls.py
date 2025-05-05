"""
URL configuration for pytest_udemy_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rueruprechner.urls import my_router as rueruprechner_router
from capabilities.urls import router as capabilities_router


def api_root(request):
    return HttpResponse(
        "Welcome to the API Root. Available endpoints: /rueruprechner/, /capabilities/"
    )


urlpatterns = [
    path("", api_root, name="api-root"),
    path("admin/", admin.site.urls),
    path("rueruprechner/", include(rueruprechner_router.urls)),
    path("capabilities/", include(capabilities_router.urls)),
]
