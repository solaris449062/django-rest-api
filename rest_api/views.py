from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):
    """Test API VIEW"""

    def get(self, request, format=None):
        """Returns response examples"""
        example = ['a', 'b', 'c', 'd', 'e']

        return Response({'testA': 'a', 'testB': example})
# Create your views here.
