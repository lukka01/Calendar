from django.http import JsonResponse
from django.views import View
from .models import User


class UserView(View):
    def get(self, request):
        user = User.objects.first()

        if user:
            data = {
                'სახელი': user.first_name,
                'გვარი': user.last_name,
                'ასაკი': user.age,
                'დაბადების_თარიღი': user.birth_date.strftime('%Y-%m-%d')
            }
        else:
            data = {
                'შეტყობინება': 'მომხმარებელი ვერ მოიძებნა'
            }

        return JsonResponse(data)