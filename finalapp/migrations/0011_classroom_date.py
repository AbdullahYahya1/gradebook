# Generated by Django 4.2.3 on 2023-07-19 08:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0010_alter_classroom_subject_delete_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]