from django.conf.urls import url
from polls import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^'),
    url(r'^'),
    url(r'^'),
    url(r'^')

]
