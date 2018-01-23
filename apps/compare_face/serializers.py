from rest_framework import serializers

from face_sets.serializers import FaceSetsSerializer
from faces.serializers import FaceInfoNoSetsSerializer
from .models import CompareResults


class CompareResultsSerializer(serializers.ModelSerializer):
    faceset = FaceSetsSerializer()
    related_face = FaceInfoNoSetsSerializer()

    class Meta:
        model = CompareResults
        fields = "__all__"


class CompareResultsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompareResults
        fields = "__all__"