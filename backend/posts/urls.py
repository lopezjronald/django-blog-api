from django.urls import path
# from .views import PostDetail, PostList, UserList, UserDetail
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

# urlpatterns = [
#     path("users/<int:pk>/", UserDetail.as_view()),
#     path("users/", UserList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("posts", PostViewSet, basename="posts")

urlpatterns = router.urls
