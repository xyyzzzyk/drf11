from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView
from rest_framework.viewsets import ModelViewSet


from api.serializers import CourseSerializer,ModuleSerializer,ModuleNewSerializer,ModuleSetSerializer,VideoSerializer
from api import models,serializers


# Create your views here.


class TestView(APIView):
    versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        # print(request.version)
        return Response('...')


class CourseView(APIView):
    versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        queryset = models.Course.objects.all()
        ser = CourseSerializer(instance=queryset, many=True)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        ser = CourseSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response('添加成功')
        return Response(ser.errors)


class CourseNewView(ListAPIView, CreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    # versioning_class = URLPathVersioning


class CourseCrudView(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class ModuleView(APIView):
    versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        queryset = models.Module.objects.all()
        ser = ModuleSerializer(instance=queryset, many=True)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        ser = ModuleSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response('添加成功')
        return Response(ser.errors)


class ModuleNewView(ListAPIView, CreateAPIView, RetrieveAPIView):
    queryset = models.Module.objects.all()
    serializer_class = ModuleNewSerializer


class ModuleSetView(ModelViewSet):
    queryset = models.Module.objects.all()
    serializer_class = ModuleSetSerializer


class VideoView(ListAPIView,RetrieveAPIView):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


class VideoViewSet(ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSetSerializer



