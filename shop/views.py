from django.shortcuts import render , get_object_or_404
from .models import Category , Product,SubCategory , HomePageImages
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.core.paginator import Paginator
from django.db.models import Q , Count
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response

def productList(request):
    cats = Category.objects.annotate(num_cats=Count('subcategory__product')).filter(num_cats__gt=1).order_by("-id")[:5]
   
    slides = HomePageImages.objects.all()
    context = {
        "ftcats":cats,
        "slides":slides
    }
    return render(request,"shop/index.html",context)

def productDetail(request,pk):
    object = get_object_or_404(Product, pk=pk)
    popular_products = list(object.subcategory.product_set.all().order_by("-id")[:10])
    # if len(popular_products) < 10:
    #     for obj in object.subcategory.category.getProducts():
    #         if obj.subcategory!=object.subcategory:
    #             popular_products.append(obj)
    context ={
        "object":object,
        "popular_products":popular_products
    }
    # context["popular_products"] = popular_products
    return render(request,"shop/detail.html",context)

def categoryDetail(request,pk):
    cat = get_object_or_404(Category,pk=pk)
    subcats = cat.subcategory_set.all()
    products=[i for item in subcats for i in item.product_set.all()]
    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "subcats":subcats,
        "cat_name":cat.name,
        "currentcat":cat,
        "page_obj":page_obj
    }
    return render(request,"shop/cat.html",context)
    
def search(request):
    q = request.GET.get("query", "")
    if q and q!="":
        products=Product.objects.filter(Q(name_uz__icontains=q) | Q(name_ru__icontains=q))
    else:
        products = Product.objects.filter(id=0)
    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj":page_obj,
        "count":products.count(),
        "query":q,
    }
    return render(request,"shop/result.html",context)

def subcategoryDetail(request,pk):
    subcat = get_object_or_404(SubCategory,pk=pk)
    products=[i for i in subcat.product_set.all()]
    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "cat_name":subcat.name,
        "page_obj":page_obj,
        "currentcat":subcat.category,
    }
    return render(request,"shop/cat.html",context)

def handler404(request, exception):
    return render(request, 'page404.html', status=404)

def about(request):
    return render(request,"about.html")

def adress(request):
    return render(request,"adress.html")
def test(request):
    return render(request,"home.html")