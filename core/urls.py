from django.urls import path
from .views import LandpageView, HomepageView, BlogView, PostView

app_name = "core"

urlpatterns = [
    path("", LandpageView, name="index"),
    path("home/", HomepageView, name="home"),
    path("logs/", BlogView, name="blog"),
    path("logs/<int:pk>/<slug:slug>/", PostView, name="article"),
    # path("legal/", LegalView.as_view(), name="legal"),
]