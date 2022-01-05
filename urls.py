from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

app_name='crud'

router = routers.DefaultRouter()
router.register(r'students', ItemCrud, basename="students")
urlpatterns = [
    path("",include(router.urls)),
]
