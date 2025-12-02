from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def about(request):
    return render(request, 'recipes/about.html')

def add_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        cooking_time = request.POST.get('cooking_time')
        author_name = request.POST.get('author_name')
        image = request.FILES.get('image')
        image_url = request.POST.get('image_url')  # Новое поле
        
        if title and description and cooking_time:
            recipe = Recipe.objects.create(
                title=title,
                description=description,
                cooking_time=int(cooking_time),
                author_name=author_name or 'Аноним',
                image=image,
                image_url=image_url  # Сохраняем URL изображения
            )
            messages.success(request, 'Рецепт успешно добавлен!')
            return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, 'recipes/add_recipe.html')

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        recipe_title = recipe.title
        recipe.delete()
        messages.success(request, f'Рецепт "{recipe_title}" был успешно удален!')
        return redirect('recipe_list')
    
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})