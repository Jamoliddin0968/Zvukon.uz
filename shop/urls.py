from django.urls import path
from . import views
urlpatterns = [
    path("",views.productList,name="home"),
    path("categories/<int:pk>/", views.categoryDetail, name="categoryDetail"),
    path("subcategories/<int:pk>/", views.subcategoryDetail, name="subcategoryDetail"),
    path("detail/<int:pk>/",views.productDetail,name="productDetail"),
    path("search/",views.search,name="search"),
    path("about/",views.about,name="about"),
    path("adress/",views.adress,name="adress")
]
