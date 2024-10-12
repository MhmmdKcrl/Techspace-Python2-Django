from rest_framework import serializers

from recipes.models import Category, Recipe, Tags



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']



class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tags
        fields = ['id', 'name', 'created_at', 'updated_at']


class TagRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'name']


class CategoryRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class RecipeSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source='category.name')
    category = CategoryRecipeSerializer()
    tags = TagRecipeSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 
            'title', 
            'description', 
            'image', 
            'category', 
            'tags', 
            'author_fullname',
            'slug',
            'created_at',
            'updated_at',
            ]
        

class RecipeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            'id', 
            'title', 
            'description', 
            'image', 
            'category', 
            'tags', 
            'author'
            ]