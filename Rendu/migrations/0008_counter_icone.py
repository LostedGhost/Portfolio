# Generated by Django 5.0.6 on 2024-05-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rendu', '0007_alter_experience_date_fin'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='icone',
            field=models.CharField(default='bi bi-check', max_length=10),
        ),
    ]
