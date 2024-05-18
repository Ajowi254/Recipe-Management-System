#tests.py
from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(title='Test Recipe', description='Just a test')

    def test_title_content(self):
        recipe = Recipe.objects.get(id=1)
        expected_object_name = f'{recipe.title}'
        self.assertEquals(expected_object_name, 'Test Recipe')
