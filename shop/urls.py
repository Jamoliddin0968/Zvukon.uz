from django.urls import path
from . import views
urlpatterns = [
    path("",views.productList,name="home"),
    path("categories/<int:pk>/", views.categoryDetail, name="categoryDetail"),
    path("detail/<int:pk>/",views.productDetail,name="productDetail")
]
