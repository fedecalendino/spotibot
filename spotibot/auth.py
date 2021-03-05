from django import conf
from rest_framework.permissions import BasePermission


class ValidateApiKey(BasePermission):
    def has_permission(self, request, view):
        return request.query_params.get("api_key") == conf.settings.API_KEY
