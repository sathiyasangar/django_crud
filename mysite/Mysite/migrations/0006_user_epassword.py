# Generated by Django 3.0.3 on 2020-02-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0005_remove_user_efiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='epassword',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
