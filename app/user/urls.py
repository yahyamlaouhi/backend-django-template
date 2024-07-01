from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user import views

app_name = "user"


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/<str:role>/", views.GetAllUsersView.as_view(), name="get-users"),
    path(
        "users/<str:role>/<str:identifier>/",
        views.GetUserView.as_view(),
        name="get-user",
    ),
    path("seller/create/", views.CreateSellerView.as_view(), name="get-seller"),
    path("buyer/create/", views.CreateBuyerView.as_view(), name="create-buyer"),
    path(
        "users/<str:role>/<str:identifier>/update/",
        views.UpdateUserView.as_view(),
        name="update-user",
    ),
    path(
        "users/<str:role>/<str:identifier>/update/password/",
        views.UpdateUserPasswordView.as_view(),
        name="update-pwd-user",
    ),
    path(
        "user/<str:role>/<str:identifier>/delete/",
        views.DeleteUserView.as_view(),
        name="delete-user",
    ),
]
