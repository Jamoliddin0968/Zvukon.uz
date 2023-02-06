from django.db import models
from django.conf import settings
import os
from uuid import uuid4
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from PIL import Image
import PIL
from imagekit.models import ImageSpecField
from pilkit.processors import *
from django.conf import settings
def rename_product_image(instance, filename,upload_to = 'product-image'):
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
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        #db_table = "Kategoriya"
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("nomi"))
    price = models.FloatField(default=0, verbose_name=_("narxi"))
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("kategoriya"))
    description = models.TextField(verbose_name=_("ta'rifi"))
    characteristic = models.TextField(verbose_name=_("xarakteristikasi"),null=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Maxsulot")
        verbose_name_plural = _("Maxsulotlar")
    @property
    def small_image(self):
        return  self.image_set.first().image_small.url
    
    @property
    def medium_images(self):
        lst = [ i.image_medium.url for i in self.image_set.all()[:4]]
        while len(lst) < 4:
            lst.append(None)
        return lst


class Image(models.Model):
    image = models.ImageField(
        upload_to=rename_product_image, verbose_name=_("rasm"), max_length=150)
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name=_("Maxsulot"))

    image_small = ImageSpecField(
        source='image',
        processors=[Resize(719, 791)],
        format='JPEG',  
        options={'quality': 100}
    )
    image_medium = ImageSpecField(
        source='image',
        processors=[Resize(774,800)],
        format='JPEG',
        options={'quality': 100}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.product.name+' ' + self.image.url
    
    class Meta:
        verbose_name = _("Rasm")
        verbose_name_plural = _("Rasmlar")
