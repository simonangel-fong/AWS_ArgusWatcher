from django.urls import path
from .views import BlogCreateView, BlogListView

app_name = "Blog"
urlpatterns = [
    path("list/", BlogListView.as_view(), name="list"),
    path("create/", BlogCreateView.as_view(), name="create"),
]
