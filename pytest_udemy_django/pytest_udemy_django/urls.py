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
from django.urls import path, include, reverse
from django.http import HttpResponse
from django.utils.html import format_html
from rueruprechner.urls import my_router as rueruprechner_router
from capabilities.urls import router as capabilities_router


def api_root(request):
    links = [
        format_html('<li><a href="{}">{}</a></li>', reverse(pattern.name), pattern.name)
        for pattern in urlpatterns
        if hasattr(pattern, 'name') and pattern.name
    ]

    # Add top-level links manually for routers
    top_level_links = [
        format_html('<li><a href="/admin/">Admin</a></li>'),
        format_html('<li><a href="/rueruprechner/">Ruerup Rechner</a></li>'),
        format_html('<li><a href="/capabilities/">Capabilities</a></li>'),
    ]

    return HttpResponse(
        format_html(
            "<h1>Welcome to the API Root</h1><ul>{}</ul>",
            format_html("".join(top_level_links))
        )
    )


urlpatterns = [
    path("", api_root, name="api-root"),
    path("admin/", admin.site.urls),
    path("rueruprechner/", include(rueruprechner_router.urls)),
    path("capabilities/", include(capabilities_router.urls)),
]
