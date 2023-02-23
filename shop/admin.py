from django.contrib import admin
from .models import Product,Category,Image,SubCategory,HomePageImages
from modeltranslation.admin import TranslationAdmin

from django.contrib.auth.models import Group

admin.site.unregister(Group)
class ImageInline(admin.StackedInline):
    model = Image
    min_num = 1
    max_num = 4
    
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name',"description"]
    search_fields = ['name']
    list_per_page = 10
        

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name','price','subcategory','created_at','updated_at']
    list_display_links = ["name","price"]
    search_fields = ['name','description']
    inlines = (ImageInline,)
    list_per_page = 10


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    
    list_display = ['image','product']
    list_per_page = 10
    
    def has_add_permission(self, request):
        return False
    


@admin.register(HomePageImages)
class ImageAdmin(admin.ModelAdmin):
    
    list_display = ['caption_text',"img"]
    list_display_links = ['caption_text',"img"]
    
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    list_display = ['name','category']
    search_fields = ['name']
    list_per_page = 10


    