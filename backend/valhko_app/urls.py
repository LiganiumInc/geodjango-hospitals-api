from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(prefix="api/v1/valhko/adm0", viewset=ADM0ViewSet, basename="adm0")
router.register(prefix="api/v1/valhko/adm1", viewset=ADM1ViewSet, basename="adm1")
router.register(prefix="api/v1/valhko/adm2", viewset=ADM2ViewSet, basename="adm2")
router.register(prefix="api/v1/valhko/adm3", viewset=ADM3ViewSet, basename="adm3")
router.register(prefix="api/v1/valhko/adm4", viewset=ADM4ViewSet, basename="adm4")
router.register(prefix="api/v1/valhko/documents", viewset=DocumentViewSet, basename="documents")
router.register(prefix="api/v1/valhko/indices", viewset=IndiceViewSet, basename="indices")
router.register(prefix="api/v1/valhko/indicesvalues", viewset=IndiceValuesViewSet, basename="indicesvalues")


urlpatterns = router.urls