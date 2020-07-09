from rest_framework.generics import ListAPIView

from home.models import Banner,Nav
from home.serializers import BannerModelSerializer,NavModelSerializer

from BZedu_api.settings.constants import BANNER_LENGTH, NAV_LENGTH

class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")[:BANNER_LENGTH]
    serializer_class = BannerModelSerializer
class NavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False).order_by("orders")[:NAV_LENGTH]
    serializer_class = NavModelSerializer

