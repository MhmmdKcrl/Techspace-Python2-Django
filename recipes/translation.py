from modeltranslation.translator import translator, TranslationOptions
from recipes.models import Category, Tags, Recipe


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class TagsTranslationOptions(TranslationOptions):
    fields = ('name',)


class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Tags, TagsTranslationOptions)
translator.register(Recipe, RecipeTranslationOptions)