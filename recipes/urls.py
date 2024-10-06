from django.urls import path

from recipes.views import recipes, recipe_single, stories, add_to_fav, remove_from_fav, RecipeList

app_name = "recipes"
urlpatterns = [
    # path("recipes/", recipes, name="recipes_page"),
    path("recipes/", RecipeList.as_view(), name="recipes_page"),

    path("recipes/<slug:slug>/", recipe_single, name="recipe_single_page"),

    path("add-to-fav/<int:id>/", add_to_fav, name="add_to_fav"),
    path("remove-from-fav/<int:id>/", remove_from_fav, name="remove_from_fav"),

    path("stories/", stories, name="stories_page"),
]


# http://127.0.0.1:8000/core/