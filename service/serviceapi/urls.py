from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, OrderViewSet, ReviewViewSet

router = DefaultRouter()
router.register('services', ServiceViewSet)
router.register('orders', OrderViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls