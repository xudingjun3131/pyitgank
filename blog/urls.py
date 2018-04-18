from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', blog_title, name='blog_title'),
]