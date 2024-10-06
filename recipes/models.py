from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

User = get_user_model()

class Date(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Date):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        ordering = ["-id"]
    

class Tags(Date):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"


class RecipeImages(Date):
    image = models.ImageField(upload_to="recipeimages/")
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.recipe.title

    class Meta:
        verbose_name_plural = "Recipe Images"
        verbose_name = "Recipe Image"


class Recipe(Date):
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to="recipeimages/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    tags = models.ManyToManyField(Tags, related_name="recipes")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Recipes"
        verbose_name = "Recipe"

    def get_absolute_url(self):
        return reverse_lazy("recipes:recipe_single_page", kwargs={"slug": self.slug})
        



class Favourites(Date):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="favourites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")

    def __str__(self):
        return f"{self.recipe.title} - {self.user.username}"
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Favourites"
