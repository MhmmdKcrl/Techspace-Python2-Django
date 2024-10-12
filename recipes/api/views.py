from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from recipes.models import Category, Tags, Recipe
from recipes.api.serializers import CategorySerializer, TagSerializer, RecipeSerializer, RecipeCreateSerializer


def categories(request):
    category_list = Category.objects.all()

    # data = []
    # for i in category_list:
    #     data.append({
    #         "id": i.id,
    #         "name": i.name
    #     })
    # return JsonResponse(data, safe=False)

    serializer = CategorySerializer(category_list, many=True)
    return JsonResponse(serializer.data, safe=False)



def tags(request):
    tags_list = Tags.objects.all()
    serializer = TagSerializer(tags_list, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def recipes(request):
    recipe_list = Recipe.objects.all()

    if request.method == "POST":
        serializer = RecipeCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status = 403)

    serializer = RecipeSerializer(recipe_list, many=True,  context = {'request': request})
    return JsonResponse(serializer.data, safe=False, status=200)



class RecipeListCreateView(ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = RecipeCreateSerializer
        return self.serializer_class


@api_view(['PUT', 'PATCH'])
def recipe_update(request, pk):
    recipe = Recipe.objects.get(id = pk)

    if request.method == "PUT":
        serializer = RecipeCreateSerializer(data = request.data, instance = recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
    
    elif request.method == "PATCH":
        serializer = RecipeCreateSerializer(data = request.data, instance = recipe, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    return JsonResponse(serializer.data, safe=False)



class RecipeUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()
    allowed_methods = ['PUT', 'PATCH', 'GET', 'DELETE']
    permission_classes = [IsAuthenticatedOrReadOnly]

