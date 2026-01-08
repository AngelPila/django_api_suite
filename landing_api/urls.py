from django.urls import path

from landing_api.views import LandingAPI

urlpatterns = [
    path("index/", LandingAPI.as_view(), name="landing-index"),
]
