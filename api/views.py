from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': 'api/project-list/',
        'Detail View': 'api/project-detail/<str:pk>/',
        'Create': 'api/project-create/',
        'Update': 'api/project-update/<str:pk>/',
        'Delete': 'api/project-delete/<str:pk>/',
        '--------': 'Model Fields listed below -------',

        "id": 32,
        "project": "example_name",
        "description": "example descroption",
        "image": 'null',
        "project_url": "example.com"

    }

    return Response(api_urls)


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project_detail(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def project_create(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def project_update(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=projects, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def project_delete(request, pk):
    projects = Project.objects.get(id=pk)
    projects.delete()

    return Response('Item deleted successfully')
