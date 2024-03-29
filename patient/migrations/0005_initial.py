# Generated by Django 5.0.1 on 2024-02-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0004_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('age', models.CharField(max_length=5)),
                ('disease', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
