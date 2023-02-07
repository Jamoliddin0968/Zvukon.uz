from django.contrib import admin
from .models import Product,Category,Image
from modeltranslation.admin import TranslationAdmin

from django.contrib.auth.models import Group

admin.site.unregister(Group)
class ImageInline(admin.StackedInline):
    model = Image
    min_num = 1
    max_num = 4
    
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name','created_at','updated_at']
    search_fields = ['name']
    list_per_page = 10
        

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name','price','category','created_at','updated_at']
    # list_editable = ['price','count','is_active','color']
    # list_filter = ['is_active']

    search_fields = ['name','description']
    inlines = (ImageInline,)
    list_per_page = 10


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    
    list_display = ['image','product']
    list_per_page = 10
    
    def has_add_permission(self, request):
        return False
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

    
