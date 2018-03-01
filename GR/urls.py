from django.conf.urls import url
from django.urls import path
from . import views
from . import views as core_views

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^all/$', views.all, name='all'),
    url(r'^all2/$', views.all2, name='all2'),
    url(r'^resilience/$', views.resilience, name='resilience'),
    url(r'^emergency/$', views.emergency, name='emergency'),
    #tools
    url(r'^threePs/$', views.threePs, name='threePs'),
    url(r'^shutdown/$', views.shutdown, name='shutdown'),
    url(r'^reset/$', views.reset, name='reset'),
    url(r'^zero/$', views.zero, name='zero'),
    url(r'^keystone/$', views.keystone, name='keystone'),
    url(r'^littlewins/$', views.littlewins, name='littlewins'),
    url(r'^journal/$', views.journal, name='journal'),
    url(r'^chain/$', views.chain, name='chain'),
    url(r'^arrow/$', views.arrow, name='arrow'),
    url(r'^goal/$', views.goal, name='goal'),
    #activiy
    url(r'^label/$', views.label, name='label'),
    url(r'^keystone/$', views.keystone, name='keystone'),
    url(r'^ministry/$', views.ministry, name='ministry'),
    url(r'^space/$', views.space, name='space'),
    url(r'^threeselves/$', views.threeselves, name='threeselves'),
    url(r'^universes/$', views.universes, name='universes'),
    #Mindsets
    url(r'^compassion/$', views.compassion, name='compassion'),
    url(r'^curiosity/$', views.curiosity, name='curiosity'),
    url(r'^design/$', views.design, name='design'),
    url(r'^growth/$', views.growth, name='growth'),
    url(r'^mindfulness/$', views.mindfulness, name='mindfulness'),
    url(r'^vulnerability/$', views.vulnerability, name='vulnerability'),
]
