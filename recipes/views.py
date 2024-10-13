from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView

# Create your views here.

from .models import Recipe, Category, Favourites


class RecipeList(ListView):
    template_name = 'recipes.html'
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 1

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        recipes = context['recipes']
        sessions = self.request.session.get('favs', [])
        user = self.request.user
        if user.is_authenticated:
            for i in recipes:
                if Favourites.objects.filter(user=user, recipe=i).exists():
                    i.is_fav = True
                else:
                    i.is_fav = False
        else:
            for i in recipes:
                if i.id in sessions:
                    i.is_fav = True
                else:
                    i.is_fav = False
        context["categories"] = Category.objects.all()
        return context



def recipes(request):
    recipes = Recipe.objects.all()  # select * from recipes_recipe
    Recipe.objects.raw("select * from recipes_recipe")
    sessions = request.session.get('favs', [])
    print(sessions, "++++++++++++++")

    user = request.user
    if user.is_authenticated:
        for i in recipes:
            if Favourites.objects.filter(user=user, recipe=i).exists():
                i.is_fav = True
            else:
                i.is_fav = False
    else:
        for i in recipes:
            if i.id in sessions:
                i.is_fav = True
            else:
                i.is_fav = False
        

    context = {
        "recipes": recipes,
        # "categories": categories
    }

    return render(request, "recipes.html", context)


def recipe_single(request, slug):
    # recipe = Recipe.objects.get(id=id)
    # recipe = get_object_or_404(Recipe, id=id)
    recipe = get_object_or_404(Recipe, slug=slug)

    context = {
        "recipe": recipe
    }

    return render(request, "single.html", context)



def stories(request):
    return render(request, "stories.html")




def add_to_fav(request, id):
    user = request.user
    recipe = Recipe.objects.get(id=id)
    if user.is_authenticated:
        if not Favourites.objects.filter(user=user, recipe=recipe).exists(): 
            Favourites.objects.create(user=user, recipe=recipe)
            messages.add_message(request, messages.SUCCESS, "Recipe added to favourites")
        else:
            messages.add_message(request, messages.ERROR, "Recipe already in favourites")

    else:
        recipe = get_object_or_404(Recipe, id=id)
        sessions = request.session.get('favs', [])
        if not (recipe.id in sessions):
            sessions.append(recipe.id)
            request.session['favs'] = sessions
            # request.COOKIES['favs'] = sessions
            messages.add_message(request, messages.SUCCESS, "Recipe added to favourites")
        else:
            messages.add_message(request, messages.ERROR, "Recipe already in favourites")

        print(request.session['favs'], "------------")
        
        
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect("recipes:recipes_page")



# def remove_from_fav(request, id):
#     user = request.user
#     recipe = get_object_or_404(Recipe, id=id)
#     if user.is_authenticated:
#         if recipe:
#             if Favourites.objects.filter(user=user, recipe=recipe).exists():
#                 fav_recipe = Favourites.objects.get(user=user, recipe=recipe)
#                 fav_recipe.delete()
#                 messages.add_message(request, messages.INFO, "Recipe removed from favourites")
#             else:
#                 messages.add_message(request, messages.ERROR, "Recipe not in favourites")
#     else:
#         messages.add_message(request, messages.ERROR, "Recipe not in favourites")

#     return redirect("recipes:recipes_page")



# def add_to_fav(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     sessions = request.session.get('favs', [])
#     if not (recipe.id in sessions):
#         sessions.append(recipe.id)
#         request.session['favs'] = sessions
#         messages.add_message(request, messages.SUCCESS, "Recipe added to favourites")
#     else:
#         messages.add_message(request, messages.ERROR, "Recipe already in favourites")

#     print(request.session['favs'], "------------")
    
    
    
#     # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     return redirect("recipes:recipes_page")



def remove_from_fav(request, id):
    sessions = request.session.get('favs', [])
    recipe = get_object_or_404(Recipe, id=id)
    if sessions:
        if recipe:
            if recipe.id in sessions:
                sessions.remove(recipe.id)
                request.session['favs'] = sessions
                messages.add_message(request, messages.INFO, "Recipe removed from favourites")
            else:
                messages.add_message(request, messages.ERROR, "Recipe not in favourites")
        else:
            messages.add_message(request, messages.ERROR, "Recipe not in favourites")

    else:
        messages.add_message(request, messages.ERROR, "Recipe not in favourites")

    return redirect("recipes:recipes_page")


