from rest_framework import serializers

from face_sets.serializers import FaceSetsSerializer
from .models import FaceInfo


class FaceInfoSerializer(serializers.ModelSerializer):
    faceset = FaceSetsSerializer()

    class Meta:
        model = FaceInfo
        fields = "__all__"


class FaceInfoNoSetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaceInfo
        fields = "__all__"