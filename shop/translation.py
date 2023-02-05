from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name","description")
    
@register(Color)
class ColorTranslationOptions(TranslationOptions):
    fields = ("name",)
    
@register(Product)
class ColorTranslationOptions(TranslationOptions):
    fields = ("name","description")
