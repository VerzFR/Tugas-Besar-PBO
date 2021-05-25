from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="home"),
    url(r'^akuns/', include("akuns.urls")),
    url(r'^profile/', include("profiles.urls")),
    url(r'^admins/', include("admins.urls"))
]
