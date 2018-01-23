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

from .serializers import FaceSetsSerializer
from .models import FaceSets
from .filters import FaceSetsFilter
# Create your views here.


class FaceSetsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class FaceSetsViewSet( viewsets.ModelViewSet):
    """
    人脸库的新增，删除，修改，查看
    """
    # throttle_classes = (UserRateThrottle, )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = FaceSets.objects.all()
    serializer_class = FaceSetsSerializer
    pagination_class = FaceSetsPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = FaceSetsFilter
    search_fields = ('name', 'desc', )
    ordering_fields = ('add_time',)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.click_num += 1
    #     instance.save()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)