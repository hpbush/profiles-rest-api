from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
            
        