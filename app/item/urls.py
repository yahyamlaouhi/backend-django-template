from django.urls import include, path
from rest_framework.routers import DefaultRouter

from item import views

app_name = "item"


router = DefaultRouter()
router.register("items", views.ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
