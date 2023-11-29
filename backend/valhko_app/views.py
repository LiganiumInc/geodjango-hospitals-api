from rest_framework import status, viewsets
from rest_framework.response import Response


from .models import *
from .serializers import *


class ADM0ViewSet(viewsets.ModelViewSet):
    queryset = ADM0.objects.all()
    serializer_class = ADM0Serializer

class ADM1ViewSet(viewsets.ModelViewSet):
    queryset = ADM1.objects.all()
    serializer_class = ADM1Serializer

class ADM2ViewSet(viewsets.ModelViewSet):
    queryset = ADM2.objects.all()
    serializer_class = ADM2Serializer

class ADM3ViewSet(viewsets.ModelViewSet):
    queryset = ADM3.objects.all()
    serializer_class = ADM3Serializer

class ADM4ViewSet(viewsets.ModelViewSet):
    queryset = ADM4.objects.all()
    serializer_class = ADM4Serializer
    
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class IndiceViewSet(viewsets.ModelViewSet):
    queryset = Indice.objects.all()
    serializer_class = IndiceSerializer

class IndiceValuesViewSet(viewsets.ModelViewSet):
    queryset = IndiceValues.objects.all()
    serializer_class = IndiceValuesSerializer

