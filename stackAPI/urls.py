from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("Data",views.DataApi)

urlpatterns=[
    path('stack',include(router.urls)),
    path("fetch",views.fetch,name="fetch")
]