# Generated by Django 4.2.3 on 2023-07-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0006_remove_subject_doctor_remove_subject_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]