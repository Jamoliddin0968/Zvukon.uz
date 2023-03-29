from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name","description")
    
    
@register(Product)
class ColorTranslationOptions(TranslationOptions):
    fields = ("name","description")


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)