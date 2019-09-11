from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
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