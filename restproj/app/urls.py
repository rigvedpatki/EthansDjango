from django.conf.urls import url
from rest_framework import routers
from app.views import StudentViewSet, UniversityViewSet

app_name = 'app'

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls
