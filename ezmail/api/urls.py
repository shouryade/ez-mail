from django.contrib import admin
from django.urls import path
import core.views as core_views

urlpatterns = [
    path("users/", core_views.get_users, name="get_users"),
    path("users/create/", core_views.create_user, name="create_user"),
]
