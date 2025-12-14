from django.urls import path
from .views import UserView

app_name = 'user_app'

urlpatterns = [
    path('', UserView.as_view(), name='user'),
]