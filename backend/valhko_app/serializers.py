from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import *


class ADM0Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = ADM0
        geo_field = "adm_geom"
        fields = "__all__"

class ADM1Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = ADM1
        geo_field = "adm_geom"
        fields = "__all__"

class ADM2Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = ADM2
        geo_field = "adm_geom"
        fields = "__all__"

class ADM3Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = ADM3
        geo_field = "adm_geom"
        fields = "__all__"

class ADM4Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = ADM4
        geo_field = "adm_geom"
        fields = "__all__"

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class IndiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Indice 
        fields = "__all__"

class IndiceValuesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = IndiceValues
        fields = "__all__"