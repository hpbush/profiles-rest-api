from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as fucntion (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over application logic',
            'Is mapped manually to urls',
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Createa a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle update object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'patch'})
    
    def delete(self, request, pk=None):
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Hello message"""

        a_viewset = [
            'uses actions(list, retrieve, update, partial_update)',
            'automatically maps to urls using routers',
            'provides more functionallity with less code',
        ]

        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response(message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http method' : 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles partial update of object"""
        return Resposne({'method' : 'Patch'})
    
    def destroy(self, request, pk=None):
        """Handles deleting an object"""
        return Response({'method' : 'DELETE'})

    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'email']
