import uuid

from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response


class ClientAuthViewSet(viewsets.ViewSet):
    serializer_class = None

    def list(self, request):
        session_id = request.COOKIES.get(
            settings.SESSION_ID_COOKIE,
            uuid.uuid4()
        )
        response = Response("OK")
        response.set_cookie(
            settings.SESSION_ID_COOKIE,
            session_id
        )
        return response
