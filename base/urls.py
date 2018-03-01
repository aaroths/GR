"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include

# Use include() to add paths from the play application
from django.conf.urls import include

urlpatterns = [
    path('GR/', include('GR.urls')),
    path('registration/', include('registration.urls')),
    path('admin/', admin.site.urls),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),]

#Below are patterns that this generates
#accounts/ login/ [name='login']
#accounts/ logout/ [name='logout']
#accounts/ password_change/ [name='password_change']
#accounts/ password_change/done/ [name='password_change_done']
#accounts/ password_reset/ [name='password_reset']
#accounts/ password_reset/done/ [name='password_reset_done']
#accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/ reset/done/ [name='password_reset_complete']

urlpatterns += [
    url('^', include('django.contrib.auth.urls')),
]

from django.views.generic import RedirectView
urlpatterns += [url(r'^$', RedirectView.as_view(url='/GR/', permanent=True)),]
