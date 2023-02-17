from django.urls import path
from . import views
urlpatterns = [
    path("",views.productList,name="home"),
    path("categories/<int:pk>/", views.categoryDetail, name="categoryDetail"),
    path("subcategories/<int:pk>/", views.subcategoryDetail, name="subcategoryDetail"),
    path("detail/<int:pk>/",views.productDetail,name="productDetail"),
    path("home/",views.test),
]
