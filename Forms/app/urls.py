from django.conf.urls import url, include
from app import views

urlpatterns = [
    url(r'^formpage/', views.form_name_view, name="form_page")

]
