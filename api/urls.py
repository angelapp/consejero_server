from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'applicationConfiguration', views.ApplicationConfigurationView)


urlpatterns = [
    url(r'^applicationConfiguration/$', views.ApplicationConfigurationView.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.UsersView.as_view()),

]