from django.db import models



class Product(models.Model):
    TYPE_CHOICES = [
        ('meat', 'Meat'),
        ('dairy', 'Dairy'),
        ('eggs', 'Eggs'),
        ('fruits', 'Fruits'),
        ('vegetables', 'Vegetables'),
        ('pasta', 'Pasta/Grains'),
        ('drinks', 'Drinks'),
        ('fats', 'Fats'),
        ('breadstuff', 'Breadstuff'),
        ('nuts', 'Nuts'),
        ('fish', 'Fish'),
        ('mushrooms', 'Mushrooms'),
        ('misc', 'Misc'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    proteins = models.FloatField(verbose_name="Proteins per 100g")
    carbs = models.FloatField(verbose_name="Carbs per 100g")
    fats = models.FloatField(verbose_name="Fats per 100g")
    kcal = models.FloatField(verbose_name="Kcal per 100g")

    def __str__(self):
        return f'{self.name} ({self.type})'