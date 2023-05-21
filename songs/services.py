from django.forms import ValidationError


def validate_mp3_file(value):
    if not value.name.endswith('.mp3'):
        raise ValidationError("Invalid file format. Only MP3 files are allowed.")
