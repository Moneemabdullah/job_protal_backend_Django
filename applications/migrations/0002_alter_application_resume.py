# Generated by Django 5.0.6 on 2024-08-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(upload_to='applications/resumes/'),
        ),
    ]
