# Generated by Django 5.0.1 on 2024-02-15 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_rename_studentage_student_age_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]