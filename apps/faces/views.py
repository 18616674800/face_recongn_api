from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from .serializers import FaceInfoSerializer,FaceInfoNoSetsSerializer
from .models import FaceInfo
from django.conf import settings
import face_recognition
import numpy as np
import time
try:
    from PIL import Image, ImageFilter
except ImportError:
    import Image
    import ImageFilter
import cv2
import os

# Create your views here.


class FaceInfoPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class FaceInfoViewSet(viewsets.ModelViewSet):
    """
    人脸库的新增，删除，修改，查看
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = FaceInfo.objects.all()
    pagination_class = FaceInfoPagination
    # authentication_classes = (TokenAuthentication, )
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_class = FaceSetsFilter
    search_fields = ('name', 'faceset', )
    ordering_fields = ('add_time',)

    def get_serializer_class(self):
        if self.action == "list":
            return FaceInfoSerializer
        elif self.action == "create":
            return FaceInfoNoSetsSerializer

        return FaceInfoSerializer
