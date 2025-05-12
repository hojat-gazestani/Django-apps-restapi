from django.urls import path
from .views import PostPageView, PostList, PostDetail

urlpatterns = [
  path("<int:pk>/", PostDetail.as_view(), name="posts_detail"),
  path("", PostList.as_view(), name="posts_list"),
  path("list/", PostPageView.as_view(), name="posts"),
]
