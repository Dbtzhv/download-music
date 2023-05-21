from django.db import models
import uuid



class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    token = models.CharField(max_length=128, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=64)
