from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('about/', views.about, name='about'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),  # Новый URL
    path('review/<int:pk>/delete/', views.delete_review, name='delete_review'),
]