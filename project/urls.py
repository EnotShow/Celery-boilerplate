from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Neobis test",
        default_version='v1',
        description="Neobis test REST API",
        license=openapi.License(name="Apache License 2.0"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

swagger_info = schema_view.with_ui('swagger', cache_timeout=0)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', swagger_info, name='swagger'),

    path('api/v1/', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
