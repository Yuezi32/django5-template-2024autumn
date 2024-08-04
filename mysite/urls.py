"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Django5教学API文档",
        default_version="v1",
        description="API文档说明",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# 欢迎信息
def welcome(request):
    return HttpResponse("Welcome to Django5")


urlpatterns = [
    path("", welcome),
    path("demo/", include("demo.urls")),
    path("account/", include("account.urls")),
]

# 仅在DEBUG=True情况下加载API文档和Django管理后台
if settings.DEBUG:
    urlpatterns += [
		path("admin/", admin.site.urls),
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ]
