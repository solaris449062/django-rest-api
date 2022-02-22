from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_api import serializers

class TestAPIView(APIView):
    """Test API VIEW"""

    serializer_class = serializers.TestSerializer

    def get(self, request, format=None):
        """Returns response examples"""
        example = ['a', 'b', 'c', 'd', 'e']

        return Response({'testA': 'a', 'testB': example})

    def post(self, request):
        """post method"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)