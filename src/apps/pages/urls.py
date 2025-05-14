from django.urls import path
from .views import HomePageView, AboutPageView, home_page_view

urlpatterns = [
        path("about/", AboutPageView.as_view(), name="about"),
        path("home/", home_page_view, name="home"),
        path("", HomePageView.as_view(), name="home"),
]
