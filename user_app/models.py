from django.db import models
from datetime import date

class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='სახელი')
    last_name = models.CharField(max_length=100, verbose_name='გვარი')
    birth_date = models.DateField(verbose_name='დაბადების თარიღი')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or \
           (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age