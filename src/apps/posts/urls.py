from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostPageView, PostList, PostDetail, UserViewSet,PostViewSet,  UserList, UserDetail

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

#router = SimpleRouter()
#router.register("users", UserViewSet, basename="users")
#router.register("posts", PostViewSet, basename="posts")
#router.register("", PostViewSet, basename="posts_llist")
#
#urlpatterns = router.urls

urlpatterns = [
  path("users/", UserList.as_view()),
  path("users/<int:pk>/", UserDetail.as_view()),
  path("<int:pk>/", PostDetail.as_view(), name="posts_detail"),
  path("", PostList.as_view(), name="posts_list"),
  path("list/", PostPageView.as_view(), name="posts"),
  path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'),name='redoc',),
  path('schema/swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
]
