from rest_framework import routers
from .views import ChannelViewSet

router = routers.SimpleRouter()
router.register(r'channels', ChannelViewSet)

urlpatterns = router.urls
