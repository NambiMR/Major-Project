# Generated by Django 5.0.1 on 2024-03-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Naachiyar', '0007_project_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Rate',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
