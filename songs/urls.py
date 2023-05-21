from django.urls import path
from songs.views import SongView


app_name = 'songs'

urlpatterns = [
    path('record/', SongView.as_view())
]
