# Generated by Django 3.0.3 on 2020-02-12 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0009_auto_20200212_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regis',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='regis',
            name='updated_at',
        ),
    ]
