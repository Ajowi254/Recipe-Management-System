#models.py
from django.db import models

class Recipe(models.Model):
    EASY = 'E'
    MEDIUM = 'M'
    HARD = 'H'
    DIFFICULTY_LEVELS = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    cooking_instructions = models.TextField()
    difficulty_level = models.CharField(
        max_length=2,
        choices=DIFFICULTY_LEVELS,
        default=EASY,
    )

    def __str__(self):
        return self.title
