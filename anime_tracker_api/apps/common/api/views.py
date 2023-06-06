from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


# Create your api here.
class JoinRoom(GenericAPIView):
    def get(self, request, *args, **kwargs):
        print(request)
        return Response(data={'message': 'RED'})
