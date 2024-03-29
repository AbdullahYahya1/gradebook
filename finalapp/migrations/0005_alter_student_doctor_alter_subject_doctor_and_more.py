# Generated by Django 4.2.3 on 2023-07-19 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0004_doctor_student_subject_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subject',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
