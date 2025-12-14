from django.db import models

class Calendar(models.Model):
    year = models.IntegerField(verbose_name="წელი")
    month = models.IntegerField(verbose_name="თვე")
    day = models.IntegerField(verbose_name="დღე")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.year}--{self.month:02d}--{self.day:02d}'



