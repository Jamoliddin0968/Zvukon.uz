from django.shortcuts import render , get_object_or_404
from .models import Category , Product
from hitcount.utils import get_hitcount_model
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

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
    # cats = Category.objects.all().order_by("-name")
    new_products = Product.objects.all().order_by("-id")
    popular_products = Product.objects.all().order_by("id")
    
    context = {
        "new_products":new_products,
        "popular_products":popular_products
    }
    return render(request,"shop/index.html",context)


def productDetail(request,pk):
    object = get_object_or_404(Product, pk=pk)
    context = {}
    context["object"] = object
    popular_products = Product.objects.all().order_by("id")
    context["popular_products"] = popular_products
    return render(request,"shop/detail.html",context)


def categoryDetail(request,pk):
    cat = get_object_or_404(Category,pk=pk)
    new_products = cat.product_set.all().all().order_by("-id")
    popular_products = Product.objects.exclude(category=cat.id).order_by("id")
    cat_products = []
    lst = []
    for item in new_products:
        if len(lst) < 9:
            lst.append(item)
        else:
            cat_products.append(list(lst[:]))
            lst.clear()
    cat_products.append(list(lst[:]))
    context = {
         "cat_products":cat_products,
        "popular_products":popular_products,
        "cat_name":cat.name,
    }
    return render(request,"shop/cat.html",context)