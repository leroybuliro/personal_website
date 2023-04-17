from django.urls import path
from .views import LandpageView, BlogView, ArticleView, PodcastView, BlogPodView

app_name = "core"

urlpatterns = [
    path("", LandpageView, name="index"),
    path("home/", BlogPodView, name="home"),
    path("logs/", BlogView, name="blog"),
    path("logs/entry-<int:pk>/<slug:slug>/", ArticleView, name="article"),
    path("kubonga-show/", PodcastView, name="podcast"),
    # path("legal/", LegalView.as_view(), name="legal"),
]