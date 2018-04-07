from django.conf.urls import url
from world_app.views import SayHello, SayWelcome

app_name = 'world_app'

urlpatterns = [
    url(r'^hello', SayHello, name='hello'),
    url(r'^welcome', SayWelcome, name='welcome')    
]