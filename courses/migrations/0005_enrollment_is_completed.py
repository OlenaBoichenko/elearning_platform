# Generated by Django 5.1.2 on 2024-11-24 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_lessoncompletion'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]