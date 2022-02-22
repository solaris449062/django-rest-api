from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    """Serializer example"""
    name = serializers.CharField(max_length=10)