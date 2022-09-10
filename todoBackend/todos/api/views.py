from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def getRoute(request):
    route = [
        '/api/token', 
        '/api/token/refresh'
    ]

    return Response(route) 