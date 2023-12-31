# Generated by Django 4.2.1 on 2023-06-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_profile_last_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_educator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
