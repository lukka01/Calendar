from django.http import JsonResponse
from django.views import View
from .models import Calendar


class CalendarView(View):
    def get(self, request):
        # აიღე პირველი კალენდარი ბაზიდან
        calendar = Calendar.objects.first()

        if calendar:
            data = {
                'წელი': calendar.year,
                'თვე': calendar.month,
                'რიცხვი': calendar.day,
                'თარიღი': str(calendar)
            }
        else:
            # თუ არ არის, მიმდინარე თარიღი
            from datetime import datetime
            now = datetime.now()
            data = {
                'წელი': now.year,
                'თვე': now.month,
                'რიცხვი': now.day,
                'თარიღი': now.strftime('%Y-%m-%d')
            }

        return JsonResponse(data)