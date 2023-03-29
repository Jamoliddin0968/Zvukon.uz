"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include 
from django.conf.urls.static import static
from django.conf import settings , urls
from django.conf.urls.i18n import i18n_patterns
from shop.views import set_language
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}



urlpatterns = [
    path("set_language/<str:language>", set_language, name="set-language"),
    path('i18n/',include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")), 
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path("",include("shop.urls")),
) 

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'shop.views.handler404'
