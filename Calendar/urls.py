"""
URL configuration for Calendar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse  # ← JSON-სთვის

def home(request):
    """მთავარი გვერდი - ხელმისაწვდომი URL-ების სია"""
    data = {
        'message': 'MyCalendar API',
        'endpoints': {
            'admin': '/admin/',
            'calendar': '/calendar/',
            'user': '/user/'
        }
    }
    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/', include('calendar_app.urls')),
    path('user/', include('user_app.urls')),
    path('', home),  # ← ეს დაამატე!
]