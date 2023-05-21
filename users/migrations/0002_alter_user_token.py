# Generated by Django 4.2.1 on 2023-05-20 11:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default=uuid.uuid4, max_length=128, unique=True),
        ),
    ]