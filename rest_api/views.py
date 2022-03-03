from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_api import serializers
from rest_api import models
from rest_api import permissions

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

    def put(self, request, pk=None):
        """Update an object	by PUT (replacing the entire object)"""
        # provide any logic you want for PUT request
        return Response({'method': 'PUT'})	

    def patch(self, request, pk=None):
        """Update an object by PATCH (partially update an object by providing necessary changes)"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class TestViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.TestSerializer

    def list(self, request):
        """Return the content in a manner similar to GET"""

        my_list = ['a', 'b', 'c', 'd', 'e']

        return Response({'message': 'These are example of list', 'my list': my_list})

    def create(self, request):
        """Create an example message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Retrieve an object by ID"""
        return Response({'http_method': 'Get'})

    def update(self, request, pk=None):
        """Update an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Partially update an object"""
        return Response({'http_response': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an object"""
        return Response({'http_method': 'DELETE'})


class TestModelViewSet(viewsets.ModelViewSet):
    """Create and update test object"""
    serializer_class = serializers.TestModelSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Create user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

