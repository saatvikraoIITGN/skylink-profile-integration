from rest_framework import viewsets
from django.http import HttpResponse
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.views import exception_handler

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def index(request):
    return HttpResponse("Welcome to the SkyLink Profile Data Integration API")

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response