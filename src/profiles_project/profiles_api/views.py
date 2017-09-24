from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
    Test API View.
    """

    def get(self, request, format=None):
        """
        Returns a list of APIView features.
        """

        an_apiview = [
            'uses http methods as functions(get, post, patch, put, delete)',
            'similar to a traditional Django view',
            'gives you the most control over your logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
