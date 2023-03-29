from django.contrib import admin
from .models import Product,Category,Image,SubCategory,HomePageImages,Items,Color
from modeltranslation.admin import TranslationAdmin

from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = "Zvukon.uz"
admin.site.site_title = admin.site.site_header
class ImageInline(admin.StackedInline):
    model = Image
    min_num = 1
    max_num = 4
 
class ItemsInline(admin.TabularInline):
    model = Items
    # min_num = 1
    extra = 1
    
class ColorInline(admin.TabularInline):
    model = Color
    # min_num = 1
    extra = 1
class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1
    list_display = ['name','category']
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name',"description"]
    search_fields = ['name']
    list_per_page = 10
    inlines=(SubCategoryInline,)
        

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name','price','subcategory','created_at','updated_at']
    list_display_links = ["name","price"]
    search_fields = ['name','description']
    inlines = (ItemsInline,ColorInline,ImageInline)
    list_per_page = 10



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


    