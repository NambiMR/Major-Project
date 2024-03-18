# Generated by Django 5.0.1 on 2024-03-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Naachiyar', '0006_employee_feedback_rename_mobil_job_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('client_name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=250)),
                ('budget', models.CharField(max_length=50)),
                ('s_date', models.DateField(blank=True, default=None, null=True)),
                ('status', models.CharField(max_length=50)),
                ('e_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]