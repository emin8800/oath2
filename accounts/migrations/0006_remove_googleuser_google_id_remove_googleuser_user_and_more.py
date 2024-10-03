# Generated by Django 5.1 on 2024-10-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googleuser',
            name='google_id',
        ),
        migrations.RemoveField(
            model_name='googleuser',
            name='user',
        ),
        migrations.AddField(
            model_name='googleuser',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
