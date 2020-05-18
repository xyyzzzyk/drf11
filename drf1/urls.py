"""drf200 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path


from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r'video_new',views.VideoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<str:version>/test/', views.TestView.as_view()),
    path('api/<str:version>/course/', views.CourseView.as_view()),
    path('api/<str:version>/course/new/', views.CourseNewView.as_view()),
    path('api/<str:version>/course/crud/', views.CourseCrudView.as_view({'get': 'list', 'post': 'create'})),
    path('api/<str:version>/course/crud/<int:pk>/', views.CourseCrudView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    path('api/<str:version>/module/', views.ModuleView.as_view()),
    path('api/<str:version>/module/new/', views.ModuleNewView.as_view()),
    path('api/<str:version>/module/new/<int:pk>/', views.ModuleNewView.as_view()),
    path('api/<str:version>/module/set/', views.ModuleSetView.as_view({'get': 'list', 'post': 'create'})),
    path('api/<str:version>/module/set/<int:pk>/', views.ModuleSetView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    path('api/<str:version>/video/', views.VideoView.as_view()),
    path('api/<str:version>/video/<int:pk>/', views.VideoView.as_view()),
    path('api/<str:version>/',include(router.urls))
]














