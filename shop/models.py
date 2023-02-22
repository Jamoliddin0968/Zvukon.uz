import os
from uuid import uuid4

import PIL
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from PIL import Image
from pilkit.processors import *

VIDEO_EXTENSIONS = ['mp4']
MAX_VIDEO_SIZE = 104857600  # 100 MB


def rename_product_image(instance, filename):
    upload_to = 'product-image'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = 'temp{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


VIDEO, IMAGE = ("Video", "Image")


class Category(models.Model):
    TYPES = ((VIDEO, VIDEO), (IMAGE, IMAGE))
    name = models.CharField(max_length=255, verbose_name=_(
        "Kategoriya nomi"), null=True, blank=True)
    description = models.TextField(verbose_name=_(
        "Kategoriya tarifi"), null=True, blank=True)
    image = models.ImageField(
        upload_to="category-image", verbose_name=_("Rasm"), help_text=_("rasm o'lchami 1920x1080 nisbatda bo'lishi kerak"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    video_file = models.FileField(upload_to='videos/', validators=[
        FileExtensionValidator(allowed_extensions=VIDEO_EXTENSIONS),
    ], null=True, blank=True,help_text=_("Video o'lchami 1920x1080 nisbatda bo'lishi kerak"))

    media = models.CharField(_("media"), max_length=10, help_text=_(
        "Asosiy sahifada rasm yoki video turishini tanlash"), default=IMAGE, choices=TYPES)

    image_fon = ImageSpecField(
        source='image',
        processors=[Resize(1920, 1080)],
        format='PNG',
        options={'quality': 100}
    )
    image_bg = ImageSpecField(
        source='image',
        processors=[Resize(1920, 1080)],
        format='PNG',
        options={'quality': 100}
    )
    def __str__(self) -> str:
        return self.name
    @property
    def subcats(self):
        return self.subcategory_set.all()
    class Meta:
        # db_table = "Kategoriya"
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")


class SubCategory(models.Model):
    name = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name=_("Subkategoriya nomi"))
    image = models.ImageField(upload_to="subcategory-images")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Kategoriya"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_fon = ImageSpecField(
        source='image',
        processors=[Resize(634, 740)],
        format='PNG',
        options={'quality': 100}
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("SubKategoriya")
        verbose_name_plural = _("SubKategoriyalar")


SOM, DOLLAR = ("so'm", "$")


class Product(models.Model):

    VALYUTA = (
        (SOM, "So'm"), (DOLLAR, "Dollar")
    )
    name = models.CharField(max_length=255, verbose_name=_("nomi"))
    value = models.FloatField(default=0, verbose_name=_("narxi"))
    currency = models.CharField(
        choices=VALYUTA, default=SOM, max_length=7, verbose_name=_("Valyutasi"))
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Kategoriya"))
    description = models.TextField(verbose_name=_("Ta'rifi"))
    characteristic = models.TextField(
        verbose_name=_("Xarakteristikasi"), null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    @property
    def small_image(self):
        return self.image_set.first().image_small.url

    @property
    def medium_images(self):
        lst = [i.image_medium.url for i in self.image_set.all()[:4]]
        while len(lst) < 4:
            lst.append(None)
        return lst

    @property
    def price(self):
        if self.currency == DOLLAR:
            return DOLLAR + " " + str(self.value)
        return str(self.value) + " " + SOM

    @property
    def categoryname(self):
        return self.subcategory.name

    class Meta:
        verbose_name = _("Maxsulot")
        verbose_name_plural = _("Maxsulotlar")


class Image(models.Model):
    image = models.ImageField(
        upload_to=rename_product_image, verbose_name=_("rasm"), max_length=150, help_text=_("Tavsiya etiladiogan rasm o'lchani 719x791"))
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name=_("Maxsulot"))

    image_small = ImageSpecField(
        source='image',
        processors=[Resize(719, 791)],
        format='PNG',
        options={'quality': 100}
    )
    image_medium = ImageSpecField(
        source='image',
        processors=[Resize(774, 800)],
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

class HomePageImages(models.Model):
    img = models.ImageField(_("Bosh mahsulotlar pastki qismidan chiqadigan rasm"), upload_to="settings/", height_field=1105, width_field=2533, max_length=None)
    is_active = models.BooleanField(_("Activligi"),default=False)
    
    def __str__(self) -> str:
        return self.img.url