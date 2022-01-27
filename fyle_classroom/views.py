from rest_framework import generics
from rest_framework.response import Response

class BaseView(generics.GenericAPIView):
    def get(self, request):
        return Response({'status': 'ok'})
