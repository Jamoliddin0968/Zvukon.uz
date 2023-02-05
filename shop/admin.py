from django.contrib import admin
from .models import Product,Color,Category,Image
from modeltranslation.admin import TranslationAdmin

from django.contrib.auth.models import Group
from hitcount.models import Hit , HitCount , BlacklistIP,BlacklistUserAgent
import hitcount
admin.site.unregister(Group)
# admin.site.unregister(Hit)
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name','created_at','updated_at']
    search_fields = ['name']
    list_per_page = 10
        

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name','price','category','color','created_at','updated_at']
    # list_editable = ['price','count','is_active','color']
    # list_filter = ['is_active']

    search_fields = ['name','description']
    inlines = (ImageInline,)
    list_per_page = 10
    
@admin.register(Color)
class ColorAdmin(TranslationAdmin):
    list_display = ['name']
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10
    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image','product']
    list_per_page = 10
    
