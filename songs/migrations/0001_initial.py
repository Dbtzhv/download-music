# Generated by Django 4.2.1 on 2023-05-20 12:31

from django.db import migrations, models
import django.db.models.deletion
import songs.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_user_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.CharField(max_length=128)),
                ('song_mp3', models.FileField(upload_to='songs/', validators=[songs.services.validate_mp3_file])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
