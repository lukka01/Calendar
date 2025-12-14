from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'age', 'created_at')
    search_fields = ('first_name', 'last_name')

    def age(self, obj):
        return obj.age
    age.short_description = 'ასაკი'