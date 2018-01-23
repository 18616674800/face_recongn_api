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
from django.conf import settings
from django.http import QueryDict
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

from .serializers import CompareResultsSerializer,CompareResultsCreateSerializer
from .models import CompareResults
from faces.models import FaceInfo
# Create your views here.


def compare_faces_tolerance(known_face_encodings, face_encoding_to_check):
    """
    Compare a list of face encodings against a candidate encoding to see if they match.

    :param known_face_encodings: A list of known face encodings
    :param face_encoding_to_check: A single face encoding to compare against the list
    :return tolerance: How much distance between faces to consider it a match. Lower is more strict. 0.6 is typical best performance.
    """
    return face_recognition.face_distance(known_face_encodings, face_encoding_to_check)


def str_to_list_float(str):
    str = str.strip().strip('[]')
    list_str = str.split(",")
    list_float = []
    for li in list_str :
        list_float.append(float(li))
    return list_float



class CompareFacesViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    搜索并进行人脸库比对
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = CompareResults.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CompareResultsSerializer
        elif self.action == "create":
            return CompareResultsCreateSerializer

        return CompareResultsSerializer


    def create(self, request, *args, **kwargs):
        datas = request.data.copy()
        start = time.clock()
        compare_result_id = []
        compare_result_name = []
        compare_result_tolerance = []
        np.set_printoptions(precision=30, suppress=True)
        for FaceInfos in FaceInfo.objects.filter(faceset=datas['faceset']).values("id","name","face_encode"):
            face_encoding = np.array(str_to_list_float(FaceInfos['face_encode']))
            search_image_encoding = np.array(str_to_list_float(datas['search_encode']))
            compare_result_id.append(FaceInfos['id'])
            compare_result_name.append(FaceInfos['name'])
            compare_result_tolerance.append(compare_faces_tolerance([face_encoding], search_image_encoding).tolist()[0])
        min_compare_result_tolerance = min(compare_result_tolerance)
        datas['related_name'] = compare_result_name[compare_result_tolerance.index(min_compare_result_tolerance)]
        datas['related_face'] = compare_result_id[compare_result_tolerance.index(min_compare_result_tolerance)]
        datas['tolerance'] = min_compare_result_tolerance
        end = time.clock()
        response_time = end - start
        datas['response_time'] = response_time
        serializer = self.get_serializer(data=datas)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):

        serializer.save()