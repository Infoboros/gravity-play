from rest_framework import routers

from rest.viewsets.auth import ClientAuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'client', ClientAuthViewSet, basename='client')