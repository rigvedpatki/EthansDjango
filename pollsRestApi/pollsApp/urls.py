from django.urls import path
from django.conf.urls import url
from .views import QuestionViewSet, OptionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet, base_name='questions')
router.register(r'options', OptionViewSet, base_name='options')

urlpatterns = router.urls
