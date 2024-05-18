#views.py
from django.views import generic
from .models import Recipe
from django.urls import reverse_lazy


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search', '')
        if search_term:
            queryset = queryset.filter(title__icontains=search_term)
        return queryset

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

class RecipeCreateView(generic.CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['title', 'description', 'ingredients', 'cooking_instructions', 'difficulty_level']

class RecipeUpdateView(generic.UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['title', 'description', 'ingredients', 'cooking_instructions', 'difficulty_level']

class RecipeDeleteView(generic.DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes')
