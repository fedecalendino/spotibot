from rest_framework import serializers


class UpdatePlaylistSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    ids = serializers.ListField(child=serializers.CharField())
