from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

# Register your models here.

from .models import Tags, Category, Recipe, RecipeImages, Favourites

admin.site.register(RecipeImages)
# admin.site.register(Tags)
# admin.site.register(Category)
admin.site.register(Favourites)
# admin.site.register(Recipe)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]


@admin.register(Tags)
class TagsAdmin(TranslationAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]


class RecipeImagesInline(admin.TabularInline):
    model = RecipeImages
    extra = 4


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id","title",'slug', 'get_image', 'category', 'author','get_tags', "created_at", "updated_at"]
    list_display_links = ["id", "title", "get_image"]
    list_editable = ["category", "author", ]
    list_filter = ["category", "author", "tags"]
    # list_per_page = 2
    search_fields = ["title", "description"]
    inlines = [RecipeImagesInline]
    

    fieldsets = (
      ('Standard info', {
          'fields': ['title', 'description', 'image', 'slug']
      }),
      
      ('Relations', {
          'fields': ('category', 'tags', 'author')
      }),
    )


    def get_tags(self, obj):
        tags = obj.tags.all()
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = "Tags"
    
    
    def get_image(self, obj):
        if obj.image:
            image = f" <img src='{obj.image.url}' width='100' /> "
        
            return format_html(image)
        return "No Image"
    get_image.short_description = "Image"




