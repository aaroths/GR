from django.conf.urls import url
from django.urls import path
from . import views
from . import views as core_views

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
]
