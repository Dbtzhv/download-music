from django.urls import path
from users.views import UserView


app_name = 'users'

urlpatterns = [
    path('create_user/', UserView.as_view())
]
