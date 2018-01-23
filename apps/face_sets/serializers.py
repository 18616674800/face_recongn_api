from rest_framework import serializers


from .models import FaceSets


class FaceSetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaceSets
        fields = "__all__"