from django.db import models


class Expense(models.Model):

    CATEGORY_CHOICES = [
    ('TO_UNI', 'Going to University'),
    ('FROM_UNI', 'Coming from University'),
    ('LUNCH', 'Lunch'),
    ('OTHER', 'Other'),
    ]


    amount = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)
    note = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f"{self.category} - {self.amount}"