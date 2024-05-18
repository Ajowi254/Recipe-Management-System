#urls.py
from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new/', views.RecipeCreateView.as_view(), name='recipe_new'),
    path('recipe/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]
