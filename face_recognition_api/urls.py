"""face_recognition_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
import xadmin
from face_recognition_api.settings import MEDIA_ROOT
from django.views.static import serve
from django.views.generic import TemplateView

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token




router = DefaultRouter()
from face_sets.views import FaceSetsViewSet
from faces.views import FaceInfoViewSet
from compare_face.views import CompareFacesViewSet
#FaceSets系列查询
router.register(r'FaceSets', FaceSetsViewSet, base_name="FaceSets")
#FaceInfo系列查询
router.register(r'FaceInfo', FaceInfoViewSet, base_name="FaceInfo")
#CompareFace系列查询
router.register(r'CompareFaces', CompareFacesViewSet, base_name="ComparesFace")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title="face_recognition")),

    #drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),

]
