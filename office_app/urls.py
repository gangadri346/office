from django.urls import path

from django.urls import path
from .views import *

urlpatterns = [
    path("index/", index),
    path("create/",create),
    path("edit/<int:eid>/",edit),
    path("update/<int:eid>/",update),
    path("delete/<int:eid>/",delete),
]
