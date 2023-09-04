from rest_framework import routers
from .views import TodoViewSet, AccessLogViewSet

# created routers for the functionality of app1
router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet, basename = 'todos')
router.register(r'access-logs', AccessLogViewSet, basename = 'access_logs')

urlpatterns = router.urls