
from rest_framework.response import Response
from .models import User
from rest_framework import generics,viewsets
from .serializers import UserSerializer
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework.views import APIView


class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]




class hi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):



        return Response(template_name='hi.html')

