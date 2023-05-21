from django.db import models
from users.models import User
from songs.services import validate_mp3_file

import uuid


class Song(models.Model):
    song_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=128)
    token = models.CharField(max_length=128)
    song_mp3 = models.FileField(upload_to='songs/')
