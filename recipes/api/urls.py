from django.urls import path

from recipes.api.views import categories, tags, recipes, recipe_update, RecipeListCreateView, RecipeUpdateAPIView

urlpatterns = [
    path("cats/", categories, name = "categories"),

    path("tags/", tags, name = "tags"),

    # path('recipes/', recipes, name = "recipes"),
    path('recipes/', RecipeListCreateView.as_view(), name = "recipes"),

    # path('recipes/<int:id>/', recipe_update, name="recipe_update"),
    path('recipes/<int:pk>/', RecipeUpdateAPIView.as_view(), name="recipe_update")

]