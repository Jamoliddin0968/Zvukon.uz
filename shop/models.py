from django.db import models
from django.conf import settings
import os
from uuid import uuid4
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.views import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


def rename_product_image(instance, filename):
    upload_to = 'product-image'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = 'temp{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name=_(
        "Kategoriya nomi"), null=True, blank=True)
    description = models.TextField(verbose_name=_(
        "Kategoriya tarifi"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        #db_table = "Kategoriya"
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")


class Color(models.Model):

    name = models.CharField(max_length=255, verbose_name=_("rangi"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        #db_table = "Rang"
        verbose_name = _("Rang")
        verbose_name_plural = _("Ranglar")


class Product(models.Model, HitCountMixin):
    name = models.CharField(max_length=255, verbose_name=_("nomi"))
    price = models.FloatField(default=0, verbose_name=_("narxi"))
    # count = models.IntegerField(default=0, verbose_name=_("soni"))
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("kategoriya"))
    # is_active = models.BooleanField(default=True, verbose_name=_("Aktivmi"))
    description = models.TextField(verbose_name=_("ta'rifi"))

    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("rangi"))
    hit_count_generic = GenericRelation(
        MODEL_HITCOUNT, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        #db_table = "Maxsulot"
        verbose_name = _("Maxsulot")
        verbose_name_plural = _("Maxsulotlar")
    
    def images(self):
        return [i.image.url for i in self.image_set.all()]


class Image(models.Model):
    image = models.ImageField(
        upload_to=rename_product_image, verbose_name=_("rasm"), max_length=150)
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name=_("Maxsulot"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.product.name+' ' + self.image.url
    
    class Meta:
        #db_table = "Rasm"
        verbose_name = _("Rasm")
        verbose_name_plural = _("Rasmlar")
