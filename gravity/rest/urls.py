from django.conf.urls import include
from django.urls import path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import permissions

from rest.routers.auth import router as auth_router


class CoreSpectacularAPIView(SpectacularAPIView):
    custom_settings = {
        'TITLE': "GRAVITY API",
        'SCHEMA_PATH_PREFIX': "/api",
        'DESCRIPTION': 'Полный список api',
        'VERSION': '1.0.0'
    }
    patterns = [
        re_path(r'^api/', include('rest.urls')),
    ]
    permission_classes = [permissions.IsAuthenticated]
    serve_public = False


urlpatterns = [
    path('schema/', CoreSpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('auth/', include(auth_router.urls))
]
